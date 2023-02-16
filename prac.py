#class student:
 #   def __init__(self, name, major, gpa, is_on_probation):
#        self.name = name
#       self.major = major
#        self.gpa = gpa
#        self.is_on_probation = is_on_probation

import numpy as np
a=np.full((5, 3), 1, dtype=float)
b=np.full((3, 2), 7, dtype=int)
print(f"\nПервая матрица:\n {a}")
print(f"\nВторая матрица:\n {b}")
print(f"\nПроизведение матриц:\n {a.dot(b)}")