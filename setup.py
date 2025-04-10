# setup.py
from setuptools import setup, find_packages

setup(
    name="ei_appium",  # Name of your library
    version="0.1.0",   # Version of your library
    packages=find_packages(),  # Automatically find all packages in the directory
    install_requires=[
        'appium-python-client',
        'requests'
    ],
    description="A library for controlling settings and mobile application automation on Android devices using Appium.",
    author="Aditya Patel",
    author_email="aditya.patel@einfochips.com",
    license="MIT",
)
