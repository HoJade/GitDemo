str1 = "https://rahulshettyacademy.com/"
str2 = "resource website"

print(str1[1])
print(str1[0:5])

print(str1+str2)    # concatenate

strValid = "academy"
print(strValid in str1)     # string check; return "True" or "False"

var = str1.split(".")       # string split; the split point based on the argument
print(var)
print(var[0])

str3 = " Great "
print(str3)
print(str3.strip())         # trim the white spaces in the beginning and at the end of the text
print(str3.lstrip())        # only trim the left
print(str3.rstrip())        # only trim the right
