class Student:
    def __init__(
            self,
            lessons,
            name,
            group,
            age:int=0,
            gender:str='middle',
            course:int=1,
    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course
        self.courses = []
        self.group=group
        self.lessons=lessons

    # Метод 1: вывод информации о студенте
    def info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Пол: {self.gender}")
        print(f"Курс: {self.course}")
        print(f"Группа: {self.group}")
        print(f"Предметы: {', '.join(self.lessons) if self.lessons else 'нет'}")

    # Метод 2: изменение группы
    def change_group(self, new_group:int=None):
        if new_group is not None:
            self.group=new_group
            print('Group change success')

    # Метод 3: повышение среднего балла
    def add_lesson(self, lesson):
        if lesson not in self.lessons:
            self.lessons.append(lesson)
            print( f"Предмет '{lesson}' добавлен.")
        else: print( f"Предмет '{lesson}' уже есть в списке.")


student_1=Student(name='Mari',lessons=['liturature','economics'],group=93843,age=20, course=3,gender='female')
student_1.info()
print(student_1.group)
student_1.age=21
student_1.change_group(new_group=104954)
student_1.add_lesson('French')
student_1.info()
