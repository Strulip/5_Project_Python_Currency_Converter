# According to Python best practices, we should import all necessary libraries at the beginning of a program
# In this challenge, you don't need to import any additional libraries.

def print_numbers(n):
    for i in range(1, n + 1):
        if i % (3*5) == 0:
            print('FizzBuzz')
            break
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


user_n = int(input())

print_numbers(user_n)