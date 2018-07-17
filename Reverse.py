s=raw_input("Enter string to perform a reverse check")

def reverse(s): //using extended slicing
    s = s[::-1]
    return s
 
print("Entered string is:")
print(s)
print("Reversed string is:")
print(reverse(s))
if(reverse(s)==s):
  print("U entered a palindrome!")
else:
  print("Its not a palindrome")
