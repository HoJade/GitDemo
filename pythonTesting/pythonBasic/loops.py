# if else condition
greeting = "Good Morning"
print("******if else condition******")
if greeting == "Morning":
    print("Condition Matches")
else:
    print("Condition does not match")
print("if else condition is completed")


# for loop
obj = [2, 3, 5, 7, 9]
print("******for loop******")
for i in obj:
    print(i*2)


# print sum of first five natural number
print("******for loop summation******")
summation = 0
for j in range(1, 6):    # range(h,k) --> h to k-1
    summation = summation + j
print(summation)


print("******add a step******")
for k in range(1, 10, 5):
    print(k)

print("******skip first index******")
for m in range(10):     # start from 0 to m-1
    print(m)
