#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import io
import sys

from setuptools import setup

version = "0.0.1"

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

with io.open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    'certifi>=2018.11.29',
    'chardet>=3.0.4',
    'idna>=2.8',
    'requests>=2.21.0',
    'urllib3>=1.24.0'
]

if sys.argv[-1] == 'readme':
    print(readme)
    sys.exit()


setup(
    name='actionsportsnetwork',
    version=version,
    description=('Action Sports Network API client'),
    long_description=readme,
    author='jim zhou',
    author_email='jimtje@gmail.com',
    url='https://github.com/jimtje/actionsportsnetwork',
    packages=[
        'actionsportsnetwork',
    ],
    package_dir={'actionsportsnetwork': 'actionsportsnetwork'},
    entry_points={
        'console_scripts': [
            'actionsportsnetwork = actionsportsnetwork.__main__:main',
        ]
    },
    include_package_data=True,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=requirements,
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
    keywords=(
        'action sports network', 'sports', 'api', 'betting', 'gambling'
    ),
)