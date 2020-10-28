"""
setup file for installing package
"""

from distutils.core import setup

setup(
    name="fakeproj",
    version="1.0rc",
    packages=["fakeproj", "fakeproj/fakedir"],
    long_description=open("README.md").read(),
    install_requires=["numpy==1.19.2"],
)
