#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:

    def __init__(self, name="Default", job="Sales"):
        self.name = name
        self.job = job

    # ==== name =====        
    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if (type(name) == str and (1 <= len(name) <= 25)):
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.") 


    # ==== job =====        
    def get_job(self):
        print("Retrieving job.")
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")   


   
    name = property(fget=get_name, fset=set_name)
    job = property(fget=get_job, fset=set_job)
