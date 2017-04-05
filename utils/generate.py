"""
Provides functions for generating dates, times, names, surnames,
emails, JSON objects and also files and directories.
"""

__author__ = "Ondrej Tucek"
__email__ = "ondrej.tucek@gmail.com"
__license__ = "MIT"
__version__ = "0.0.1"
__status__ = "Development"

from os import makedirs, path, getcwd
from datetime import date, datetime
from random import choice, randint
from calendar import Calendar
from string import ascii_lowercase, ascii_uppercase

from utils.open_save_file import open_file


def generate_time(args=None):
    """
    This function generates only time values, i.e. hour and minute
    with separator beetwen them. The user can change or define
    this separator inside args dictionary as 'time_sep': ':'.

    Usage:
        generate_time() -> 15-23
        generate_time({'time_sep': ':'}) -> 08:45

    Args:
        args (dict):
            -> 'time_sep' (str): Separator between hour and minute.

    Returns:
        string: Time in format "HH'time_sep'MM".

    Notes:
        - Default value of 'time_sep' is string '-'.
        - Hour is range of [0, 23] and minute in [0, 59].

    Raises:
        TypeError: - If 'time_sep' is not string.

    """

    if args:
        if not 'time_sep' in args:
            time_sep = '-'
        else:
            time_sep = args['time_sep']
            if not isinstance(time_sep, str):
                raise TypeError("Variable 'time_sep' has to be string!")
    else:
        time_sep = '-'

    hour = str(randint(0, 23)).zfill(2)
    minute = str(randint(0, 59)).zfill(2)

    return "%s%s%s" % (hour, time_sep, minute)


def generate_year_month_day(args=None):
    """
    This function generates year, month and day values.

    Usage:
        generate_year_month_day() -> (1986, 06, 20)
        or

        generate_year_month_day(
            {'order_ymd': 'dmy'}
        ) -> (2, 3, 1928)

        or

        fun_args = {
            'year_from': 1950,
            'year_to': 2017,
            ...
        }
        generate_year_month_day(fun_args) -> (1906, 12, 03)

    Args:
        args (dict):
            -> 'year_from' (int): since when date will be generated.
            -> 'year_to' (int): until when date will be generated.
            -> 'order_ymd' (str): order of year, month and day. User
                can choose only three options: 'ymd', 'mdy', 'dmy'.

    Returns:
        string: Tuple values of year, month and day in defined order.

    Notes:
        - Default value of 'year_from' is 1900 and year_to = current year.
        - Default order is 'ymd', i.e. (year, month, day).

    Raises:
        ValueError: - If 'year_from' is greater than 'year_to'.
                    - If 'order_ymd' is not 'ymd', 'dmy' either 'myd'.
        TypeError: - If 'year_from' and 'year_to' are not integer.
                   - If 'order_ymd' is not string.

    """

    order_ymd = ''
    if args:
        if not 'year_from' in args:
            year_from = 1900
        else:
            year_from = args['year_from']
            if not isinstance(year_from, int):
                raise TypeError("Variable 'year_from' has to be integer!")

        if not 'year_to' in args:
            year_to = datetime.now().year
        else:
            year_to = args['year_to']
            if not isinstance(year_to, int):
                raise TypeError("Variable 'year_to' has to be integer!")

        if year_from > year_to:
            raise ValueError(
                "Variable 'year_from' has to be less than 'year_to'!"
            )

        if 'order_ymd' in args:
            order_ymd = args['order_ymd']
            if not isinstance(order_ymd, str):
                raise TypeError("Variable 'order_ymd' has to be string!")
            if not (
                    order_ymd == 'ymd' or \
                    order_ymd == 'dmy' or \
                    order_ymd == 'myd'
            ):
                raise ValueError("Variable 'order_ymd' has to be either 'ymd', 'dmy' or 'myd'!")
    else:
        year_from = 1900
        year_to = datetime.now().year

    cal = Calendar()
    year = randint(year_from, year_to)
    month = randint(1, 12)
    day_list = list(filter(lambda x: x != 0, cal.itermonthdays(year, month)))
    day = choice(day_list)

    if order_ymd == 'dmy':
        order_ymd = (day, month, year)
    elif order_ymd == 'myd':
        order_ymd = (month, year, day)
    else:
        order_ymd = (year, month, day)

    return order_ymd


def generate_date(args=None):
    """
    This function generates only date values, i.e. year, month and day
    with separator beetwen them. The user can change or define this
    separator inside args dictionary as it's wrriten below in Usage.

    Usage:
        generate_date() -> 1986-06-20

        or

        fun_args = {
            ...
            'year_from': 1950,
            'year_to': 2017,
            'date_sep': '/'
            ...
        }
        generate_date(fun_args) -> 2007/06/15

    Args:
        args (dict):
            -> 'year_from' (int): since when date will be generated.
            -> 'year_to' (int): until when date will be generated.
            -> 'date_sep' (str): Separator between year, month and day.

    Returns:
        string: Date in format "YYYY'date_sep'MM'date_sep'DD".

    Notes:
        - Default value of 'year_from' is 1900 and year_to = current year.
        - Default value of 'date_sep' is string '-'.

    Raises:
        TypeError: - If 'date_sep' is not string.

    """

    if args:
        if not 'date_sep' in args:
            date_sep = '-'
        else:
            date_sep = args['date_sep']
            if not isinstance(date_sep, str):
                raise TypeError("Variable 'date_sep' has to be string!")

        a, b, c = tuple(
            map(
                lambda el: str(el).zfill(2), generate_year_month_day(args)
            )
        )

        if not 'order_ymd' in args or args['order_ymd'] == 'ymd':
            return '%s%s%s%s%s' % (a, date_sep, b, date_sep, c)
        elif args['order_ymd'] == 'dmy':
            return '%s%s%s%s%s' % (a, date_sep, b, date_sep, c)
        elif args['order_ymd'] == 'myd':
            return '%s%s%s%s%s' % (a, date_sep, b, date_sep, c)
    else:
        year, month, day = generate_year_month_day()

        return date(year, month, day).isoformat()


def generate_date_time(args=None):
    """
    This function generates date and time values with two separators
    beetwen them. The user can change or define these separators inside
    args dictionary as it's wrriten below in Usage.

    Usage:
        generate_date_time() -> 1929-09-09--03-36

        or

        fun_args = {
            ...
            'year_from': 1950,
            'year_to': 2017,
            'date_sep': '/',
            'dt_sep': '--',
            'time_sep': 'T'
            ...
        }
        generate_date_time(fun_args) -> 2007/06/15T17:09

    Args:
        args (dict):
            -> 'year_from' (int): since when date will be generated.
            -> 'year_to' (int): until when date will be generated.
            -> 'date_sep' (str): Separator between year, month and day.
            -> 'dt_sep' (str): Separator between date and time.
            -> 'time_sep' (str): Separator between hour and minute.

    Returns:
        string: Date and time in format
            "YYYY'date_sep'MM'date_sep'DD'dt_sep'HH'time_sep'MM".

    Notes:
        - Default value of 'year_from' is 1900 and year_to = current year.
        - Hour is range of [0, 23] and minute in [0, 59].
        - Default value of 'date_sep' is string '-'.
        - Default value of 'dt_sep' is string '--'.
        - Default value of 'time_sep' is string '-'.

    Raises:
        TypeError: - If 'dt_sep' is not string.

    """

    if args:
        if not 'dt_sep' in args:
            dt_sep = '--'
        else:
            dt_sep = args['dt_sep']
            if not isinstance(dt_sep, str):
                raise TypeError("Variable 'dt_sep' has to be string!")

        ymd = generate_date(args)
        hhmm = generate_time(args)

        return "%s%s%s" % (ymd, dt_sep, hhmm)

    else:
        dt_sep = '--'
        ymd = generate_date()
        hhmm = generate_time()

        return "%s%s%s" % (ymd, dt_sep, hhmm)


def generate_domain():
    """
    This function generates two-letter or three-letter server domain.

    Usage:
        generate_domain() -> ad

    Args:
        None.

    Returns:
        string: Two-letter or three-letter server domain, e.g. ad, eww, ...

    Raises:
        ValueError: If 'year_from' is greater than 'year_to'.
        TypeError: If 'year_from' and 'year_to' is not integer.

    """

    first_letter = choice(ascii_lowercase)
    second_letter = choice(ascii_lowercase)
    third_letter = choice(ascii_lowercase)

    if first_letter < second_letter:
        return '%s%s' % (first_letter, second_letter)
    else:
        return '%s%s%s' % (first_letter, second_letter, third_letter)


def generate_email(args=None):
    """
    This function generates emails.
    """

    if args:
        # firstname, surname, name_sep, server_name, server_domain
        # names[0], names[1], separator, names[2], server_domain
        names = list(
            map(
                lambda data:
                open_file('%s%s' % (args['directory_data'], str(data))),
                args['names']
            )
        )

        return '%s%s%s@%s.%s' % (
            choice(names[0]).strip(),
            args['name_sep'].strip(),
            choice(names[1]).strip(),
            choice(names[2]).strip(),
            args['server_domain'].strip()
        )
    else:
        args = {
            'name_sep': '.',
            'server_domain': generate_domain(),
            'names': ['_males_name.txt', '_surnames.txt', '_websites_name.txt'],
            'directory_data': 'source_data/'
        }
        return generate_email(args)


def generate_website(args=None):

    if args:
        if isinstance(args, list):
            return choice(args).strip() + '.' + generate_domain()

        if not 'websites_data' in args:
            websites_data = open_file('source_data/_websites_name.txt')

            return choice(websites_data).strip() + '.' + generate_domain()
        else:
            websites_data = args['websites_data']
            if not isinstance(websites_data, list):
                raise TypeError("Variable 'websites_data' has to be list!")

            return choice(websites_data).strip() + '.' + generate_domain()
    else:
        websites_data = open_file('source_data/_websites_name.txt')

        return choice(websites_data).strip() + '.' + generate_domain()


def data_from_file(infile, default_dir_data='source_data/'):
    data_dir = default_dir_data + infile
    data = open_file(data_dir)

    return data


def generate_files(
        number_of_files, func, func_args, file_format,
        name_dir='generated_data'
    ):
    """
    This function generates files on based function func and args.
    These files are saved in default directory 'generated_data'.
    The user can define number of generated files and their file
    format. And also /path/to/directory where generated files will
    be saved.

    Usage:
        generate_files(
            10, generate_date_time, {}, 'txt'
        ) -> generated_data/1995-09-24--01-04.txt,..., 10 diff files

        generate_files(
            10, generate_date_time, {}, 'txt', '/path/to/your/directory'
        ) -> directory/1995-09-24--01-04.txt,..., 10 diff files

    Args:
        'number_of_files' (int): Number of generated files.
        'func' (func): Name of generate function with permissible
            string output. 'Permissible' means what your system
            allows to save on your hard drive.
        'func_args' (dict): Dictionary contains input args for
            generate functions.
        'file_format' (str): Format of generated files, e.g txt.
        'name_dir' (str): Name of directory where are saved generated
            files or can contain path to user's defined directory.

    Returns:
        string: Generated files in directory 'generated_data' or
            user's defined dir.

    Notes:
        - Default value of 'name_dir' is 'generated_data'.

    """

    if name_dir == 'generated_data':
        dir_save = getcwd() + '/' + name_dir + '/'
    else:
        dir_save = name_dir + '/'

    num = 0
    while num < number_of_files:
        file_name = "%s.%s" % (func(func_args), file_format)
        check_file = dir_save + file_name

        if path.exists(check_file):
            number_of_files += 1
        else:
            f = open(path.join(dir_save, file_name), "w")
            f.close()

        num += 1

    print("Your generated files were saved in '%s' directory." % (dir_save))


def generate_directories(
        number_of_dir, func, func_args, name_dir='generated_data'
    ):
    """
    This function generates directories on based function func and args.
    These directories are created in default directory 'generated_data'.
    The user can define number of generated directories and also
    /path/to/directory where generated files will be saved.

    Usage:
        generate_directories(
            10, generate_date_time, {}
        ) -> generated_data/1995-09-24--01-04,..., 10 diff directories

        generate_directories(
            10, generate_date_time, {}, '/path/to/your/directory'
        ) -> directory/1995-09-24--01-04,..., 10 diff directories

    Args:
        'number_of_dir' (int): Number of generated directories.
        'func' (func): Name of generate function with permissible
            string output. 'Permissible' means what your system
            allows to save on your hard drive.
        'func_args' (dict): Dictionary contains input args for
            generate functions.
        'name_dir' (str): Name of directory where are saved generated
            directories or can contain path to user's defined directory.

    Returns:
        string: Generated directories in directory 'generated_data' or
            user's defined dir.

    Notes:
        - Default value of 'name_dir' is 'generated_data'.

    """

    if name_dir == 'generated_data':
        dir_save = getcwd() + '/' + name_dir + '/'
    else:
        dir_save = name_dir + '/'

    num = 0
    while num < number_of_dir:
        dir_name = "%s" % (func(func_args))
        check_dir = dir_save + dir_name

        if path.exists(check_dir):
            number_of_dir += 1
        else:
            makedirs(check_dir)

        num += 1

    print("Your generated directories were saved in '%s' directory." % (dir_save))


def generate_array(num_of_element, func, *args):
    arr = []

    if args:
        if 1 == len(args):
            if isinstance(args[0], dict):
                arg = args[0]
                sorting = 'sort_asc'
            if isinstance(args[0], str):
                arg = {}
                sorting = args[0]
        elif 2 == len(args):
            if isinstance(args[0], dict):
                arg = args[0]
                sorting = args[1]
            if isinstance(args[0], str):
                arg = args[1]
                sorting = args[0]
        elif 2 < len(args):
            raise ValueError(
                "Arguments have to contain either None or dictionary-args for "
                "func and/or strings: {'sort_asc', 'sort_desc', 'no_sort'} "
                "for sorting!"
            )
    else:
        arg = {}
        sorting = 'sort_asc'

    for i in xrange(num_of_element):
        arr.append(
            func(arg)
        )

    if sorting == 'sort_asc':
        return sorted(arr)
    elif sorting == 'sort_desc':
        return sorted(arr, reverse=True)
    elif sorting == 'no_sort':
        return arr
    else:
        raise ValueError("Variable 'sorting' has to be either sort_asc, 'sort_desc' or 'no_sort'!")


def generate_VRP(args=None):
    """
    Vehicle registration plates
    """

    country_VRP = {
        'czech': ['A', 'B', 'C', 'E', 'H', 'J', 'K', 'L', 'M',\
            'P', 'S', 'T', 'U', 'V', 'Z'],
        'estonia': ['A', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',\
            'O', 'P', 'R', 'S', 'T', 'V']
    }

    if args:
        if 'code' in args:
            args_code = args['code']
        if not 'region' in args:
            print('je tam')
            args_region = ''

        if not isinstance(args_code, str):
            raise TypeError("Variable 'code' has to be string!")

        if args_code in country_VRP:
            if args_code == 'czech':

                digits = str(randint(0, 9999)).zfill(4)
                letter = choice(country_VRP['czech'])

                if bool(args_region.strip()) or not args_region in country_VRP['czech']:
                    letter = args_region
                else:
                    raise ValueError("Your 'region' code is wrong!")

                return "%s%s%s %s" % (str(randint(0, 9)), letter, str(randint(0, 9)), digits)

            elif args_code == 'estonia':
                pass
        else:
            raise ValueError(
                "Your country 'code' is not in our"
                "VRP's database or you wrote incorrect!"
            )
    else:
        return "%s%s%s %s" % (
            str(randint(0, 9)), choice(ascii_uppercase), str(randint(0, 9)),
            str(randint(0, 9999)).zfill(4)
        )


