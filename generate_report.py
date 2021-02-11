from jinja2 import Template
from os import path
from csv import reader
from typing import NamedTuple


class ProwlerTestResult(NamedTuple):
    profile: str
    account_id: str
    region: str
    title_id: str
    result: str
    scored: str
    level: str
    title_text: str
    notes: str
    compliance: str
    severity: str
    service_name: str


class Total:
    def __init__(self, results):
        self._results = results
        self._by_sev = {}

        self._parse()

    def _parse(self):
        for r in self._results:
            self._by_sev.setdefault(r.severity.lower(), 0)
            self._by_sev[r.severity.lower()] += 1

    @property
    def accounts(self):
        return set([r.account_id for r in self._results])

    @property
    def regions(self):
        return set([r.region for r in self._results])

    @property
    def scan_results(self):
        return len(self._results)

    @property
    def passes(self):
        return self._by_result('PASS')

    @property
    def fails(self):
        return self._by_result('FAIL')

    @property
    def infos(self):
        return self._by_result('INFO')

    def _by_result(self, result: str):
        # NOTE: Don't use a generator since the caller may want to
        #       inspect the size of the dataset.
        return [r for r in self._results if r.result == result]

    @property
    def all_by_sev(self):
        return self._by_sev

    @property
    def passes_by_sev(self):
        return self._by_sev['PASS']  # idk what this has

    def __iter__(self):
        yield next(self._results)

def run():
    with open('template.html') as f:
        tpl = f.read()

    with open('prowler-test.csv') as csv_file:
        csv_reader = reader(csv_file, delimiter=',')
        next(csv_reader, None)
        totals = Total(list(map(ProwlerTestResult._make), csv_reader))
        csv_data = total._results

    tpl = Template(tpl)
    rendered = tpl.render(data=csv_data, totals=totals)

    with open('report.html', 'w') as f:
        f.write(rendered)
        print('Generated report as "report.html"')


if __name__ == '__main__':
    run()
