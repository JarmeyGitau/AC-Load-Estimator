# AC Load Estimator 
width=float(input("Enter the width of the room:"))
height=float(input("Enter the height of the room:"))
number_of_people=float(input("Enter the number of people:"))
horsepower=width*height*0.1+number_of_people*0.06
print(horsepower)