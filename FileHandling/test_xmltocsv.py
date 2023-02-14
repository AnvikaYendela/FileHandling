from _csv import writer
from pathlib import Path
from xml.etree import ElementTree
import csv

from FileHandling.Baseclass import get_file_path

# PARSE XML
if Path('output.xml').exists():
    xml = ElementTree.parse('output.xml')
else:
    print("no file found")


if Path(get_file_path('.csv')).exists():
    print('exists')
else:
    csvfile = open(get_file_path('.csv'), 'w', encoding='utf-8')

    csvfile_writer = csv.writer(csvfile)
    csvfile_writer.writerow(["failures", "skipped", "tests", "timestamp"])

for testsuite in xml.findall("testsuite"):

    if testsuite:

        with open(get_file_path('.csv'), 'a', newline='\n') as f_object:
            failures = testsuite.get('failures')
            skipped = testsuite.get('skipped')
            tests = testsuite.get('tests')
            timestamp = testsuite.get('timestamp')
            csv_line = [failures, skipped, tests, timestamp]
            # Pass the CSV  file object to the writer() function
            writer_object = writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow(csv_line)
            # Close the file object
            f_object.close()


