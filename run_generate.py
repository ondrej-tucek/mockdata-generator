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
from utils.open_save_file import *


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

    input_files = ['_females_name.txt', '_surnames.txt', '_websites_name.txt']
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


    websites_data = open_file('source_data/_websites_name.txt')
    args = {
        'websites_data': websites_data
    }

    print(generate_website())
    print(generate_website(args))
    print(generate_website(websites_data))

    print(generate_from_file('_females_name.txt'))


    data = {}
    settings = {
        'date_sep': '. ',
        'order_ymd': 'dmy'
    }
    users = 'users'
    log_dates = 'log_dates'
    data[users] = []
    log_dates = []

    for i in xrange(3):
        log_dates.append(
            generate_date_time()
        )

    for i in xrange(5):
        name = generate_from_file('_females_name.txt')
        surname = generate_from_file('_surnames.txt')
        website = generate_from_file('_websites_name.txt')
        domain = generate_domain()

        data[users].append({
            'id': i,
            'name': name,
            'surname': surname,
            'website': 'www.'+website+'.'+domain,
            'email': name+'.'+surname+'@'+website+'.'+domain,
            'born': generate_date(settings),
            'log_dates': log_dates
        })

    save_file(data, 'mockdata.json')

