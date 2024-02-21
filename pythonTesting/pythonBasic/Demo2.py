# https://www.digitalocean.com/community/tutorials/python-data-types

# "List" is a data type allows multiple values and different data types
values = [1, 2, "yannie", 4, 5]
print(values[0])    # 1
print(values[2])    # yannie
print(values[-1])   # value from the last index
print(values[1:3])  # [2, "yannie"]

# insert
values.insert(3, "genki")   # [1, 2, 'yannie', 'genki', 4, 5]
print(values)
# append
values.append("End")                        # [1, 2, 'yannie', 'genki', 4, 5, 'End']
print(values)
# update
values[2] = "YANNIE"                        # [1, 2, 'YANNIE', 'genki', 4, 5, 'End']
print(values)
# delete
del values[0]                               # [2, 'yannie', 'genki', 4, 5, 'End']
print(values)


# "Tuple" is a data type similar to list BUT it is write-protected, which means it's immutable
val = (10, 20, "yannie", 40, 50)
print(val[0])

# val[2] = "BRITNEY"   # 'tuple' object does not support item assignment
print(val)


# "Dictionary" is a sequence of data written in the form of key-value pair
dic = {1: "a", 2: 2, "three": 3, "Four": "C"}
print(dic[1])           # a
print(dic[2])           # 2
print(dic["three"])     # 3
print(dic["Four"])      # C


dictionary = {}
print(dictionary)
dictionary["first name"] = "Emma"
dictionary["last name"] = "Queen"
dictionary["gender"] = "Female"
print(dictionary)
print(dictionary["last name"])
