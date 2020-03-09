#!/usr/bin/env python3

from distutils.core import setup


setup(
    name="radicale_modoboa_token_auth",
    version='0.1.0',
    description='A token based authentication plugin for Radicale provided by Modoboa.',
    url='https://github.com/modoboa/radicale-modoboa-auth-token',
    author='Antoine Nguyen',
    author_email='tonio@ngyn.org',
    license='MIT',
    packages=["radicale_modoboa_token_auth"],
    install_requires=['radicale'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: POSIX',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: 3.8'
    ]
)
