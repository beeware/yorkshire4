#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages


with io.open('./yorkshire4/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='yorkshire4',
    version=version,
    description="A support library for the Yorkshire4 games",
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='https://yorkshire4.readthedocs.io/',
    license='New BSD',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'toga>=0.3.0.dev9'
    ],
    entry_points={
        'console_scripts': [
            'c64 = yorkshire4.app:c64',
            'microbee = yorkshire4.app:microbee',
            'zxspectrum = yorkshire4.app:zxspectrum',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    # test_suite='tests'
)
