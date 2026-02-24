# coding: utf-8

import os
from setuptools import setup, find_packages  # noqa: F401

NAME = "justserpapi"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.9"
REQUIRES = [
    "urllib3 >= 2.1.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Professional Python SDK for JustSerpAPI",
    author="JustSerpAPI Team",
    author_email="support@justserpapi.com",
    url="https://api.justserpapi.com",
    keywords=["OpenAPI", "OpenAPI-Generator", "JustSerpAPI", "SERP"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    long_description=open("README.md").read(),
    python_requires=PYTHON_REQUIRES,
)
