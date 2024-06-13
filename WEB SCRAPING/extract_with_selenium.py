from selenium import webdriver
from selenium.webdriver.common.by import By

class ExtractwithSelenium:

    def __init__(self):
        self.url = None
        self.driver = None
        self.phone_element = None
        self.phone_number = None
        self.email_element = None
        self.email_address = None
        self.address_element = None
        self.address = None
    
    def get_url(self):
        self.url = input("Enter URL: ")

    def initialize_webdriver(self):
        self.driver = webdriver.Firefox()

    def open_webpage_containing_HTML_snippet(self):
        self.driver.get(self.url)

    def locate_telephone_number_element_and_extract_text(self):
        self.phone_element = self.driver.find_element(By.CSS_SELECTOR, "a[href^='tel:'] .hero-contacts__item-content")
        self.phone_number = self.phone_element.text.strip()

    def locate_email_element_and_extract_text(self):
        self.email_element = self.driver.find_element(By.CSS_SELECTOR, "a[href^='mailto:'] .hero-contacts__item-content")
        self.email_address = self.email_element.text.strip()

    def locate_address_element_and_extract_text(self):
        self.address_element = self.driver.find_element(By.CSS_SELECTOR, "a[href*='maps'] .hero-contacts__item-content")
        self.address = self.address_element.get_attribute('innerHTML').strip().replace('<br>', ' ').replace('\n', ' ').strip()

    def print_extracted_contact_details(self):
        print("Telephone Number:", self.phone_number)
        print("Email Address:", self.email_address)
        print("Address:", self.address)

    def close_browser(self):
        self.driver.quit()
    
    def run(self):
        self.get_url()
        self.initialize_webdriver()
        self.open_webpage_containing_HTML_snippet()
        self.locate_telephone_number_element_and_extract_text()
        self.locate_email_element_and_extract_text()
        self.locate_address_element_and_extract_text()
        self.print_extracted_contact_details()
        self.close_browser()

if __name__ == '__main__':
    extract = ExtractwithSelenium()
    extract.run()

