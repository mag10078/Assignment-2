


#Ques1

given_input = "Python is a case sensitive language"
print(given_input)


#PART a
str_length = len(given_input)

print("Length of the string is:", str_length)


#PART b
str_reverse = given_input[::-1]
print("The reversed string is:",str_reverse)


#PART c
#Using slice to store a part of string in a variable
str_slice = given_input[10:26]


#PART d
#repalcing the stored sliced string 
replaced_str = given_input.replace(str_slice, "object oriented")

print(replaced_str)


#PART e (Index of "a")
index_a = given_input.find("a")
print('Index of "a" substring in input string is:',index_a)


#PART f
#To remove white spaces, replacing spaces with empty quotes
g = given_input.replace(" ", "")

print(g)








#Ques 2

name = "Madhur"
SID = "21107102"
CGPA = "9.9"
department_name = "MECHANICAL"


print("Hey,",name, "Here!\nMy SID is", SID,"\nI am from", department_name, "department and my CGPA is", CGPA )


#Ques 3
a=56
b=10
print(a&b,a|b,a^b,a>>2,b>>2,a<<2,b<<4)


#Ques 4
inputstring=input("Enter string: ")
substring="name"
if substring in inputstring:
  print("Yes")
else:
  print("No")


  
#Ques 5
a=int(input("enter side 1: "))
b=int(input("enter 2nd side: "))
c=int(input("enter 3rd side: "))
while (a+b<=c) or (b+c<=a) or (c+a<=b):
  print("No")
  break
while (a+b>c) and (b+c>a) and (c+a>b):
  print("Yes")
  break





#Ques 6
number_1 = int(input("Enter 1st number (a) "))


number_2 = int(input("Enter 2nd number (b) "))


ex_or = number_1 ^ number_2


bin_exor = bin(ex_or)
check_string = str(bin_exor)


bits_need_flip = check_string.count("1")

print("Number of bits needed to be flipped to convert ‘a’ to ‘b’ are:", bits_need_flip)
