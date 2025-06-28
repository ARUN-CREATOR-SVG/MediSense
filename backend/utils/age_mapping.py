'''
According to Diabetes Dataset age is coded in AGEG5YR FOMRAT ,
so this function will map the user input age to this format 
'''

def age_to_AGEG5YR(age: int) -> int:
    if 18 <= age <= 24: return 1
    elif 25 <= age <= 29: return 2
    elif 30 <= age <= 34: return 3
    elif 35 <= age <= 39: return 4
    elif 40 <= age <= 44: return 5
    elif 45 <= age <= 49: return 6
    elif 50 <= age <= 54: return 7
    elif 55 <= age <= 59: return 8
    elif 60 <= age <= 64: return 9
    elif 65 <= age <= 69: return 10
    elif 70 <= age <= 74: return 11
    elif 75 <= age <= 79: return 12
    elif age >= 80: return 13
    else:
        raise ValueError("Age must be at least 18")
