import re, requests
import pandas as pd

class Search:

    def __init__(self):
        self.url = None
        self.response = None
        self.allmatches = None
        self.alladdresses = []
        self.alladdpd = None

    def get_url(self):
        self.url = input("Enter URL: ")

    def get_response(self):
        self.response = requests.get(self.url)

    def locate_matches(self):
        self.allmatches = re.finditer(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', self.response.text)

    def print_all_addresses(self):
        for match in self.allmatches:
            self.alladdresses.append(match[0])
            print(self.alladdresses)

    def add_pd(self):
        self.alladdpd = pd.DataFrame(self.alladdresses)
        print(self.alladdpd)

    def create_csv(self):
        self.alladdpd = self.alladdpd.sort_values(0,ascending=False)
        self.alladdpd.to_csv('extracted_email.csv')
    
    def run(self):
        self.get_url()
        self.get_response()
        self.locate_matches()
        self.print_all_addresses()
        self.add_pd()
        self.create_csv()

if __name__ == '__main__':
    extract = Search()
    extract.run()



