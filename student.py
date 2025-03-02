import pandas as pd
import numpy as np


student = []

for i in range(1,10000):
    student_id = f"S{i:05d}"
    name = f"Student_{i}"
    subjects = ["Electronics","Programming","Database","Data Science","Math","Eng"]
    marks = np.random.randint(40,100,size = 6)
    student.append([student_id,name]+list(marks))
df = pd.DataFrame(student, columns=["StudentID","Name","Electronics","Programming","Database","Data Science","Math","Eng"])

df.to_csv("student_mark.csv",index=False)
print("generated")