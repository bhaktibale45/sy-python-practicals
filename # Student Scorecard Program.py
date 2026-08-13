print("=====STUDENT SCORECARD=====")

subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))


total = subject1 + subject2 + subject3
average = TOTAL * 100/300


print("\n========== STUDENT SCORECARD ==========")
print(f"Subject 1: {subject1:.2f}")
print(f"Subject 2: {subject2:.2f}")
print(f"Subject 3: {subject3:.2f}")
print("---------------------------------------")
print(f"Total Marks: {total:.2f}")
print(f"Average:     {average:.2f}")
print("=======================================")