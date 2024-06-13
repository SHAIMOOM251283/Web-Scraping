import requests
import re

class Search:

    def __init__(self):
        self.url = None
        self.response = None
        self.page_content = None
        self.pattern = None
        self.matches = None
        self.all_at_rate = []

    def get_url(self):
        self.url = input("Enter URL: ")

    def fetch_content_of_URL(self):
        self.response = requests.get(self.url)
        self.page_content = self.response.text

    def delineate_the_regular_expression(self):
        self.pattern = r'.{0,7}@.{0,10}'

    def find_all_matches(self):
        self.matches = re.findall(self.pattern, self.page_content)

    def store_and_print(self):
        for match in self.matches:
            self.all_at_rate.append(match)
            print(match)

    def run(self):
        self.get_url()
        self.fetch_content_of_URL()
        self.delineate_the_regular_expression()
        self.find_all_matches()
        self.store_and_print()

if __name__ == '__main__':
    extract = Search()
    extract.run()