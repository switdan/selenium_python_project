import csv
import random

from faker import Faker

class RegistrationDataGenerator:
    def __init__(self):
        self.gender = random.choice(["M", "F"])
        self.__fake = Faker("pl_PL")
        if self.gender == "M":
            self.first_name = self.__fake.first_name_male()
            self.last_name = self.__fake.last_name_male()
        elif self.gender == "F":
            self.first_name = self.__fake.first_name_female()
            self.last_name = self.__fake.last_name_female()
        self.email = self.__fake.email()
        self.password = self.__fake.password()
        self.day = int(self.__fake.day_of_month())
        self.month = int(self.__fake.month())
        self.year = int(self.__fake.date_of_birth().year)
        self.password_max_4 = self.__fake.password()[:4]

def get_csv_data(filename):
    rows = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        next(reader, None)

        for row in reader:
            rows.append(row)
        return rows

def get_emails_from_csv(filename):
    emails = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            emails.append(row["Email"].strip())

    return emails