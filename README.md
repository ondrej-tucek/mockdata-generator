
Mock/fake data creator. Of course there exist another a couple projects in Python, see:
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
# run_generate.py
from random import choice

from utils.generate import *
from utils.open_save_file import *


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
```

<table>
    <!--<tr><td  colspan="3"></td></tr>-->
    <thead style="border-bottom: 3px solid #FF7F0E; border-top: 3px solid #FF7F0E;">
    <tr>
        <th>Function arguments</th>
        <th>Function usage</th>
        <th>Output</th>
    </tr>
    </thead>
    <tr>
        <td colspan="3"><b>generating of times</b></td>
    </tr>
    <tr>
        <td rowspan="3">args = {
            <div style="padding-left:15px;">
                'time_sep': ':'
            </div>}
        </td>
        <td>generate_time()</td>
        <td>08-40</td>
    </tr>
    <tr>
        <td>generate_time(args)</td>
        <td>09:40</td>
    </tr>
    <tr>
        <td colspan="2">
            <sub>
                Default value of 'time_sep' is '-'.
            </sub>
        </td>
    </tr>
    <tr>
        <td colspan="3"><b>generating of year, month and day as tuple</b></td>
    </tr>
    <tr>
        <td rowspan="3" style="width: 180px;">args = {
            <div style="padding-left:15px;">
                'year_from': 1950,
                'year_to': 2017,
                'order_ymd': 'dmy'
            </div>}
        </td>
        <td>generate_year_month_day()</td>
        <td>(1983, 7, 4)</td>
    </tr>
    <tr>
        <td>generate_year_month_day(args)</td>
        <td>(23, 11, 1932)</td>
    </tr>
    <tr>
        <td colspan="2">
            <sub>Default values are set up on
                'year_from': 1900,
                'year_to': current year,
                'order_ymd': 'ymd' ('myd', 'dmy')
            </sub>
        </td>
    </tr>
    <tr>
        <td colspan="3"><b>generating of dates</b></td>
    </tr>
    <tr>
        <td rowspan="3">args = {
            <div style="padding-left:15px;">
                'year_from': 1950,
                'year_to': 2017,
                'date_sep': '/'
            </div>}
        </td>
        <td>generate_date()</td>
        <td>1966-10-17</td>
    </tr>
    <tr>
        <td>generate_date(args)</td>
        <td>1976/09/23</td>
    </tr>
    <tr>
        <td colspan="2">
            <sub>Default values are set up on
                'year_from': 1900,
                'year_to': current year,
                'date_sep': '-'
            </sub>
        </td>
    </tr>
    <tr>
        <td colspan="3"><b>generating of dates and times</b></td>
    </tr>
    <tr>
        <td rowspan="3">args = {
            <div style="padding-left:15px;">
                'year_from': 1950,
                'year_to': 2017,
                'order_ymd': 'dmy',
                'date_sep': '/',
                'dt_sep': 'T',
                'time_sep': ':'
            </div>}
        </td>
        <td>generate_date_time()</td>
        <td>1933-02-19--17-31</td>
    </tr>
    <tr>
        <td>generate_date_time(args)</td>
        <td>02/06/1993T22:08</td>
    </tr>
    <tr>
        <td colspan="2">
            <sub>Default values are set up on
                'year_from': 1900,
                'year_to': current year,
                'date_sep': '-',
                'dt_sep': '--',
                'time_sep': '-'
            </sub>
        </td>
    </tr>
    <tr>
        <td colspan="3"><b>generating files</b></td>
    </tr>
    <tr>
        <td rowspan="3">
            number_of_files = 10</br>
            generate_func = <div style="padding-left:15px;">generate_date_time </div>
            func_args = {...}</br>
            file_format = "txt"</br>
            path_to_exist_dir = <div style="padding-left:15px;">'/temp/gen_files'</div>
        </td>
        <td>generate_files(
                <div style="padding-left:15px;">number_of_files, generate_func, </br>func_args, file_format
                </div>)
        </td>
        <td>in directory 'generated_data' is 10 txt files</td>
    </tr>
    <tr>
        <td>
            generate_files(
                <div style="padding-left:15px;">number_of_files, generate_date_time, func_args, file_format, path_to_exist_dir
                </div>)</td>
        <td>in directory '/temp/gen_files'</br> is 10 txt files</td>
    </tr>
    <tr>
        <td colspan="2"><sub>Default directory for generated files is in 'generated_data'.
        Note: Output of generate_func has to be permissible string. 'Permissible' means
        what your system allows to save on your hard drive.</sub>
    </tr>
    <tr>
        <td colspan="3"><b>generating directories</b></td>
    </tr>
    <tr>
        <td rowspan="3">
            number_of_dir = 10</br>
            generate_func = <div style="padding-left:15px;">generate_date_time </div>
            func_args = {...}</br>
            path_to_exist_dir = <div style="padding-left:15px;">'/temp/gen_dirs'</div>
        </td>
        <td>generate_directories(
            <div style="padding-left:15px;">number_of_dir, generate_func, func_args
            </div>)
        </td>
        <td>in directory 'generated_data' is 10 txt directories</td>
    </tr>
    <tr>
        <td>generate_directories(
            <div style="padding-left:15px;">number_of_dir, generate_date_time, func_args, path_to_exist_dir
            </div>)</td>
        <td>in directory '/temp/gen_dirs' is 10 txt directories</td>
    </tr>
    <tr>
        <td colspan="2"><sub>Default directory for generated directories is in 'generated_data'.
        Note: Output of generate_func has to be permissible string. 'Permissible' means
        what your system allows to save on your hard drive.</sub>
    </tr>
    <tr>
        <td colspan="3"><b>generating of domains</b></td>
    </tr>
    <tr>
        <td rowspan="3">None</td>
        <td>generate_domain()</td>
        <td>ya</td>
    </tr>
    <tr>
        <td>generate_domain()</td>
        <td>oki</td>
    </tr>
    <tr>
        <td colspan="2"><sub>Function generates two-letter or three-letter server domain.</sub>
    </tr>
    <tr>
        <td colspan="3"><b>generating of emails</b></td>
    </tr>
    <tr>
        <td rowspan="3">args = {
            <div style="padding-left:15px;">
                'name_sep': '.',
                'server_domain': <div style="padding-left:15px;">generate_domain(),</div>
                'names': <div style="padding-left:15px;">
                    ['_females_name.txt', '_surnames.txt', '_websites_name.txt'],
                        </div>
                'directory_data': <div style="padding-left:15px;">'source_data/'</div>
            </div>}
        </td>
        <td>generate_email()</td>
        <td>Elvis.Wexcombe@escavalie.cj</td>
    </tr>
    <tr>
        <td>generate_email(args)</td>
        <td>Kirstin.Westbrook@lilligant.shi</td>
    </tr>
    <tr>
        <td colspan="2">
            <sub>
                Default values are set up on
                'names': [_males_name.txt', '_surnames.txt', '_websites_name.txt']
            </sub>
        </td>
    <tr>
        <td colspan="3"><b>generating of websites</b></td>
    </tr>
    </tr>
        <td rowspan="3"># list of strings</br>
        websites_data = open_file('source_data/_websites_name.txt')</br>
        OR</br>
        args = {
            <div style="padding-left:15px;">
                'websites_data': websites_data
            </div>}
        </td>
        <td>generate_website()</td>
        <td>serperior.pu</td>
    </tr>
    <tr>
        <td>generate_website(websites_data)</td>
        <td>swanna.nq</td>
    </tr>
    <tr>
        <td>generate_website(args)</td>
        <td>eelektros.gh</td>
    </tr>
    <tr>
        <td colspan="3"><b>data from your file</b></td>
    </tr>
    <tr>
        <td rowspan="3">
            Function arguments are name of file (this file has to be saved
            in source_data directory) or name of file and path to your directory where is file.
            Each content of row (in input file ) is saved as one string element of list.
        </td>
        <td>data_from_file('_females_name.txt')</td>
        <td>Hannah</td>
    </tr>
    <tr>
        <td>data_from_file('your_file.format', 'path_to_dir_data')</td>
        <td>Sienna</td>
    </tr>
    <tr>
        <td colspan="2"><sub>Default value of 'default_dir_data' is 'source_data/'.</sub>
        </td>
    </tr>
    <tr>
        <td colspan="3"><b>generating array for JSON object</b></td>
    </tr>
    <tr>
        <td rowspan="5">
            num_of_el = 3</br>
            generate_func = generate_date_time</br>
            sorting = ...</br>
            args = {
            <div style="padding-left:15px;">
                'dt_sep': 'T',</br>
                'time_sep': ':'
            </div>}
        </td>
        <td>generate_array(
            <div style="padding-left:15px;">num_of_el, generate_func
            </div>)
        </td>
        <td>['1987-02-09--22-35', '1974-01-22--16-52', '1963-02-05--14-53']</td>
    </tr>
    <tr>
        <td>generate_array(
            <div style="padding-left:15px;">num_of_el, generate_func, 'no_sort'
            </div>)
        </td>
        <td>['1986-08-27T15:13', '1967-11-14T18:25', '1918-11-12T16:16']</td>
    </tr>
    <tr>
        <td>generate_array(
            <div style="padding-left:15px;">num_of_el, generate_func, 'sort_desc'
            </div>)
        </td>
        <td>['1980-06-23--11-49', '1976-01-24--19-33', '1968-04-13--16-38']</td>
    </tr>
    <tr>
        <td>generate_array(
            <div style="padding-left:15px;">num_of_el, generate_func, args
            </div>)
        </td>
        <td>['1901-01-26T20:00', '1912-06-10T04:18', '1915-03-31T21:45']</td>
    </tr>
    <tr>
        <td colspan="2">
            <sub>
                Default value of sorting is set up on 'sort_asc' and can be 'sort_asc',
                'sort_desc' or 'no_sort'.
            </sub>
        </td>
    </tr>
</table>


## License
[![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)](https://github.com/ondrej-tucek/mockdata-generator/blob/master/LICENSE)