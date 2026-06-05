def is_palindrome(num):
    return str(num) == str(num) [::-1]

number = int(input("Enter a number:"))
palindrom_check = is_palindrome(number)
print("Is given number a Palindrome?", palindrom_check)

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    if sum(int(d)**power for d in digits) == num:
            return True
    else:
            return False
            
armstrong_check = is_armstrong(number)
print("Is given nymber an Armstrong?", armstrong_check)