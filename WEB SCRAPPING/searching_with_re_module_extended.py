import re

class Search:

    def __init__(self):
        self.text =  None
        self.search_word = None
        
    def input_text(self):
        self.text = input("Enter Text: ")
    
    def input_search_word(self):
        self.search_word = input("Enter Search Word: ")
    
    def locate_search_word(self):
        match = re.search(self.search_word, self.text)
        if match:
            print("Word found at position:", match.span())
        else:
            print("Word not found")
    
    def output(self):
        match = re.search(self.search_word, self.text)
        if match:
            print("Matched word:", match.group())
        else:
            print("No match found")
    
    def run(self):
        self.input_text()
        self.input_search_word()
        self.locate_search_word()
        self.output()

if __name__ == '__main__':
    extract = Search()
    extract.run()
    

# Sample Text: irrelevant text I recommend irrelevant text
# Sample Search Word: recommend