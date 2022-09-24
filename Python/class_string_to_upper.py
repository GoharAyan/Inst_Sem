class String:
    def __init__(self):
        self.word = ""

    def get_string(self):
        self.word = input("Enter string: ")

    def upper_string(self):
        print("Entered string is uppercase: ", self.word.upper())

string = String()
string.get_string()
string.upper_string()
