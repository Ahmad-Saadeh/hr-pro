import datetime
class Employee:
    def __init__(self,name,age,salary,employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
    def get_working_years(self):
        Current_time = datetime.datetime.now()
        working_years = int(Current_time.year) - int(self.employment_year)
        return working_years
    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age) + ", Salary: " + str(self.salary) + ", Working Years: " + str(self.get_working_years())
class Manager(Employee):
    def __init__(self,name,age,salary,employment_year,bonus_percentage):
        super().__init__(name,age,salary,employment_year)
        self.bonus_percentage = bonus_percentage

    def get_working_years(self):
        Current_time = datetime.datetime.now()
        working_years = int(Current_time.year) - int(self.employment_year)
        return working_years
    def get_bonus(self):
        bonus = float(self.salary) * float(self.bonus_percentage)
        return bonus

    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age) + ", Salary: " + str(self.salary) + ", Working Years: " + str(self.get_working_years()) + ", Bonus: " + str(self.get_bonus())


def main():
    Employee_list = []
    Managers_list = []
    print("\nWelcome to HR Pro 2020")
    options = ["Show Employees","Show Managers","Add An Employee","Add A Manager","Exit"]
    while(True):
        print("Options:")
        for i in range(len(options)):
            print("    "+str(i+1)+". "+options[i])
        print("")
        Check = int(input("What would you like to do? "))
        print("")
        print("-"*20)
        if Check == 1:
            print("Employees\n")
            for emp_ob in Employee_list:
                print(emp_ob)
            print("-"*20)
        elif Check == 2:
            print("Managers\n")
            for mng_object in Managers_list:
                print(mng_object)
            print("-"*20)
        elif Check == 3:
            emp_name = input("Name: ")
            emp_age = input("Age: ")
            emp_salary = input("Salary: ")
            emp_employment_years = input("Employment Year: ")
            emp_ob = Employee(name=emp_name,age=emp_age,salary=emp_salary,employment_year=emp_employment_years)
            Employee_list.append(emp_ob)
            print("Employee added succesfully\n")
        elif Check == 4:
            mng_name = input("Name: ")
            mng_age = input("Age: ")
            mng_salary = input("Salary: ")
            mng_employment_years = input("Employment Year: ")
            mng_bonus_percentage = input("Bonus Percentage: ")
            mng_ob = Manager(name=mng_name,age=mng_age,salary=mng_salary,employment_year=mng_employment_years,bonus_percentage=mng_bonus_percentage)
            Managers_list.append(mng_ob)
            print("Manager added succesfully\n")
        elif Check == 5:
            print("GoodBye :)")
            break
if __name__ == '__main__':
	main()
