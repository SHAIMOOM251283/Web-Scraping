import requests
import re

class Search:

    def __init__(self):
        self.url = None
        self.search = None
        self.response = None
        self.page_content = None
        self.pattern = None
        self.matches = None
        self.all_at_rate = []
        self.prefix_range = None
        self.suffix_range = None

    def get_url(self):
        self.url = input("Enter URL: ")
    
    def get_search_item(self):
        self.search = input("Enter Search Element: ")
    
    def get_prefix_range(self):
        self.prefix_range = input("Enter prefix range (e.g., 0,7): ")

    def get_suffix_range(self):
        self.suffix_range = input("Enter suffix range (e.g., 0,10): ")

    def fetch_content_of_URL(self):
        self.response = requests.get(self.url)
        self.page_content = self.response.text

    def delineate_the_regular_expression(self):
        search_escaped = re.escape(self.search)
        prefix_range = self.prefix_range
        suffix_range = self.suffix_range
        self.pattern = rf'.{{{prefix_range}}}{search_escaped}.{{{suffix_range}}}'

    def find_all_matches(self):
        self.matches = re.findall(self.pattern, self.page_content)
        if not self.matches:
            raise ValueError("Searched element not found")

    def store_and_print(self):
        print("\n---MATCHES---")
        try:
            self.find_all_matches()
            for match in self.matches:
                self.all_at_rate.append(match)
                print(match)
        except ValueError as e:
            print(e)

    def run(self):
        self.get_url()
        self.get_search_item()
        self.get_prefix_range()
        self.get_suffix_range()
        self.fetch_content_of_URL()
        self.delineate_the_regular_expression()
        self.store_and_print()

if __name__ == '__main__':
    extract = Search()
    extract.run()
