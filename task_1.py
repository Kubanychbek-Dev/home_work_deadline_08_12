class Teacher:
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, exp):
        self.__experience = exp

    #methods
    def get_teacher_data(self):
        return (f"{self.__name}, образование {self.__education}, "
                f"опыт работы {self.__experience} года")

    def add_mark(self, student, grade):
        return f"{self.__name} поставил оценку {grade} студенту {student}"

    def remove_mark(self, student, grade):
        return f"{self.__name} удалил оценку {grade} студенту {student}"

    def give_a_consultation(self, classname):
        return f"{self.__name} провел консультацию в классе {classname}"


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title


dis = DisciplineTeacher("Эйбел Херциг", "Стэнфордский университет", 4,
                        "Python", "Директор вышки")

dis.set_experience(8)
print(f"Имя: {dis.get_name()}")
print(f"Образование: {dis.get_education()}")
print(f"Опыт работы: {dis.get_experience()} года")
print()

print(f"{dis.get_teacher_data()}.\nПредмет {dis.get_discipline()},"
      f" должность {dis.get_job_title()}")
print()
print(f"{dis.add_mark("Лукас", 5)}. Предмет: {dis.get_discipline()}")
print()
print(f"{dis.remove_mark("John", 3)}. Предмет: {dis.get_discipline()}")
print()
print(f"{dis.give_a_consultation("KC-15")}. По предмету {dis.get_discipline()}"
      f" как {dis.get_job_title()}")