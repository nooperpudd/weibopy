# encoding:utf-8

from setuptools import setup, find_packages

from weibopy import __version__

setup(
    name="weibopy",
    version=__version__,
    description="Weibo API SDK",
    long_description=open("README.md").read(),
    author="Winton Wang",
    url="https://coding.net/u/wefindx/p/weibopy/git",
    license="BSD",
    author_email="365504029@qq.com",
    packages=find_packages(),
    install_requires=["requests"],
    zip_safe=False,
    classifiers=[
        "Topic :: Software Development",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        'Environment :: Web Environment',
    ]

)
