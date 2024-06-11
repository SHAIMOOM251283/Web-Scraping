import requests

class Search:

    def __init__(self):
        self.url = None
        self.response = None

    def get_url(self):
        self.url = input("Enter URL: ")

    def get_response(self):
        self.response = requests.get(self.url)

    def output(self):
        print(self.response.text[0:600])
    
    def run(self):
        self.get_url()
        self.get_response()
        self.output()

if __name__ == '__main__':
    extract = Search()
    extract.run()