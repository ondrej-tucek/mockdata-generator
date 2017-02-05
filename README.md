
Of course there exist another a couple projects in Python, see:
- [Barnum](https://github.com/chris1610/barnum-proj)
- [Yan DATA](http://www.yandataellan.com/)
- [Faker](https://github.com/joke2k/faker)

and on the web:
- [JSON Generator](http://beta.json-generator.com/)
- [Mockaroo](https://www.mockaroo.com/)



### Usage:
```
    $ ipython run_generate.py
```
```Python
# In run_generate.py you can define e.g.
args = {
    'year_from': 1950,
    'year_to': 2017,
    'order_ymd': 'dmy',
    'date_sep': '/',
    'dt_sep': '--',
    'time_sep': ':'
}
# ...
gd = generate_date()
print(gd)
```

<center>
    <table>
        <tr>
            <th>Description</th>
            <th>Function name</th>
            <th>Output</th>
        </tr>
        <tr>
            <td rowspan="3">generating of times</td>
            <td>generate_time()</td>
            <td>08-40</td>
        </tr>
        <tr>
            <td>generate_time({'time_sep': ':'})</td>
            <td>09:40</td>
        </tr>
        <tr>
            <td colspan="2"><sub>Function arguments are None or args = {'time_sep': ':'}
                Default value of 'time_sep' is '-'.</sub>
            </td>
        </tr>
        <tr></tr><tr></tr>
        <tr>
            <td rowspan="4">generating of year, month and day as tuple</td>
            <td>generate_year_month_day()</td>
            <td>(1983, 7, 4)</td>
        </tr>
        <tr>
            <td>generate_year_month_day(args)</td>
            <td>(1964, 8, 9)</td>
        </tr>
        <tr>
            <td>generate_year_month_day({'order_ymd': 'dmy'})</td>
            <td>(23, 11, 1932)</td>
        </tr>
        <tr>
            <td colspan="2"><sub>Function arguments are None or args = {
                    'year_from': 1950,
                    'year_to': 2017,
                    'order_ymd': 'dmy'
                    }. Default values are set up on
                    'year_from': 1900,
                    'year_to': current year,
                    'order_ymd': 'ymd' ('myd', 'dmy')
                </sub>
            </td>
        </tr>
        <tr>
            <td rowspan="3">generating of dates</td>
            <td>generate_date()</td>
            <td>1966-10-17</td>
        </tr>
        <tr>
            <td>generate_date(args)</td>
            <td>1976/09/23</td>
        </tr>
        <tr>
            <td colspan="2"><sub>Function arguments are None or args = {
                'year_from': 1950,
                'year_to': 2017,
                'date_sep': '/'
                }. Default values are set up on
                'year_from': 1900,
                'year_to': current year,
                'date_sep': '-'</sub>
            </td>
        </tr>
        <tr>
            <td rowspan="3">generating of dates and times</td>
            <td>generate_date_time()</td>
            <td>1933-02-19--17-31</td>
        </tr>
        <tr>
            <td>generate_date_time(args)</td>
            <td>02/06/1993T22:08</td>
        </tr>
        <tr>
            <td colspan="2"><sub>Function arguments are None or args = {
                'year_from': 1950,
                'year_to': 2017,
                'order_ymd': 'dmy',
                'date_sep': '/',
                'dt_sep': 'T',
                'time_sep': ':'
                }. Default values are set up on
                'year_from': 1900,
                'year_to': current year,
                'date_sep': '-',
                'dt_sep': '--',
                'time_sep': '-'
                </sub>
        </tr>
        <tr>
            <td rowspan="3">generating files</td>
            <td><sub>number_of_files = 10</br>
                file_format = "txt"</br></sub>
                generate_files(number_of_files, generate_date_time, func_args, file_format)</td>
            <td>in directory 'generated_data'</br> is 10 txt files</td>
        </tr>
        <tr>
            <td><sub>number_of_files = 10</br>
                file_format = "txt"</br>
                path_to_exist_dir = '/temp/gen_files'</br></sub>
                generate_files(number_of_files, generate_date_time, func_args, file_format, path_to_exist_dir)</td>
            <td>in directory '/temp/gen_files'</br> is 10 txt files</td>
        </tr>
        <tr>
            <td colspan="2"><sub>Function arguments are number_of_files, generate_func, func_args
            file_format and path_to_exist_dir. Default directory for generated files is in 'generated_data'.
            Note: Output of generate_func has to be permissible string. 'Permissible' means
            what your system allows to save on your hard drive.</sub>
        </tr>
        <tr>
            <td rowspan="3">generating directories</td>
            <td><sub>number_of_dir = 10</br></sub>
                generate_directories(number_of_dir, generate_date_time, func_args)</td>
            <td>in directory 'generated_data'</br> is 10 txt directories</td>
        </tr>
        <tr>
            <td><sub>number_of_dir = 10</br>
                path_to_exist_dir = '/temp/gen_dirs'</br></sub>
                generate_directories(number_of_dir, generate_date_time, func_args, path_to_exist_dir)</td>
            <td>in directory '/temp/gen_dirs'</br> is 10 txt directories</td>
        </tr>
        <tr>
            <td colspan="2"><sub>Function arguments are number_of_dir, generate_func, func_args
            and path_to_exist_dir. Default directory for generated directories is in 'generated_data'.
            Note: Output of generate_func has to be permissible string. 'Permissible' means
            what your system allows to save on your hard drive.</sub>
        </tr>
        <tr>
            <td rowspan="3">generating of domains</td>
            <td>generate_domain()</td>
            <td>ya</td>
        </tr>
        <tr>
            <td>generate_domain()</td>
            <td>oki</td>
        </tr>
        <tr>
            <td colspan="2"><sub>Function argument is None and generates two-letter or
            three-letter server domain.</sub>
        </tr>
        <tr>
            <td rowspan="3">generating of emails</td>
            <td>generate_email()</td>
            <td>Elvis.Wexcombe@escavalie.cj</td>
        </tr>
        <tr>
            <td>generate_email(args)</td>
            <td>Kirstin.Westbrook@lilligant.shi</td>
        </tr>
        <tr>
            <td colspan="2"><sub>Function arguments are None or args...NOT DONE.</sub>
        </tr>
            <td rowspan="4">generating of websites</td>
            <td>generate_website()</td>
            <td>serperior.pu</td>
        </tr>
        <tr>
            <td><sub>websites_data = open_file('source_data/_websites_name.txt')</br>
            args = {</br>
                'websites_data': websites_data</br>
            }</sub></br>
            generate_website(args)
            </td>
            <td>swanna.nq</td>
        </tr>
        <tr>
            <td><sub>websites_data = open_file('source_data/_websites_name.txt')</sub></br>
            generate_website(websites_data)
            </td>
            <td>eelektros.gh</td>
        </tr>
        <tr>
            <td colspan="2"><sub>Function arguments are None, args contains variable
            'websites_data' or list of strings.</sub>
            </td>
        </tr>
    </table>
</center>