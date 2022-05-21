n = int(input("Enter n: "))
first_term = int(input("Enter first term: "))
second_term = int(input("Enter second term: "))
i = 1
while i <= n:
    print(str(first_term) + ", ")
    next_term = first_term + second_term
    first_term = second_term
    second_term = next_term
    i += 1

