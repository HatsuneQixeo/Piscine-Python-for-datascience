from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

# student = Student(name = "Edward", surname = "agle", active=False)

# try:
#     student = Student(name = "Edward", surname = "agle", login="Eagle")
# except Exception as e:
#     print(f"{e.__class__.__name__}:", e)

# try:
#     student = Student(name = "Edward", surname = "agle", id="myid")
# except Exception as e:
#     print(f"{e.__class__.__name__}:", e)

# try:
#     Student(name = "Edward")
# except Exception as e:
#     print(f"{e.__class__.__name__}:", e)
