from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="stream-it",
    description="CLI tool for downloading videos",
    url="https://github.com/Manojlovic1998/stream-it",
    version="0.0.0",
    py_modules=['stream-it'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    license="MIT",
    entry_points={
        'console_scripts': [
            'streamit = streamit.scripts.streamit:cli'
        ]
    }
)
