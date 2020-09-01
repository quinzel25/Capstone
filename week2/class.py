#needs this in order to work
from dataclasses import dataclass

#this makes a little more sense with my brain, and it's less typing when it comes to creating new objects
@dataclass
class Student:
    name: str
    college_id: int
    gpa: float


# *ORIGINAL VERSION*
# class Student:
#     def __init__(self, name, college_id):
#         self.name = name
#         self.college_id = college_id

def main():
    #sample data
    alice = Student('Alice', 'aa123aa', 3.7)
    bob = Student('Bob', 'bb123bb', 2.8)
    frankie = Student('Frankie', 'cc123c', 3.9)
    erik = Student('Erik', 'dd123dd', 3.1)

    # printing out each data set in a neat format
    print(f'{alice.name} has a GPA of {alice.gpa} and their college ID is {alice.college_id}')
    print(f'{bob.name} has a GPA of {bob.gpa} and their college ID is {bob.college_id}')
    print(f'{frankie.name} has a GPA of {frankie.gpa} and their college ID is {frankie.college_id}')
    print(f'{erik.name} has a GPA of {erik.gpa} and their college ID is {erik.college_id}')


main()