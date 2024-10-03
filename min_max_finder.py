largest_num = None
smallest_num = None

list_user = input("Enter a list of integers(separate them using spaces): ")

numbers = list_user.split()
for num in numbers:
    num = int(num)
    if largest_num is None or num > largest_num:
        largest_num = num
    elif smallest_num is None or num < smallest_num:
        smallest_num = num
    else:
        print(f"Invalid input. {num} is not an integer.")
if largest_num is not None and smallest_num is not None:
    print("Largest Number is: ", largest_num)
    print("Smallest Number is: ", smallest_num)
else:
    print("Not valid numbers. Please enter an integer.")