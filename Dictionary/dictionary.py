# student = { 
#     "name":"hanzla",
#     "subject": {
#         "phy" : 23,
#         "chem": 34,
#         "bio" : 47
#     }
# }

# print(student["subject"]["chem"])
# print(student.keys())     # keys used for which key used in the dic
# print(student.items())  # items used for the all item with keys and values 
# print(student.values())  #values used for to get values of all key which uswed in the dic
# print(student.get("subject"))  # used to ge values of that key which we used
# student.update({"marks":7239})
# print(student)

# Q=:  store word and meaning in python dictionary

# dic = {
#     "table" : ["A piece of furniture","list of facts and figures"],
#     "cat" : "a small animal"

# }
# print(dic)




marks = {}
x = int(input("enter marks of chem :"))
marks.update({"chem":x})
y = int(input("enter marks of phy :"))
marks.update({"phy":y})
z = int(input("enter marks of bio :"))
marks.update({"bio":z})
print(marks)