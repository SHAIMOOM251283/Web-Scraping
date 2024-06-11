import requests
from bs4 import BeautifulSoup

class SearchElements:

    def __init__(self):
        self.url = None
        self.response = None
        self.soup = None
        self.all_elements = None
    
    def get_url(self):
        self.url = input("Enter URL: ")
    
    def get_response(self):
        self.response = requests.get(self.url)
    
    def create_soup(self):
        self.soup = BeautifulSoup(self.response.text, 'lxml')
    
    def get_all_elements(self):
        self.all_elements = self.soup.find_all('a')
    
    def output_all_elements(self):
        for each in self.all_elements:
            print(each['href'])

    def run(self):
        self.get_url()
        self.get_response()
        self.create_soup()
        self.get_all_elements()
        self.output_all_elements()

if __name__ == '__main__':
    search = SearchElements()
    search.run()