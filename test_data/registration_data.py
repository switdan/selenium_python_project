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
        birth_date = self.__fake.date_of_birth(minimum_age=18, maximum_age=80)
        self.day = birth_date.day
        self.month = birth_date.month
        self.year = birth_date.year
        self.password_max_4 = self.__fake.password()[:4]

def get_login_data(filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            email = row["Email"].strip()
            password = row["Password"].strip()

            fullname = f"{row['FirstName'].strip()} {row['LastName'].strip()}"

            data.append((email, password, fullname))

    return data

def get_emails_from_csv(filename):
    emails = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            emails.append(row["Email"].strip())

    return emails