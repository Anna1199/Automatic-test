class Users:
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name


    def sayName(self):
        print('my name is ', self.first_name)
    def saySurename(self):
        print('my surename is ', self.last_name)
    def sayFullName(self):
        print('I am ', self.first_name, self.last_name)