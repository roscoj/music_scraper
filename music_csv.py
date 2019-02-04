import csv

### CREATE DATA ###

def create_csv(file_name, dict_rows):
    csv_file = open(file_name, 'w')
    with csv_file:
        headers = ['first_name', 'last_name']
        writer = csv.DictWriter(csv_file, fieldnames=headers)

        writer.writeheader()
        for row in dict_rows:
            writer.writerow(row)

dict1 = [{'first_name': 'Ross', 'last_name': 'Jarrett'}, {'first_name': 'Jake', 'last_name': 'Smith'}]
dict2 = [{'first_name': 'Ross', 'last_name': 'Jarrett'}, {'first_name': 'Jake', 'last_name': 'Smith'}, {'first_name': 'Harry', 'last_name': 'Carter'}]

create_csv('old.csv', dict1)
create_csv('new.csv', dict2)



def unique_entries(file_1, file_2):
    with open(file_1, 'r') as file_1, open(file_2, 'r') as file_2:
        f1 = file_1.readlines()
        f2 = file_2.readlines()
    
    with open('unique.csv', 'w') as unique:
        for line in file_2:
            if line not in file_1:
                unique.write(line)



unique_entries('new.csv', 'old.csv')


