//Program to calculate number of upper and lower case in a string
value=raw_input("Enter string to be validated")
x=0
y=0
for i in value:
      if(i.islower()):
            x=x+1
      elif(i.isupper()):
            y=y+1
print("Number of lowercase in the string are:" )
print(x)
print("Number of uppercase in the string are:" )
print(y)

