#!/usr/bin/env python3
import csv
from collections import Counter
shell = []
with open('/etc/passwd') as csv_file:
    csv_passwd = csv.reader(csv_file, delimiter=':')
    for row in csv_passwd:
        shell.append(row[-1])
count_shell = Counter(shell)
print(str(count_shell).replace('Counter({','').replace(':',' -').replace("'","").replace(',',';').replace('})',''))

from pwd import getpwnam
groups = {}
with open('/etc/group') as csv_file:
    csv_users = csv.reader(csv_file, delimiter=':')
    for row in csv_users:
        groups.update({row[0]:row[-1]})
filter = {key: value for key, value in groups.items() if value != ''}
for key, value in filter.items():
    tmp_val = value.split(',')
    tmp_list = []
    for i in tmp_val:
        tmp_list.append(getpwnam(i).pw_uid)
        filter.update({key: str(tmp_list).replace('[','').replace(']','')})

print(str(filter).replace('{','').replace("'}",'').replace("'",'').replace(': ',':'))