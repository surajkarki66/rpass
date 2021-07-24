#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import pathlib


README = (pathlib.Path(__file__).parent / "README.md").read_text()


def read_requirements():
    try:
        with open("requirements.txt") as req:
            content = req.read()
        requirements = content.split("\n")
    except IOError:
        print("requirements.txt is not found")

    return requirements


setup(
    name="rpass",
    description="A simple commandline app for generating strong random passwords",
    version="0.0.1",
    packages=find_packages(),
    install_requires=read_requirements(),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        rpass=rpass.__main__:main
    """,
    author="Suraj Karki",
    keywords="rpass, generate, passlist",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/surajkarki66/rpass",
    author_email="suraj.karki500@protonmail.com",
    license="MIT",
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Topic :: Utilities',
      ],
)
