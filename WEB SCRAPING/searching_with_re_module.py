import re

print(re.search(r'recommend','irrelevant text I recommend irrelevant text').span())

print(re.search(r'recommend','irrelevant text I recommend irrelevant text').group())
