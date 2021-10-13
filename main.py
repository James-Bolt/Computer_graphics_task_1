
from classes import *


def FindCountOfLectors(countOfSubjects):
    return countOfSubjects / 3 + int(bool(countOfSubjects % 3))

def CalculateSUMZPLectors(countOfLectors, salaryPerHour):
    return (countOfLectors * 0.8 * 80 + countOfLectors * 0.2 * 40) * salaryPerHour * 12  # 80% работников работают на полную ставку, 20% на полвоину

def RentCost(countOfStudents, rentCost, countOfLectors):
    return rentCost * 4 * (countOfStudents + countOfLectors) * 1.05  # на каждого человека нужно 4 кв.м и +5% на тех. помещения


if __name__ == '__main__':
    Online_university = Online()
    Offline_university = Offline()
    FindCountOfLectors(Online_university.ourEducationPlan)



