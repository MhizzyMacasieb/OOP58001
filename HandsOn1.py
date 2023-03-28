class Person:
    def __init__(self, std1, std2, std3, pre, mid, fin):
        self.std1 = std1
        self.std2 = std2
        self.std3 = std3
        self.pre = pre
        self.mid = mid
        self.fin = fin


Student1 = {"name": "Student 1",
            "Prelim": [82],
            "Midterm": [92],
            "Final": [98.80]
            }

Student2 = {"name": "Student 2",
            "Prelim": [86],
            "Midterm": [88],
            "Final": [88.60]
            }

Student3 = {"name": "Student 3",
            "Prelim": [92],
            "Midterm": [94],
            "Final": [80]
            }


def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)


def calculate_total_average(students):
    Prelim = get_average(students["Prelim"])
    Midterm = get_average(students["Midterm"])
    Final = get_average(students["Final"])
    return (0.3 * Prelim + 0.3 * Midterm + 0.4 * Final)


students = [Student1, Student2, Student3]

for i in students:
    print(i["name"])
    print("_______________________")
    print("Prelim Marks of %s is : %s " % (i["name"],
                                           calculate_total_average(i)))

for i in students:
    print(i["name"])
    print("_______________________")
    print("Midterm Marks of %s is : %s " % (i["name"],
                                            calculate_total_average(i)))

for i in students:
    print(i["name"])
    print("_______________________")
    print("Final Marks of %s is : %s " % (i["name"],
                                          calculate_total_average(i)))