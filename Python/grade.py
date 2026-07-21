def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


subjects = ["English", "Math", "Science", "Computer", "History"]
g = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter mark for {subject} (0-100): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= mark <= 100:
            break

        print("Please enter a mark between 0 and 100.")

    letter = grade(mark)
    g.append([subject, letter])

print(g)
