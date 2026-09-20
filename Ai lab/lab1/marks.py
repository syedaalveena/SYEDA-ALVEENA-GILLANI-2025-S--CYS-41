def obtain_marks(classes):
    if classes == 6:
        return 60
    elif classes == 5:
        return 50
    elif classes == 4:
        return 40
    elif classes == 3:
        return 30
    elif classes ==2:
        return 20
    elif classes == 1:
        return 10
    else:
        return 0
print("Enter the number of classes attended:")
classes_attended = int(input())
marks_obtained = obtain_marks(classes_attended)
print(f"Marks obtained: {marks_obtained}")