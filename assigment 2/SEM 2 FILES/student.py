class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_total_marks(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return (self.calculate_total_marks() / (len(self.marks) * 100)) * 100

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {self.calculate_total_marks()}")
        print(f"Percentage: {self.calculate_percentage()}%")





s = Student("jigyasu", "39", [85, 90, 95])
s.display_details()
