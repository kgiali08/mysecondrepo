import csv
# read the file 
customers = open('customers.csv', 'r')
customer_file = csv.reader(customers)
outfile = open('customer_country.csv', 'w')

outfile.write('Full Name,Country\n')

#skip the header 
next(customer_file)

#print contents
counter = 0 
for record in customer_file:
    outfile.write(f"{record[1]} {record[2]}, {record[4]}\n")
    counter += 1

outfile.close()

print(f"Total number of customers: {counter}")
