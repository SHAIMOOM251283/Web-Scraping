import re

print(re.search('school.*\.pdf$','schoolforgottenname.pdf').span())

print(re.search('school.*\.pdf$','schoolforgottenname.pdf').span())

print(re.search('school.*\.pdf$','school.pdf').span())

print(re.search('school.*\.pdf$','schoolothername.pdf').span())

try:
    print(re.search('school.*\.pdf$','othername.pdf').span())
except AttributeError:
    pass

try:
    print(re.search('school.*\.pdf$','schoolothernamepdf').span())
except AttributeError:
    pass

try:
    print(re.search('school.*\.pdf$','schoolforgottenname.pdf.exe').span)
except AttributeError:
    pass