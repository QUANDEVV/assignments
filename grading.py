#Grading system  if statements 

def grade():
    grade =41
    if grade <=100 and grade > 80:
        print('A')
    elif grade <80 and grade > 60:
        print('B')
    elif grade <60 and grade > 40:
        print('C')
    elif grade <40 and grade > 20:
        print('D')
    else:
        print("failed")

grade()

