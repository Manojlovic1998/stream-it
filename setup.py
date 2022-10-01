from importlib.metadata import entry_points
from setuptools import setup

setup(
    name="stream-it",
    description="CLI tool for downloading videos",
    url="https://github.com/Manojlovic1998/stream-it",
    version="0.0.0",
    py_modules=['stream-it'],
    install_requires=[
        "Click",
    ],
    license="MIT",
    entry_points='''
      [console_scripts]
      streamit=streamit:cli
      '''
)
