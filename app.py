# -*- coding: utf-8 -*-
import codecs, re, csv, os, datetime
from collections import Counter


def datatake(filename):
    regi = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    with codecs.open(filename, 'r', 'utf-8') as f:
        log = f.read()
        ipl = re.findall(regi, log)
    return Counter(ipl)

def wcsv(count):
    try:
        with open('outfile.csv', 'a') as csvf:
            csvf.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M\n'))
            writer = csv.writer(csvf)
            header = ['ip', 'frequency']
            writer.writerow(header)
            for item in count:
                writer.writerow( (item, count[item]) )
        print('\nDone!\n\nThe sorted file(outfile.csv) is located in the directory from which you ran the script.\n')
    except PermissionError:
        print('File outfile.csv is in use! Sorry...')

if __name__ == '__main__':
    while True:
        file = input('Enter the full path to the log file (including its full name)\n:> ' )
        if not os.path.exists(file):
            print('The path to the file or its name is incorrect!\nTry again...\n')
        else:
            wcsv(datatake(file))
            break
