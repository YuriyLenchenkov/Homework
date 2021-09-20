#!/usr/bin/env python3
import csv
import subprocess
from collections import Counter
shell = []
user = []
with open('/etc/passwd') as csv_file:
    csv_passwd = csv.reader(csv_file, delimiter=':')
    for row in csv_passwd:
        shell.append(row[-1])
        user.append(row[0])
count_shell = Counter(shell)
print(str(count_shell).replace('Counter({', '').replace(':', ' -').replace("'", "").replace(',', ';').replace('})', ''))
print("\n")

for i in user:

    command = "id -G " + i
    a = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    print(i+":", str(a.communicate()).replace("(b","").replace("'","").replace("\\n, None)","").replace(" ",", ")+"; ",\
        end="")
