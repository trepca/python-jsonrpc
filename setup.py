#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "jsonrpc",
    version = "0.1",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    description = "A json-rpc package which implements JSON-RPC over HTTP.",
    keywords = "JSON RPC",
    zip_safe = True,
    # author metadata
    author = "Jan-Klaas Kollhof",
    url = "http://json-rpc.org/wiki/python-json-rpc",
    license = "LGPL",
    long_description = """""",
    )
