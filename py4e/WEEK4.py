#خزني الاجابة عند كتابتها بآتوم بملف اسمه week4.py
#حملي الملف بالاستمارة المرفقة بالاسفل
#المطلوب:
#"كتابة برنامج للمعلمات، يقوم هذا البرنامج ب:

#١- يظهر في البداية التعليمات للمعلمة، كالتالي:

#"Choose one: students_names, student_score, students_count"

#٢- ثم يطلب من المعلمة ادخال المعلومات المطلوبة: اسم الطالب٫ اسم الصف٫ او كلاهما، بحسب المطلوب في ال function.

#٣- البرنامج يحتوي على ثلاث functions:

 #""١) students_names

 #تظهر قائمة بأسماء الطلاب في الصف٫ تأخذ ١ argument: اسم الصف

#٢) student_score

 #تظهر مجموع علامات طالب في صف معين٫ تأخذ ٢ arguments: اسم الصف، واسم الطالب
#٣) student_count

# تظهر عدد الطلاب في الصف، تأخذ ١ argument: اسم الصف

#٤- بعد اظهار النتيجة نطلب من المعلمة إدخال done إذا انتهت ويغلق البرنامج٫ أو إدخال more لتقوم باختيار function اخرى لتنفيذها، فتظهر الرسالة الاولى:

#"Choose one: students_names, student_score, students_count"

#القواميس المستخدمة لتخزين المعلومات، أرجو نسخها كما هي:



def students_names(grade):
    names= list(grade.keys())
    return names

def student_score(grade, name):
    score= sum(grade[name])
    return score

def students_count(grade):
    names= list(grade.keys())
    count= len(names)
    return count

grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

a= input("Choose one: students_names, student_score, students_count: ")
if a == 'students_names':
    b= input("grade: ")
    if b == "grade_one":
        print(students_names(grade_one))
    elif b == "grade_two":
        print(students_names(grade_two))
    elif b == "grade_three":
        print(students_names(grade_three))
    else:
        print("grade is not exist")
