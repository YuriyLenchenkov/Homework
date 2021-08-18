#!/usr/bin/env python3

import pickle

class Employee:
    def __init__(self, first_name):
        self.first_name = first_name

pickle_path = "/tmp/pickle.dump"
with open(pickle_path, "rb") as f:
    get = pickle.load(f)

print(Employee(get).first_name)

