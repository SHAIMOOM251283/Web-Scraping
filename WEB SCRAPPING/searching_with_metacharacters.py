import re

print(re.search('10*','My bank balance is 1').span())

print(re.search('10*','My bank balance is 1000').span())

try:
    print(re.search('10*','My bank balance is 9000').span())
except AttributeError:
    pass

print(re.search('10*','My bank balance is 1000000').span())

print(re.search('Clarke?','Please refer questions to Mr.Clark').span())

try:
    print(re.search('99+12=111','Example addition: 99+12=111').span())
except AttributeError:
    pass

print(re.search('99+12=111','Incorrect fact: 999912=111').span())

print(re.search('99\+12=111','Example addition: 99+12=111').span())

print(re.search('Clarke\?','Is anyone here named Clarke?').span())

print(re.search(r'\\',r'The escape character is \\').span())

print(re.search('\d','The loneliest number is 1').span())

print(re.search('[a-z]','My Twitter is @fake; my email is abc@def.com').span())

print(re.search('[A-Z]','My Twitter is @fake; my email is abc@def.com').span())

print(re.search('Manchac[a|k]','Lets drive on Manchaca.').span())