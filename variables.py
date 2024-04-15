
# Variables in Python

first_name = 'Anh'
last_name = 'Nguyen'
country = 'Quan9'
city = 'HCM'
age = 23
is_married = True
skills = [ 'Python']
person_info = {
    'firstname':'Anh', 
    'lastname':'Nguyen', 
    'country':'Quan9',
    'city':'HCM'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Anh', 'Nguyen', 'Quan9', 23, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)