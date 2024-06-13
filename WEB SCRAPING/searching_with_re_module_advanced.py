import re

print(re.search('rec+om+end', 'irrelevant text I recommend irrelevant text').span())

print(re.search('rec+om+end','irrelevant text I recomend irrelevant text').span())

print(re.search('rec+om+end','irrelevant text I reccommend irrelevant text').span())

try:
    print(re.search('rec+om+end','irrelevant text I reommend irrelevant text').span())
except AttributeError:
    pass

try:
    print(re.search('rec+om+end','irrelevant text I recomment irrelevant text').span())
except AttributeError:
    pass