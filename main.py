from classes.customer import Customer

def find(list_of_attend,list_of_sus):
    temp_map_of_sus_contacts = {}
    for username in list_of_sus:
        startDate, endDate =  [x.get_start_end_date_list() for x in list_of_attend if x.name_surname == username][0]
        temp_map_of_sus_contacts[username] = []
        for cust in list_of_attend:
            if(cust.name_surname == username): break; ## If user itself then break for
            if(startDate <= int(cust.start_date) <= endDate) or (startDate <= int(cust.end_date)  <= endDate):
                temp_map_of_sus_contacts[username].append(cust)
    return temp_map_of_sus_contacts

def __output_txt(list_of_contacts):
    file1 = open('output.txt', 'w') 
    file1.writelines(list_of_contacts) 
    file1.close()

def output_print(map_of_contacts):
    for contactName in map_of_contacts:
        print(f'** Customer contacts:{contactName}**')
        if(len(map_of_contacts[contactName]) == 0):
            print(f'The Customer {contactName} had no contacts') 
            continue
        for contacts in map_of_contacts[contactName]:
            print(f'Contact with {contacts.name_surname},phone {contacts.number}')

def read_file(file_name,access_mode='r'):
    file = open(file_name,access_mode)
    lines = file.read().splitlines()
    file.close()
    return lines

def main():

    listOfAttendance = []
    linesOfAttendance = read_file('attendance.txt','r')
    for line in linesOfAttendance:
        arrayOfLine = line.split(',');
        tempCust = Customer(arrayOfLine[0],arrayOfLine[1],arrayOfLine[2],arrayOfLine[3])
        listOfAttendance.append(tempCust)

    lines_of_suspicious = read_file('suspicious.txt','r')
    map_of_contacts = find(listOfAttendance,lines_of_suspicious)
    

    output_print(map_of_contacts)

main()
