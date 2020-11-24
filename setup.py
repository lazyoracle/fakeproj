"""
setup file for installing package
"""

from setuptools import setup

setup(
    name="fakeproj",
    version="1.0",
    url="https://github.com/lazyoracle/fakeproj",
    author="Anurag Saha Roy",
    author_email="anurag.roni@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
    ],
    include_package_data=True,
    packages=["fakeproj", "fakeproj/fakedir", "fakeproj/gooddir", "fakeproj/slowdir"],
    description="Mostly useless code to demonstrate Python DevOps tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["numpy==1.19.0"],
    python_requires=">=3.6",
)
