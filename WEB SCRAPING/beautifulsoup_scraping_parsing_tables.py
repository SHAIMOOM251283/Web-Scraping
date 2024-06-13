from bs4 import BeautifulSoup

class ScrapParse:

    def __init__(self):
        self.file = None
        self.content = None
        self.soup = None
        self.all_user_entries = None
        self.user = None
    
    def get_file(self):
        self.file = "example_file.html"

    def open_local_file(self):
        with open(self.file, 'r') as f:
            self.content = f.read()

    def parse_with_BeautifulSoup(self):
        self.soup = BeautifulSoup(self.content, 'lxml')

    def find_all_entries(self):
        self.all_user_entries = self.soup.find_all('tr', {'class': 'user-details'})

    def iterate_and_print_details(self):
        for each_user in self.all_user_entries:
            user = each_user.find_all("td")
            print("User Firstname: {}, Lastname: {}, Age: {}".format(user[0].text, user[1].text, user[2].text))

    def run(self):
        self.get_file()
        self.open_local_file()
        self.parse_with_BeautifulSoup()
        self.find_all_entries()
        self.iterate_and_print_details()

if __name__ == '__main__':
    Scraper = ScrapParse()
    Scraper.run()
