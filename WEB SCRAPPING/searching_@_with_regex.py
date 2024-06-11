import requests

class Search:

    def __init__(self):
        self.url = None
        self.response = None
        self.at_beginning = None

    def get_url(self):
        self.url = input("Enter URL: ")

    def get_response(self):
        self.response = requests.get(self.url)

    def search_element(self):
        self.at_beginning = self.response.text.find('@')

    def output(self):
        print(self.at_beginning)
        print(self.response.text[(self.at_beginning - 7):(self.at_beginning + 25)])
    
    def run(self):
        self.get_url()
        self.get_response()
        self.search_element()
        self.output()

if __name__ == '__main__':
    element = Search()
    element.run()

