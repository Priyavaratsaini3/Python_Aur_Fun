marks_eng = int(input("Enter the marks in English:"))
marks_math = int(input("Enter the marks in Math:"))

# if both the marks more than 80 so print grade A
if marks_eng > 80 and marks_math > 80:
    print("A grade")

# if either of marks are more than 80 so print B grade
elif marks_eng > 80 or marks_math > 80:
    print("B grade")

# if neither of marks are more than 80 so print C grade
else:
    print("C grade")
