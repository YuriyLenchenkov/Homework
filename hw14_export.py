#!/usr/bin/env python3

import pickle

class Employee:
    def __init__(self, first_name):
        self.first_name = first_name

#person1 = Employee("Mary")

pickle_path = "/tmp/pickle.dump"
with open(pickle_path, "wb") as f:
    pickle.dump(Employee("Mary").first_name, f)

#print(person1.first_name)

