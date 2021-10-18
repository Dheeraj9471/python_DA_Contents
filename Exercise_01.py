
#Q1 wap to add 2 numbers
#Ans:-
a = 5
b = 6
s = a + b
print(s)

#Q2 wap to add 2 numbers with user inputs
#Ans:-
n1 = int(input("Enter your 1st Choice:  "))
n2 = int(input("Enter your 2nd Choice:  "))
res= n1 + n2
print("The Results of the sum: ",res)

#Q3 wap to find remainder when a number is divide by 2 or 3
#Ans:-
a = 2
b =3
s = b % a
print("Results : ",s)

#Q4 make a input function and check its type
#Ans:-
n =  input("Enter your choice: ")
print(type(n))

#Q5 Make two variable a & b ,also find which variable is greater use comaprison operator
#Ans 1st method:
a = 6
b = 5
s = a > b
print("Resulta are: ",a ,"is greater then b ")
s = a < b
print("Resulta are: ",a ,"is less then b ")
s = a = b
print("Resulta are: ",a ,"is Equal to b ")
s = a < b
print("Resulta are: ",b ,"is greater then a")
s = a > b
print("Resulta are: ",b ,"is Less then a")
#2nd method
a = int(input("Enter your choice:"))
b = int(input("Enter your choice:"))
if a > b:
    print(a, "is greater then ",b) 
elif a == b:
    print(a,"is Equal to",b)
else:
    print(b,"b is greater then ",a)

#Q6 Find Avg. of two numbers
#Ans:-
n1 = float(input("Enter your 1st Choice:  "))
n2 = float(input("Enter your 2nd Choice:  "))
res = (n1+n2)/2
print("Results are: ",res)

#Q7 Square of two numbers
#ans 1st:-
n1 = int(input("Enter your 1st Choice:  "))
n2 = int(input("Enter your 2nd Choice:  "))
res = n1**n2
print(" Results are: ",res)
#2nd:-
n = int(input("Enter your 1st Choice:  "))
res = n**n
print("Result are : ",res)

#Q8 cube of a num.
#Ans:-
n = int(input("Enter your choice:  "))
res = n*n*n
print("Results are: ",res)