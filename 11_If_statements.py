is_male =True
is_tall =False

if is_male or is_tall:
    print("You are male or tall or both")
else:
    print("You are neither male or tall")

if is_male and is_tall:
    print("You are male and tall")
else:
    print("You are either not male or not tall or both")

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("You are either not male or not tall or both")