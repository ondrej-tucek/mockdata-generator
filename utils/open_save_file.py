"""
Provides functions for opening and saving files.
"""

__author__ = "Ondrej Tucek"
__email__ = "ondrej.tucek@gmail.com"
__license__ = "MIT"
__version__ = "0.0.1"
__status__ = "Development"

from os import error as os_error
from json import load as json_load, dump as json_dump
from csv import reader as csv_reader


def open_file(input_file, delim=','):
    """
    This function opens file and read data. In case of 'csv' file,
    delimiter is default set up on ','.

    Usage:
        mockdata.json = [{
            "website": "universe.com",
            "from": "milky way",
            "name": "Ummon"
        }]
        open_file('mockdata.json') -> list of mockdata

    Args:
        'input_file' (str): input file to procces.
        'delim' (str): delimiter for csv format of file.

    Returns:
        List of data from file.

    Notes:
        - Default value of 'delim' is string '-'.

    Raises:
        except IOError: - If it can't find file or read data.
        TypeError: - If 'delim' is not string.

    """

    try:
        if not isinstance(delim, str):
            raise TypeError("Variable 'delim' has to be string!")

        file_format = input_file.split('.')[1]
        if file_format == 'json':
            with open(input_file) as infile:
                return json_load(infile)
        elif file_format == 'txt':
            with open(input_file) as infile:
                # If you do not want \n included.
                # (Otherwise use infile.readlines().)
                return infile.read().splitlines()
        elif file_format == 'csv':
            with open(input_file) as infile:
                return csv_reader(infile, delimiter=delim)
    except (AttributeError, os_error):
        print("I/O error(%s): %s." % (os_error, AttributeError))
        print("Probable reason: '%s'" % (input_file.split('/')[-1]))


def save_file(data, file_name, file_format):
    """
    This function saves data to file.

    Usage:
        data = [{
            "website": "universe.com",
            "from": "milky way",
            "name": "Larry"
        }]
        save_file(data, 'mockdata', 'json') -> mockdata.json

    Args:
        'data' (obj): object where are saved data.
        'file_name' (str): name of file.
        'file_format' (str): format of file.

    Returns:
        None.

    Raises:
        ValueError: - If 'file_name' or 'file_format' are empty string.
        TypeError: - If 'file_name' or 'file_format' are not string.

    """

    if not isinstance(file_name, str):
        raise TypeError("Variable 'file_name' has to be string!")
    if not isinstance(file_format, str):
        raise TypeError("Variable 'file_format' has to be string!")
    if file_name == '':
        raise ValueError("Variable 'file_name' has not to be empty string!")
    if file_format == '':
        raise ValueError("Variable 'file_format' has not to be empty string!")

    file_name_format = file_name+'.'+file_format
    with open(file_name_format, 'w') as outfile:
        if file_format == 'json':
            json_dump(data, outfile)
        else:
            outfile.write(data)
            # print("{}".format(data), file=outfile)

