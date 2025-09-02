def prime_number(number):
    x = number // 2
    while x > 1:
        if number % x == 0:
            print(number, 'has factor', x)
            break
        x -= 1
    else:
        print(number, 'is_prime')
