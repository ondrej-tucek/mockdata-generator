"""
Provides functions for generating dates, times, names, surnames,
emails, JSON objects and also files and directories.
"""

__author__ = "Ondrej Tucek"
__email__ = "ondrej.tucek@gmail.com"
__license__ = "MIT"
__version__ = "0.0.1"
__status__ = "Development"

from utils.generate import *
from utils.open_save_file import open_file


if __name__ == '__main__':

    number_of_files = 10
    number_of_dir = 10
    func_args = {
        'year_from': 1950,
        'year_to': 2017,
        'order_ymd': 'myd',
        'date_sep': '/',
        'dt_sep': 'T',
        'time_sep': ':'
    }
    file_format = "txt"

    print(generate_time())
    print(generate_time({'time_sep': ':'}))

    # print(generate_year_month_day())
    # print(generate_year_month_day(func_args))
    # print(generate_year_month_day({'order_ymd': 'dmy'}))

    # print(generate_date())
    # print(generate_date(func_args))
    # print(generate_date({'order_ymd': 'dmy'}))

    # print(generate_date_time())
    # print(generate_date_time(func_args))

    # generate_files(number_of_files, generate_date_time, {}, file_format)
    # path_to_dir = '/temp'
    # generate_files(number_of_files, generate_date_time, func_args, file_format, path_to_dir)
    # generate_directories(number_of_dir, generate_date_time, func_args)
    # generate_directories(number_of_dir, generate_date_time, func_args, path_to_dir)

    input_files = ['females_name.txt', 'surnames.txt', 'servers_name.txt']
    directory_data = 'source_data/'
    args = {
        'name_sep': '.',
        'server_domain': generate_domain(),
        'names': list(map(
            lambda data:
            open_file(directory_data + str(data)),
            input_files))
    }
    email = generate_email()
    print(email)


    print(generate_email(args))

