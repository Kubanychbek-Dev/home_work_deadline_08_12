class Teacher:
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_name(self):
        return f"Teacher - {self.__name}"

    def get_education(self):
        return f"Education - {self.__education}"

    def get_experience(self):
        return f"Experience - {self.__experience} year(s)"

    def set_experience(self, experience):
        self.__experience = experience

    #Methods

    def get_teacher_data(self):
        return f"{self.__name}, образование {self.__education}, опыт работы {self.__experience} года."

    def add_mark(self, name, x):
        return f"{self.__name} поставил оценку {x} студенту {name}"

    def remove_mark(self, name, x):
        return f"{self.__name} удалил оценку {x} студенту {name}"

    def give_a_consultation(self, cls):
        return f"{self.__name} провел консультацию в классе {cls}"


teacher = Teacher("Abel Herzig", "California University", 8)
print(teacher.get_name())
print(teacher.get_education())
print(teacher.get_experience())
print()

print(teacher.get_teacher_data())
print(teacher.add_mark("Lucas", 5))
print(teacher.remove_mark("Lucas", 2))
print(teacher.give_a_consultation("KC - 15"))
