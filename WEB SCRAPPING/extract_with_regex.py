import re
import requests

class ExtractwithRegex:

    def __init__(self):
        self.url = None
        self.response = None
        self.email_pattern = None
        self.emails = None
        self.phone_number_pattern = None
        self.phone_numbers = None
        self.address_pattern = None
        self.addresses = None

    def get_url(self):
        self.url = input("Enter URL: ")
    
    def get_response(self):
        self.response = requests.get(self.url)
    
    def find_email(self):
        self.email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        self.emails = re.finditer(self.email_pattern, self.response.text)

    def find_phone_numbers(self):
        self.phone_number_pattern = r'\+\d{11}'
        self.phone_numbers = re.findall(self.phone_number_pattern, self.response.text)
    
    def find_addresses(self):
        self.address_pattern = address_pattern = r'\d+\s[A-Za-z0-9\s,.#-]+(?:\s|<br>)+Suite(?:\s|<br>)+[A-Za-z0-9-]+(?:\s|<br>)+[A-Za-z\s]+,\s[A-Z]{2}\s\d{5}'
        self.addresses = re.findall(self.address_pattern, self.response.text, re.DOTALL)

    def print_emails(self):
        print("Emails:")
        for email in self.emails:
            print(email.group())

    def print_phone_numbers(self):
        print("\nPhone Numbers:")
        for phone_number in self.phone_numbers:
            print(phone_number)

    def print_addresses(self):
        print("\nAddresses:")
        for address in self.addresses:
            address_cleaned = re.sub(r'<[^>]+>', '', address).replace('\n', ' ').replace('<br>', ' ')
            print(address_cleaned)

    def run(self):
        self.get_url()
        self.get_response()
        self.find_email()
        self.find_phone_numbers()
        self.find_addresses()
        self.print_emails()
        self.print_phone_numbers()
        self.print_addresses()

if __name__ == '__main__':
    extract = ExtractwithRegex()
    extract.run()
