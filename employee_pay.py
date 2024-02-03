import csv

#read the file 
employees = open('employee_data.csv', 'r')
employee_file = csv.reader(employees)

#skip the header
next(employee_file)

for record in employee_file:
    name = record[1]
    salary = float(record[3])
    bonus_percentage = float(record[7])
    bonus = salary * bonus_percentage
    pay = float(bonus + salary)

    print(f"Name: {name}")
    print(f"Salary: $ {salary:,.2f}")
    print(f"Bonus:  $  {bonus:,.2f}")
    print(f"Pay:    $ {pay:,.2f}")
    print()
    print()
    input()


