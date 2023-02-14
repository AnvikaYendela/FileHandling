from pathlib import Path
from xml.etree import ElementTree
import csv

from FileHandling.Baseclass import get_file_path

# PARSE XML
if Path('output.xml').exists():
    xml = ElementTree.parse('output.xml')
else:
    print("no file found")

# CREATE CSV FILE
csvfile = open(get_file_path('.csv'), 'w', encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

# ADD THE HEADER TO CSV FILE
csvfile_writer.writerow(["failures", "skipped", "tests", "timestamp"])

for testsuite in xml.findall("testsuite"):

    if testsuite:
        failures = testsuite.get('failures')
        skipped = testsuite.get('skipped')
        tests = testsuite.get('tests')
        timestamp = testsuite.get('timestamp')
        csv_line = [failures, skipped, tests, timestamp]
        csvfile_writer.writerow(csv_line)
csvfile.close()
