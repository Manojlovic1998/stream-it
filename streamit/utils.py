import errno
from glob import glob
import os
import time
import sys
import json
import click


def sprint(string: str, timeout: float = None):
    """Streams logo to stdout device.
    Args:
        string (str): _Logo string_
        timeout (float): _Float value for which to timeout the stdout stream_
    """
    for char in string + "\n":
        # Write char to the stdout device
        sys.stdout.write(char)

        # Flush the buffer
        sys.stdout.flush()

        # Timeout output stream
        if timeout and isinstance(timeout, float):
            time.sleep(timeout)


def expand_path(path) -> list:
    """Uses expand methods to locate user directory.
    It reads the $HOME value on Unix or searches the password
    dir using built in module pwd.

    Args:
        path (string || bytes): _A path-like object representing a 
        file system path. It can be a string or bytes object._
    """
    paths = []
    # Expand paths that include (~) symbol.
    path = os.path.expanduser(path)

    # Expand variables in paths, in case of interpolation (${HOME}/dirName).
    path = os.path.expandvars(path)

    # Check if the path is dir.
    if os.path.isdir(path):
        # Generate a directory tree.
        for (dirpath, dirnames, filenames) in os.walk(path):
            for name in filenames:
                paths.append(os.path.join(dirpath, name))
    else:
        # Return a list of paths matching a pathname pattern.
        list_of_paths = glob(path)

        # Append elements from the iterable object to the paths list.
        paths.extend(list_of_paths)

    # Return list of paths
    return paths


def create_dir(path):
    """Tries to create a directory at given path.
    If directory already exists it raises exception."""
    try:
        os.makedirs(path)
    except OSError as error:
        # Check this link for list of errno:
        # https://kernel.googlesource.com/pub/scm/linux/kernel/git/nico/archive/+/v0.97/include/linux/errno.h

        # If the dir already exists do nothing
        # else print the error
        if error.errno == errno.EEXIST:
            pass
        else:
            print(error)


def json_format_validation(file):
    """Simple json format validation utility.
    Checks if the file has valid schema. 
    If valid return the json data, else raise error.

    Args:
        file (<class '_io.TextIOWrapper'>): Json file text stream.

    Raises:
        click.FileError: FileError in case the format of JSON
         file that is being loaded is not valid. 

    Returns:
        <class 'dict'>: Python dict containing json data from the input file.
    """
    try:
        return json.load(file)
    except ValueError as err:
        raise click.FileError(
            file.name, f"""The format of JSON file can not be loaded. \
                           Check if it is valid json format. Error: {err}""")
