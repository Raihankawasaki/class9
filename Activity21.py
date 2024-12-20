#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.

mc=input("Did u have  the medical cause Y or N: \n")
atten=int(input("Enter your attendence: \n"))
if mc=="Y":
    print("You can write the exam.")
else:
    if atten>=75:
        print("You can write the exam.")
    else:
        print("You can't write the exam. Should have come to school!")
