import csv

customers = open('customers.csv','r')    #customers is the file object 

csv_file = csv.reader(customers)

#to skip the header of file
next(csv_file)

#print first name and last name
for record in csv_file:
    print(f"First Name: {record[1]} Last Name: {record[2]}")
    input()


