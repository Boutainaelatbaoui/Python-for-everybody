#Learn more or give us feedback
grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}



def students_names(class_name):
    if class_name=='grade_one' :
        for i in list(grade_one.keys()):
            print(i)
    elif class_name=='grade_two':
        for i in list(grade_two.keys()):
            print(i)
    elif class_name=='grade_three':
        for i in list(grade_three.keys()):
            print(i)
    return

def student_score(class_name ,student_name):
    if class_name=='grade_one':
        print(sum(grade_one.get(student_name)))
    elif class_name=='grade_two':
        print(sum(grade_two.get(student_name)))
    elif class_name=='grade_three' :
        print(sum(grade_three.get(student_name)))
        return

def students_count(class_name):
    if class_name=='grade_one' :
        print(len(list(grade_one.keys())))
    elif class_name=='grade_two' :
        print(len(list(grade_two.keys())))
    elif class_name=='grade_three' :
        print(len(list(grade_three.keys())))
    return

while True :
    x=input("choose one : students_names, student_score, students_count")

    if x=='students_names' :
        students_names(input("Enter class name :"))
    elif x=='student_score' :
        student_score(input( "Enter class name :"), input("Enter student name :"))
    elif x=='students_count' :
        students_count(input("Enter class name :"))

    x=input("choose Done to finish , or More to continue ")
    if x=='More' :
        continue
    else:
        break
