# What we've talked about is procedural / functional programming
# Another approach to programming is OOP (object oriented programming)

class Worker:
    salary = 0
    name = 0
    # fields are variables that belong to an object
    # self.number_of_heads = 1
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

new_worker = Worker("John",200)

print(new_worker.salary)

class Boss(Worker):
    bonus = 0

    def __init__(self, name, salary, bonus):
        Worker.__init__(self,name,salary)
        self.bonus = bonus

new_boss = Boss("Terry", 300, 100)

print("The boss' bonus is", new_boss.bonus)