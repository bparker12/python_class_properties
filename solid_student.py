class Student:

    # def __init__(self):
            # self.__first_name = ""
            # self.__last_name = ""
            # self.__age = 1
            # self.__cohort_num = 1
            # self.__full_name = self.__first_name + " " + self.__last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0

    @first_name.setter
    def first_name(self, first_name):
        if type(first_name) is str:
            self.__first_name = first_name
        else:
            raise TypeError('Please provide a word for the first name')

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if type(last_name) is str:
            self.__last_name = last_name
        else:
            raise TypeError('Please provide a word for the last name')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if type(age) is int:
            self.__age = age
        else:
            raise TypeError('Please provide a number for the age')

    @property
    def cohort_num(self):
        return self.__cohort_num

    @cohort_num.setter
    def cohort_num(self, cohort_num):
        if type(cohort_num) is int:
            self.__cohort_num = cohort_num
        else:
            raise TypeError('Please provide a number for the cohort number')

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_num}"

pam = Student()
pam.first_name = "Pam"
pam.last_name = "Beasley"
pam.age = 18
pam.cohort_num = 33

print(pam)

print()
