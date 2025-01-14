thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

thisset= {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset.discard("apple")
print(thisset)

thisset= {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset

thisset= {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"a", "d", "e"}
set4 = {1, 2, 4}

myset = set1.union(set2, set3, set4)
print(myset)

myset = set1 | set2 | set3 | set4
print(myset)

x = {"a", "b", "c"}
y = {1, 2, 3}
z = x.union(y)
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

set1 = {"a", "b" , "c"}
set2 = {"a", "f", "H"}
# set3 = set1.intersection(set2)
# print(set3)

set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)