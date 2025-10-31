# Age category

age = int(input("Enter your age?: "))

def age_cat():
    if age < 13:
        return "Child"
    elif age >= 13 and age < 19:
        return "Teenager"
    else:
        return "Adult"

print(age_cat())