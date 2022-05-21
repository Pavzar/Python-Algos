def is_palindrome(number):
    number = abs(number);
    number_copy = number;
    reverse = 0;
    while number_copy > 0:
        last_digit = number_copy % 10
        reverse = reverse * 10 + last_digit
        number_copy //= 10
    if number == reverse:
        return True
    return False


print(is_palindrome(7007))