#!/usr/bin/env python

import sys

from setuptools import find_packages, setup

install_requires = ['robotframework']
if sys.version_info < (2, 7):
    install_requires.append('argparse')


setup(
    name='pre_commit_robotframework_lint',
    description='A pre-commit hook to run robotframework-lint tool.',
    url='https://github.com/bonzaico/pre-commit-robotframework-lint',
    version='1.0.1',
    author='Debjit Biswas',
    author_email='debjit.biswas@bonzai.co',
    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            ('python-robotframework-lint = '
             'pre_commit_robotframework_lint.rf_tidy:main'),
        ],
    },
)
