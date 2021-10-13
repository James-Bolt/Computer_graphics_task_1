
import json

class University(object):
    def __init__(self):
        with open("base_university.json", "r") as read_file:
            data = json.load(read_file)
            self.countOfStudents = data['countOfStudents']
            self.ourEducationPlan = data['ourEducationPlan']
            self.internetCost = data['internetCost']
            self.accountantSalary = data['accountantSalary']
            self.cost1C = data['cost1C']
            self.sysAdminSalary = data['sysAdminSalary']
            self.methodistSalary = data['methodistSalary']
            self.inflation = data['inflation']
            self.durationOfEducation = data['durationOfEducation']

class Offline(University):
    def __init__(self):
        super.__init__()
        with open("offline_university.json", "r") as read_file:
            data = json.load(read_file)
            self.

