def convert(score):
    a = str(score)
    if len(a) == 2 and a.isdigit(): 
        return float(a[0] + '.' + a[1:])
    else:
        return float(a)

def grade(avg):
    if avg < 5:
        return "TRUOT"
    elif 5 <= avg < 8:
        return "CAN NHAC"
    elif 8 <= avg <= 9.5:
        return "DAT"
    else:
        return "XUAT SAC"

t = int(input())
students = []

for i in range(1, t + 1):
    name = input().strip()
    dlt = convert(input().strip())  
    dth = convert(input().strip())  
    avg = (dlt + dth) / 2  
    xl = grade(avg)  
    student_id = "TS0" + str(i) 
    students.append((student_id, name, avg, xl))
students.sort(key=lambda x: x[2], reverse=True)  
for student in students:
    print(f"{student[0]} {student[1]} {student[2]:.2f} {student[3]}")
