from setuptools import setup, find_packages

setup(
    name="weatherprobe",
    version='0.1',
    description="A CLI application with login to fetch weather report",
    scripts=['weatherprobe/weatherprobe'],
    packages=find_packages(),
    author="Nandan M",
    author_email="nannigalaxy25@gmail.com",
)