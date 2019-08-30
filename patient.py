class Patient:

    def __init__(self, social, birth, insurance, first, last):
        self.__social_security_number = social
        self.__date_of_birth = birth
        self.__insurance_num = insurance
        self.__first_name = first
        self.__last_name = last

    @property
    def full_name(self):
        return self.__first_name + " " + self.__last_name

    # @property
    # def social
    @property
    def social_security_number(self):
        try:
            return self.__social_security_number
        except AttributeError:
            print("You cannot access this silly")


    @property
    def social_security_number(self):
        return self.__social_security_number

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def insurance_num(self):
        return self.__insurance_num

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti"
)

# This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# Neither should this
# cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print("ssn = ", cashew.social_security_number)   # "097-23-1003"
print("date of birth = ", cashew.date_of_birth)
print("insurance num = ", cashew.insurance_num)
print("full name = ", cashew.full_name)   # "Daniela Agnoletti"
cashew.address = "500 Infinity Way"
print("address = ", cashew.address)

# These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# But this should output the full name