
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

    def printMe(self):
        print(self.countOfStudents)


class Offline(University):
    def __init__(self):
        super.__init__()
        with open("offline_university.json", "r") as read_file:
            data = json.load(read_file)
            self.costOfPlace = data['costOfPlace']
            self.securitySalary = data['securitySalary']
            self.cloakroomSalary = data['cloakroomSalary']
            self.updateProjectros = data['updateProjectros']
            self.chancelleryCost = data['chancelleryCost']
            self.paperCost = data['paperCost']


class Online(University):
    def __init__(self):
        super.__init__()
        with open("online_university.json", "r") as read_file:
            data = json.load(read_file)
            self.elearningHost = data['elearningHost']
            self.zoomAccounts = data['zoomAccounts']
            self.cloudRent = data['cloudRent']

