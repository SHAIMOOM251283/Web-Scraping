import re

class Search:

    def __init__(self):
        self.text = None
        self.email_pattern = None
        self.result = None

    def text_for_search(self):
        self.text = 'My Twitter is @fake; my email is abc@def.com'

    def pattern(self):
        self.email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    def extract(self):
        self.result = re.search(self.email_pattern, self.text)
        if self.result:
            print(self.result.span())
            print(self.result.group())
        else:
            print("No match found")

    def search(self):
        print(re.search('[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+',\
                        'My Twitter is @fake; my email is abc@def.com').span())
    
    def run(self):
        self.text_for_search()
        self.pattern()
        self.extract()
        self.search()

if __name__ == '__main__':
    extract = Search()
    extract.run()