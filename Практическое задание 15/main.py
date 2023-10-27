class Student:
    """Студент"""
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Курсы в процессе обучения:{courses_in_progress_string}\n' \
              f'Завершенные курсы:{finished_courses_string}\n'
        return res

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        """Оценка лектору от студентов"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    """Наставник"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    """Лектор"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n'\
              f'Среднее значение оценки: {self.avg()}\n '
        return res

    def avg(self):
        if not self.grades:
            return 0
        fgrade = 0
        for i in self.grades.values():
            a = i.copy()
            while len(a) != 0:
                j = a.pop()
                fgrade += int(j)
        return fgrade / len(i)

class Reviewer(Mentor):
    """Проверяющие"""
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        """Проставление оценки студенту от проверяющего"""
        if student is Student and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return 'Ошибка'


best_lecturer = Lecturer('Дим', 'Димыч')
best_lecturer.courses_attached += ['Python']

student = Student('Петр', 'Петров', 'Male')
student.courses_in_progress += ['Python']
student.finished_courses += ['Основы Python']

cool_rewiewer = Reviewer('Some', 'Buddy')
cool_rewiewer.courses_attached += ['Python']
cool_rewiewer.courses_attached += ['Java']

student.rate_hw(best_lecturer, 'Python', 10)
student.rate_hw(best_lecturer, 'Python', 4)
print(best_lecturer)

cool_rewiewer.rate_hw(student, 'Python', 8)
cool_rewiewer.rate_hw(student, 'Java', 5)


print(f'Студент:\n{student}')
print(f'Перечень лекторов:\n{best_lecturer}')