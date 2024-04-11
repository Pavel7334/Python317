import json
import os  # Импортируем модуль os для проверки существования файла


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        marks_str = ", ".join(map(str, self.marks))
        return f"Студент: {self.name} => {marks_str}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def del_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, mark):
        self.marks[index] = mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def get_file_name(self):
        return self.name.lower() + ".json"

    def dump_to_json(self):
        data = {"name": self.name, "marks": self.marks}
        with open(self.get_file_name(), "w") as f:
            json.dump(data, f, indent=2)

    def load_from_file(self):
        file_name = self.get_file_name()
        if os.path.exists(file_name):  # Проверяем существование файла
            with open(file_name, "r") as f:
                return json.load(f)
        else:
            return None


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        student_info = '\n'.join(map(str, self.students))
        return f"Группа: {self.group}\n{student_info}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(gr1, gr2, index):
        gr2.add_student(gr1.remove_student(index))

    def get_file_name(self):
        return self.group.lower().replace(" ", "-") + ".json"

    def dump_to_json(self):
        file_name = 'гк-web.json'
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                data = json.load(f)
                data[self.group] = [{'name': student.name, 'marks': student.marks} for student in self.students]
            with open(file_name, 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            group_data = {self.group: [{'name': student.name, 'marks': student.marks} for student in self.students]}
            with open(file_name, 'w') as f:
                json.dump(group_data, f, indent=2, ensure_ascii=False)

    def load_from_file(self):
        file_name = self.get_file_name()
        if os.path.exists(file_name):  # Проверяем существование файла
            with open(file_name, "r") as f:
                return json.load(f)
        else:
            return None


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])

sts1 = Group([st1, st2], "ГК Web")
sts1.add_student(st3)
sts1.remove_student(1)
print(sts1)
print()
sts2 = Group([st2], "ГК Python")
Group.change_group(sts1, sts2, 0)
print(sts1)
print()
print(sts2)
print()
sts2.dump_to_json()
sts2.load_from_file()

# Создаем новую группу "ГК JavaScript" только с одним студентом "Birukov"
sts3 = Group([st3], "ГК JavaScript")
sts3.dump_to_json()
sts3.load_from_file()
