import datetime
from random import randrange


class GenerateRandom:

    def generate_text(self, length: int):
        text = ""
        print(length)
        while length - 1 >= 0:
            text += chr(randrange(97, 122))
            length -= 1
        return text

    def generate_phone(self):
        phone = ""
        for t in range(0, 10):
            phone += str(randrange(2, 10))

        return phone

    def generate_date_of_birthday(self):
        day = randrange(1, 28)
        month = randrange(1, 12)
        year = randrange(1940, int(datetime.date.today().year - 18))
        return str(day).zfill(2) + "/" + str(month).zfill(2) + "/" + str(year)

    def generate_number(self, length):
        number = ""
        while length - 1 >= 0:
            number += str(randrange(1, 9))  # Es igual number = number + valor
            length -= 1

        return number

    def generate_rfc(self, name: str, last_name: str, second_last_name: str, year, month, day):
        last_name = last_name[0:2]
        second_last_name = second_last_name[0:1]
        name = name[0:1]
        year = str(year)[2:]
        month = str(month).zfill(2)
        day = str(day).zfill(2)
        rfc = last_name + second_last_name + name + year + month + day + str(self.generate_text(2)) + str(self.generate_number(1))
        return rfc.upper()


# gr = GenerateRandom()
#
# date_of_birthday=gr.generate_date_of_birthday()
# day=date_of_birthday[0:2]
# month=date_of_birthday[3:5]
# year=date_of_birthday[6:10]
# # year=2000
#
# rfc=gr.generate_rfc("Arturo", "Hernandez", "Perez", year, month, day)
#
# print(rfc)
# #
# print(day)
# print(month)
# print(year)
# print(date_of_birthday)