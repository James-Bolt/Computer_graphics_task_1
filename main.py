
from classes import *


def FindCountOfLectors(countOfSubjects):
    return countOfSubjects / 3 + int(bool(countOfSubjects % 3))


def CalculateSUMZPLectors(countOfLectors, salaryPerHour):
    return (countOfLectors * 0.8 * 80 + countOfLectors * 0.2 * 40) * salaryPerHour * 12  # 80% работников работают на полную ставку, 20% на полвоину


def GeneralSqare(countOfStudents, countOfLectors):
    return 4 * (countOfStudents + countOfLectors) * 1.05  # на каждого человека нужно 4 кв.м и +5% на тех. помещения


def RentCost(sqare,rentCost):
    return sqare * rentCost


def CommunalPayment(rentCost):
    return rentCost * 0.1


def CountOfCleaners(sqare):
    return sqare/500 + int(bool(sqare % 500))


def InventoryCost(countOfStudents):
    inventory = (countOfStudents/2 + 4) * 3400 + (countOfStudents + 10) * 2000  # на двух студентов 1 парта (стоимость 3400) + стулья(2000)
    computers = (countOfStudents/2 + 2) * 60000                                 # на двух студентов 1 компьютер + 2 компьютера на кафедре
                                                                                # 4 стола на всех преподавателей    10 стульев на всех преподавателей
    return inventory + computers


def CostOfAntiseptic(countOfStudents,countOfLectors):
   return ((countOfLectors + countOfLectors) * 6 * 39 * 4)/1000 * 400 # вычисляем стоимость в литрах 6 дней в неделю, 39 недель, 4мл на использование
                                                                      # стоимость литра антисептика 400 руб.


def CloudRentCost(cloudRent):
    return 512 * 300 * 12 * cloudRent  # 512 лекционных часов в год , 300мб средяя лекция, 12 месяцев, на стоимость одного гб на облаке


if __name__ == '__main__':
    Online_university = Online()
    Offline_university = Offline()

    # Стоимость обучения онлайн
    countOfLectors = FindCountOfLectors(Online_university.ourEducationPlan)
    sUMZPLectors = CalculateSUMZPLectors(countOfLectors)
    sqare = GeneralSqare(Online_university.countOfStudents, countOfLectors)
    clouds = CloudRentCost(Online_university.cloudRent)
    sumOnline = countOfLectors + sUMZPLectors + sqare + clouds + Online_university.internetCost




