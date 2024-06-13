import requests
from bs4 import BeautifulSoup

class ExtractwithBeautifulsoup:

    def __init__(self):
        self.url = None
        self.response = None
        self.html_content = None
        self.soup = None
        self.telephone_number = None
        self.email = None
        self.address_a_tag = None
        self.address_text = None
    
    def get_url(self):
        self.url = input("Enter URL: ")
    
    def get_response(self):
        self.response = requests.get(self.url)
    
    def fetch_HTML_content(self):
        self.html_content = self.response.text 

    def parse_HTML(self):
        self.soup = BeautifulSoup(self.html_content, 'lxml')
    
    def extract_telephone_number(self):
        self.telephone_number = self.soup.find('a', href=lambda href: href and href.startswith('tel')).text.strip()

    def extract_email(self):
        self.email = self.soup.find('a', href=lambda href: href and href.startswith('mailto')).text.strip()

    def extract_address(self):
        self.address_a_tag = self.soup.find('a', href=lambda href: 'maps' in href)
        self.address_text = self.address_a_tag.find('span', class_='hero-contacts__item-content').get_text(strip=True)

    def output(self):
        print("Telephone Number:", self.telephone_number)
        print("Email:", self.email)
        print("Address:", self.address_text)

    def run(self):
        self.get_url()
        self.get_response()
        self.fetch_HTML_content()
        self.parse_HTML()
        self.extract_telephone_number()
        self.extract_email()
        self.extract_address()
        self.output()

if __name__ == '__main__':
    extract = ExtractwithBeautifulsoup()
    extract.run()
