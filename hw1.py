#!/usr/bin/env python3
from tabulate import tabulate

py_types = [['||||', 'bool', 'str', 'int'], \
            ['bool', '||||', 'true\nor false', '0 or 1'], \
            ['str', 'true\nor false', '||||', 'numbers'], \
           ['int', '0 or 1', 'numbers', '||||']]

print(tabulate(py_types, headers='firstrow', tablefmt='grid'))
