# i = 5
# print(i)
# i = i + 1
# print(i)
#
# s = '''This is a multi-line string.
# This is the second line.'''
# print(s)


# length = 5
# breadth = 2
#
# area = length * breadth
# print('Area is', area)
# print('Perimeter is', 2 * (length + breadth))

#
# number = 23
# guess = int(input("Enter an integer: "))
#
# if guess == number:
#     print("Congratulations you guessed it!")
#     print("But!...There's no prize :D")
# elif guess < number:
#     print("Nope, it's a little higher than that")
# else:
#     print("Nah, it's a little lower than that")
#
# print('Done')


# number = 23
# running = True
#
# while running:
#     guess = int(input("Enter an integer: "))
#
#     if guess == number:
#         print("Congratulations! You've guessed it")
#         running = False
#     elif guess < number:
#         print("Nope, it's a little higher than that. Guess again.")
#     else:
#         print("Nah, it's a little lower than that. Please guess again.")
#
# else:
#     print('The while loop is over.')
#
# print("Done.")


# for i in range(1, 5, 2):
#     print(i)
# else:
#     print('The for loop is over')
#
# for i in list(range(5)):
#     print(i)
# else:
#     print('The for loop is over')


# while True:
#     s = input('Enter something: ')
#     if s == 'quit':
#         break
#     print('Length of the string is', len(s))
# print('Done')


# while True:
#     s = input('Enter something: ')
#     if s == 'quit':
#         break
#     if len(s) < 3:
#         print("Too short")
#         continue
#     print('Length of the string is sufficient.')
# print('Done')


# def print_max(a, b):
#     if a > b:
#         print(a, 'is maximum.')
#     elif a == b:
#         print(a, 'is equal to', b)
#     else:
#         print(b,'is maximum.')
#
# print_max(4,6)
#
# x = 3
# y = 1
# print_max(x,y)


# x = 50
#
# def funct(x):
#     print('x is', x)
#     x = 45
#     print('changed local x to', x)
#
# funct(x)
# print('Global x is still', x)


# x = 50
#
# def funct():
#     global x
#     print('x is', x)
#     x = 45
#     print('changed global x to', x)
#
# funct()
# print('Global x is now', x)


# def say(message, times = 1):
#     print(message * times)
# say('hello')
# say('World',5)


# def func(a, b=5, c=10):
#     print('a is', a, 'and b is', b, 'and c is', c)
#
# func(3, 6)
# func(32, c=67)
# func(c=12, a=42)


# def total(a=5, *numbers, **phonebook):
#     print('a', a)
#
#     #iterate through all the items in tuple
#     for single_item in numbers:
#         print('single_item', single_item)
#
#     #iterate through all the items in dictionary
#     for first_part, second_part in phonebook.items():
#         print(first_part,second_part)
#
# total(10,1,2,3,Jack=1123,John=2231,Inge=1560)


# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return 'The numbers are equal'
#     else:
#         return y
#
# print(maximum(2, 3))


def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)