# encoding:utf-8
import codecs
import os
import re

from setuptools import setup, find_packages


def find_version(*file_paths):
    """
    :return:
    """
    here = os.path.abspath(os.path.dirname(__file__))

    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', encoding="utf-8") as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="weibopy",
    version=find_version("weibopy", "__init__.py"),
    description="Sina Weibo API SDK",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    author="Winton Wang",
    url="https://github.com/nooperpudd/weibopy",
    license="BSD",
    author_email="365504029@qq.com",
    packages=find_packages(exclude=['*tests*']),
    install_requires=["requests>=2.18.1"],
    tests_require=["pytest",
                   "HTTPretty"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Environment :: Web Environment"
    ]

)
