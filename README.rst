radicale-modoboa-token-auth
===========================

A token based authentication plugin for Radicale provided by
Modoboa. If the authentication fails, it will fallback to dovecot
authentication plugin.

Installation
------------

You can install this package from PyPi using the following command::

   pip install radicale-modoboa-token-auth

Configuration
-------------

Here is a configuration example::

   [auth]
   type = radicale_modoboa_token_auth

   check_token_url = https://my.modoboa.com/api/v1/user-calendars/check_token/
   token = MYTOKENHERE

The `token` setting corresponds to a valid Modoboa API token.
