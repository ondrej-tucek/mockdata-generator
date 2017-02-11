
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
```Python
data = {}
settings = {
    'date_sep': '. ',
    'order_ymd': 'dmy'
}
num_of_el = 5
users = 'users'
data[users] = []
name_data = data_from_file('_females_name.txt')
surname_data = data_from_file('_surnames.txt')
website_data = data_from_file('_websites_name.txt')

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
        'log_dates': generate_array(num_of_el, generate_date_time, {'dt_sep': 'T', 'time_sep': ':'}, 'no_sort')
    })

save_file(data, 'mockdata.json')
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
        <tr>
            <td rowspan="3">data from your file</td>
            <td>data_from_file('_females_name.txt')</td>
            <td>Hannah</td>
        </tr>
        <tr>
            <td>data_from_file('your_file.format', 'path_to_dir_data')</td>
            <td>Sienna</td>
        </tr>
        <tr>
            <td colspan="2"><sub>Function arguments are name of file (this file has to be saved
            in source_data directory) or name of file and path to your directory where is file.
            Each content of row (in input file ) is saved as one string element of list.
            Default value of 'default_dir_data' is 'source_data/'.</sub>
            </td>
        </tr>
        <tr>
            <td rowspan="5">generating array for JSON object</td>
            <td><sub>num_of_el = 5</sub></br>
                generate_array(num_of_el, generate_date_time)</td>
            <td>['1987-02-09--22-35', '1974-01-22--16-52', '1963-02-05--14-53',
            '1954-12-02--15-13', '1919-09-15--03-34']</td>
        </tr>
        <tr>
            <td><sub>num_of_el = 5</sub></br>
                generate_array(num_of_el, generate_date_time, 'no_sort')</td>
            <td>['1986-08-27T15:13', '1967-11-14T18:25', '1918-11-12T16:16',
                '1903-05-24T20:52', '1902-12-08T22:11']</td>
        </tr>
        <tr>
            <td><sub>num_of_el = 5</sub></br>
                generate_array(num_of_el, generate_date_time, 'sort_desc')</td>
            <td>['1980-06-23--11-49', '1976-01-24--19-33', '1968-04-13--16-38',
                '1950-10-16--08-07', '1909-05-20--14-44']</td>
        </tr>
        <tr>
            <td><sub>num_of_el = 5</sub></br>
                generate_array(num_of_el, generate_date_time, {'dt_sep': 'T', 'time_sep': ':'})</td>
            <td>['1901-01-26T20:00', '1912-06-10T04:18', '1915-03-31T21:45',
                '1934-10-22T21:30', '2017-03-02T20:09']</td>
        </tr>
        <tr>
            <td colspan="2"><sub>DESCRIPTION ASAP.</sub>
            </td>
        </tr>
    </table>
</center>

