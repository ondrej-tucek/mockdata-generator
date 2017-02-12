"""
Provides functions for generating dates, times, names, surnames,
emails, JSON objects and also files and directories.
"""

__author__ = "Ondrej Tucek"
__email__ = "ondrej.tucek@gmail.com"
__license__ = "MIT"
__version__ = "0.0.1"
__status__ = "Development"

from random import choice

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

    # print(generate_website())
    # print(generate_website(args))
    # print(generate_website(websites_data))


    settings = {
        'date_sep': '. ',
        'order_ymd': 'dmy'
    }

    data = {}
    users = 'users'
    data[users] = []
    items = ['item1', 'item2', 'item3']

    name_data = data_from_file('_females_name.txt')
    surname_data = data_from_file('_surnames.txt')
    website_data = data_from_file('_websites_name.txt')

    for i, item in enumerate(items):
        data[item] = []
        data[item].append({
            'id': i,
            'date': generate_date(),
            'time': generate_time()
        })

    for i in xrange(5):
        name = choice(name_data).strip()
        surname = choice(surname_data).strip()
        website = choice(website_data).strip()
        domain = generate_domain()

        data[users].append({
            'id': i,
            'name': name,
            'surname': surname,
            'website': 'www.'+website+'.'+domain,
            'email': name+'.'+surname+'@'+website+'.'+domain,
            'born': generate_date(settings),
            'log_dates': generate_array(
                5,
                generate_date_time,
                {'dt_sep': 'T', 'time_sep': ':'},
                'no_sort'
            )
        })

    save_file(data, 'mockdata.json')

