class Customer :
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_phone_number(self):
        return self.phone_number