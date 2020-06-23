"""Authentication plugin for Radicale."""

from urllib.parse import parse_qs

import requests

from radicale_dovecot_auth import Auth as DovecotAuth


class Auth(DovecotAuth):
    """Allow read-only access using a token.

    If a token is not provided or is invalid, it will fallback to
    dovecot auth plugin.

    Configuration:

    [auth]
    type = radicale_modoboa_token_auth

    radicale_modoboa_token_auth_check_url = https://my.modoboa.com/api/v1/user-calendars/check_token/
    radicale_modoboa_token_auth_token = MYTOKENHERE

    """

    def get_external_login(self, environ):
        self._auth_is_ok = False
        try:
            check_token_url = self.configuration.get(
                'auth', 'radicale_modoboa_token_auth_check_url')
            api_token = self.configuration.get(
                'auth', 'radicale_modoboa_token_auth_token')
        except KeyError:
            raise RuntimeError('check_token_url and token must be set')

        if 'QUERY_STRING' not in environ:
            return ()
        qs = parse_qs(environ['QUERY_STRING'])
        if 'token' not in qs:
            return ()
        body = {
            'calendar': environ['PATH_INFO'].strip('/'),
            'token': qs['token'][0]
        }
        headers = {'Authorization': 'Token {}'.format(api_token)}
        response = requests.post(check_token_url, headers=headers, json=body)
        if response.status_code != 200 or response.json()['status'] != 'ok':
            return ()
        self._auth_is_ok = True
        return (qs['token'][0], '')

    def is_authenticated2(self, login, user, password):
        """Fallback to dovecot auth if needed."""
        if self._auth_is_ok:
            return True
        return super().is_authenticated2(login, user, password)
