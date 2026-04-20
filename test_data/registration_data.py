import random

from faker import Faker

class RegistrationDataGenerator:
    def __init__(self):
        self.GENDER = random.choice(["M", "F"])
        self.__fake = Faker("pl_PL")
        if self.GENDER == "M":
            self.FIRST_NAME = self.__fake.first_name_male()
            self.LAST_NAME = self.__fake.last_name_male()
        elif self.GENDER == "F":
            self.FIRST_NAME = self.__fake.first_name_female()
            self.LAST_NAME = self.__fake.last_name_female()
        self.EMAIL = self.__fake.email()
        self.PASSWORD = self.__fake.password()
        self.DAY = int(self.__fake.day_of_month())
        self.MONTH = int(self.__fake.month())
        self.YEAR = int(self.__fake.date_of_birth().year)