marks = int(input("Enter the marks:"))

# if the marks between 81 to 100
if marks > 80:
    print("Very Good")
# if the marks between 61 to 80
elif marks > 60:
    print("Good")
# if the marks between 41 to 60
elif marks > 40:
    print("Average")
# if the marks less than or equal 40
else:
    print("Fail")