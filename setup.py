#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()
#    'datariumdb~=1.0.0'
install_requires = [
    'requests>=2.11.0',
]

tests_require = [
    'tox>=2.3.1',
    'coverage>=4.1',
    'flake8>=2.6.0',
    'pytest>=3.0.1',
    'pytest-cov',
    'pytest-env',
    'pytest-sugar',
    'pytest-xdist',
    'responses~=0.5.1',
]

dev_require = [
    'ipdb',
    'ipython',
]

docs_require = [
    'Sphinx>=1.3.5',
    'sphinx-autobuild',
    'sphinxcontrib-napoleon>=0.4.4',
    'sphinx_rtd_theme',
    'sphinxcontrib-httpdomain',
    'matplotlib',
]

setup(
    name='datariumdb_driver',
    version='1.0',
    description="Python driver for DatariumDB",
    long_description=readme + '\n\n' + changelog,
    author="DatariumDB",
    author_email='dev@datariumdb.com',
    url='https://github.com/datariumdb/datariumdb-driver',
    packages=[
        'datariumdb_driver',
    ],
    package_dir={'datariumdb_driver':
                 'datariumdb_driver'},
    include_package_data=True,
    install_requires=install_requires,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='datariumdb_driver',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    extras_require={
        'test': tests_require,
        'dev': dev_require + tests_require + docs_require,
        'docs': docs_require,
    },
)
