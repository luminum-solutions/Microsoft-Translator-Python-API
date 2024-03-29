# -*- coding: utf-8 -*-
"""
    Microsoft translator API

    The Microsoft Translator services can be used in web or client
    applications to perform language translation operations. The services
    support users who are not familiar with the default language of a page or
    application, or those desiring to communicate with people of a different
    language group.

    This module implements the AJAX API for the Microsoft Translator service.

    An example::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your API Key>')
        >>> print translator.translate("Hello", "pt")
        "Olá"

    The documentation for the service can be obtained here:
    http://msdn.microsoft.com/en-us/library/ff512423.aspx

    The project is hosted on GitHub where your could fork the project or report
    issues. Visit https://github.com/openlabs/Microsoft-Translator-Python-API

    :copyright: © 2011 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import os
from setuptools import setup
import sys

PY_VERSION = sys.version_info[0], sys.version_info[1]

def read(fname):
    if PY_VERSION < (3, 0):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    else:
        return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

setup(
    name="microsofttranslator",
    version="0.5",
    packages=[
        'microsofttranslator',
    ],
    package_dir={
        'microsofttranslator': '.'
    },
    author="Openlabs Technologies & Consulting (P) Limited",
    author_email="info@openlabs.co.in",
    description="Microsoft Translator V2 - Python API",
    long_description=read('README.rst'),
    license="BSD",
    keywords="translation microsoft",
    url="http://openlabs.co.in/",
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
    ],
    test_suite="microsofttranslator.test.test_all",
    install_requires=[
        'requests >= 1.2.3',
    ]
)
