# Patient class
class patient:
    def __init__(self, name, id, age, gender, diagnoise):
        self.name = name 
        self.id = id 
        self.age = age
        self.gender = gender
        self.diagnoise = diagnoise


    def display_info(self):
        print("\n***** Patient information *****")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Name: {self.name}")