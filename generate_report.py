from jinja2 import Template
from os import path
from csv import reader


def run():
    csv_data = {}

    with open('template.html') as f:
        tpl = f.read()

    with open('prowler-test.csv') as csv_file:
        csv_reader = reader(csv_file, delimiter=',')
        for idx, row in enumerate(csv_reader):
            csv_data[idx] = {
                'profile': row[0],
                'account_id': row[1],
                'region':  row[2],
                'title_id':  row[3],
                'result': row[4],
                'scored': row[5],
                'level':  row[6],
                'title_text':  row[7],
                'notes': row[8],
                'compliance': row[9],
                'severity': row[10],
                'service_name': row[11],
            }

    t = Template(tpl)
    rendered = t.render(data=csv_data)

    with open('report.html', 'w') as f:
        f.write(rendered)
        print('Generated report as "report.html"')


if __name__ == '__main__':
    run()
