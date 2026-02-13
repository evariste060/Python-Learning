import copy
dict1 = {'name':"John",'age':30,'city':'New York'}
dict1["Member"] = [1,2,3]
dict2 = dict1
dict3 = copy.deepcopy(dict1)
dict2['age'] = 16
dict2["Member"].append(4)
print(dict1)
print(dict2)
print(dict3)
