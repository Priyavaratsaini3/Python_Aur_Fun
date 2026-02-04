file = open("youtube.txt", 'w')

try:
    file.write("my name is prince")
finally:
    file.close()

with open('youtube.txt','w') as file:
    file.write("There is a book on the table")

