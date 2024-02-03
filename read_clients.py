def main():
    #Open file
    client_file = open('clients.txt', 'r')

    client_num = 0 
    #Print Statements
    for client in client_file:
        client_num +=1
        client = client.rstrip('\n')
        print(f"{client_num}. {client}")
    
    print()
    print("Total number of clients:", num)

main()