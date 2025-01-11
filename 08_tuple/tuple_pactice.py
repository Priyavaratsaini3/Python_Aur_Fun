thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry"))

print(thistuple)

print(thistuple[1])
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon")

print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-2])

if "apple" in thistuple:
    print("Yes, 'apple' is present in the tuple")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# paking tuple 
fruits = ("apple", "banana", "cherry")

# unpacking tuple
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# asterisk

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# loop through tuple
fruits = ("apple", "banana", "cherry")

for x in fruits:
  print(x)

# loop through the index numbers

thistuple = ("apple", "banana", "cherry")

for i in range(len(thistuple)):
  print(thistuple[i])

# using a while loop

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# join two tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# multiply tuple

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)