import requests

class Search:

    def __init__(self):
        self.url = None
        self.response = None
        self.page_content = None
        self.all_at_rate = []
        self.start = 0
        self.at_beginning = None
        self.start_pos = None
        self.end_pos = None
        self.match = None

    def get_url(self):
        self.url = input("Enter URL: ")

    def fetch_content_of_URL(self):
        self.response = requests.get(self.url)
        self.page_content = self.response.text

    def find_all_occurrences_of_at_rate(self):
        while True:
            self.at_beginning = self.page_content.find('@', self.start)
            
            # If no more '@' symbols are found, break the loop
            if self.at_beginning == -1:
                break
    
            # Calculate the start and end positions to extract the required substring
            self.start_pos = max(self.at_beginning - 7, 0)
            self.end_pos = min(self.at_beginning + 11, len(self.page_content))
    
            # Extract the substring and store it in the list
            self.match = self.page_content[self.start_pos:self.end_pos]
            self.all_at_rate.append(self.match)
    
            # Print the match
            print(self.match)
    
            # Update the start position to search for the next '@'
            self.start = self.at_beginning + 1
    
    def run(self):
        self.get_url()
        self.fetch_content_of_URL()
        self.find_all_occurrences_of_at_rate()

if __name__ == '__main__':
    extract = Search()
    extract.run()
