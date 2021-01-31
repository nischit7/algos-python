#!/usr/bin/env python3
"""
Python build setup.
"""
import os

from setuptools import setup, find_packages, Command


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info .eggs .pytest_cache')

CURR_DIR = os.path.abspath(os.path.dirname(__file__))

PACKAGES = ['lib', 'constants']

ABOUT = {}
with open(os.path.join(
        CURR_DIR, '__version__.py'), 'r', encoding="utf-8") as f:
    exec(f.read(), ABOUT) # pylint: disable=W0122

with open('README.md', 'r', encoding='utf-8') as f:
    README = f.read()

with open('requirements.txt') as f:
    REQUIRES = f.read().splitlines()

setup(
    name=ABOUT['__title__'],
    version=ABOUT['__version__'],
    description=ABOUT['__description__'],
    long_description=README,
    author=ABOUT['__author__'],
    author_email=ABOUT['__author_email__'],
    packages=find_packages(exclude=['tests']),
    package_dir={'lib': 'lib', 'constants': 'constants'},
    install_requires=REQUIRES,
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
        'Programming Language :: Python :: Implementation :: CPython'
    ),
    cmdclass={
        'clean': CleanCommand,
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    use_2to3=False
)
