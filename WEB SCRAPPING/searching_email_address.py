import requests

class Search:

    def __init__(self):
        self.url = None
        self.response = None
        self.mail_beginning = None

    def get_url(self):
        self.url = input("Enter URL: ")

    def get_response(self):
        self.response = requests.get(self.url)

    def locate_email(self):
        self.mail_beginning = self.response.text.find('mailto')

    def output(self):
        print(self.mail_beginning)
        print(self.response.text[(self.mail_beginning + 7):(self.mail_beginning + 25)])

    def run(self):
        self.get_url()
        self.get_response()
        self.locate_email()
        self.output()

if __name__ == '__main__':
    extract = Search()
    extract.run()

