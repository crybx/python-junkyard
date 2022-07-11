# I think I was using this as a kind of scratch pad

# --------------------

# age = 26
# if 0 <= age <= 60:
#     print(age)

# --------------------

# x = int(input())
# y = int(input())

# if x in (1, 8) and y in (1, 8):
#     print(3)
# elif x in (1, 8) or y in (1, 8):
#     print(5)
# else:
#     print(8)

# --------------------

# print((1, 8))
# print(type((1, 8)))

# --------------------

# n = int(input())
# num_list = list()
#
# for _i in range(n):
#     num_list.append(int(input()))
#
# print(num_list)

# --------------------

# word = input()
# capital_letter_positions = list()
#
# for i in range(1, len(word)):
#     if word[i].isupper():
#         capital_letter_positions.append(i)
#
# word = word.lower()
#
# for x in range(len(capital_letter_positions)):
#     i = capital_letter_positions[-x - 1]
#     word = word[:i] + '_' + word[i:]
#
# print(word)

# --------------------

# string = ""
# for i in range(1, 58, 4):
#     string += "&" * i
#
# count = 0
# for char in string:
#     if char == "&":
#         count += 1
#
# print(string)
# print(count)

# --------------------

# numbers = [int(num) for num in input()]
# running_total = 0
#
# for i in range(len(numbers)):
#     running_total += numbers[i]
#     numbers[i] = running_total
#
# print(numbers)

# --------------------

# a = int(input())
# b = int(input())
# total = 0
# count = 0
#
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         total += i
#         count += 1
#
# mean = total / count
# print(mean)

# --------------------

# print(type(print))

# estimated completion time: 5 hours at 6 pm

# --------------------

# text = "Nobody expects the Spanish inquisition! And you?!"
# print(text)
# no_punctuation = text.replace("!", "").replace("?", "").replace(".", "").replace(",", "").lower()
# print(no_punctuation)
# low = no_punctuation.lower()
# print(low)
#
# string = "this is string example....wow!!! this is really string"
# print(string.replace("!!", ""))

# --------------------

# size = 8
# width = size * 2 - 1
#
# for i in range(size):
#     triangle = "#" + "#" * i * 2
#     padding = int((width - len(triangle)) / 2)
#     line = " " * padding + triangle
#     print(line)

# --------------------

# i = 0
# a = 'a'
# while i < 8:
#     a *= 2
#     i += 1
# print(a)
# print(len(a))

# --------------------

# start = 835950
# end = 139505
# current = start
# intervals = 0
#
# while current > end:
#     current = current / 2
#     intervals += 1
#
# print(int(intervals) * 12)
# # result should be 36

# --------------------

# square_list = list()
# sum_total = 0
#
# while sum_total != 0 or len(square_list) == 0:
#     x = int(input())
#     square_list.append(x * x)
#     sum_total += x
#
# print(sum(square_list))

# --------------------

# prime_numbers = [2]
#
# for i in range(3, 1001):
#     prime = True
#     for j in range(i - 1, 1, -1):
#         if i % j == 0:
#             prime = False
#             break
#     if prime:
#         prime_numbers.append(i)
#
# print(prime_numbers)

# --------------------

# a = "%.4f".format(3.14159265358979)
# b = "{1} {1} {1}".format(1, 2, 3)
# # c = "{1} is a {kind}".format(kind="fruit", "grapefruit")
# d = "{city} is the capital of {country}".format(country="Portugal",
#                                             city="Lisbon")
# print(a)
# print(b)
# # print(c)
# print(d)
# print('%.2f' % (21/4))

# --------------------

# income = int(input())
# tax_rate = 0
#
# if income <= 15527:
#     tax_rate = 0
# elif income <= 42707:
#     tax_rate = 15
# elif income <= 132406:
#     tax_rate = 25
# else:
#     tax_rate = 28
#
# print(f"The tax for {income} is {tax_rate}%. That is {round(income * tax_rate / 100)} dollars!")

# Hard: Password Hacker, Text Generator, Tic-Tac-Toe with an AI, Tetris, Text Based Browser
# Medium: Web scraper, Rock paper scissors with an AI
# Easy: Simple Chatty Bot, Hangman

# --------------------

# numbers = [2, 2, 4, 1, 1, 3, 5]
#
# numbers.remove(1)
# numbers.extend([0])
# numbers.append(len(numbers))
# numbers.remove(5)
# numbers.append(5)
#
# print(numbers)

# --------------------

# import creepy_hello_world
#
# creepy_hello_world.say_hello()

# --------------------
#
# # place `import` statement at top of the program
# import math
#
# # don't modify this code or the variables may not be available
# x, y = map(float, input().split(' '))
# math.copysign()

# --------------------

meals = [
        {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
        {"title": "Italian salad with fusilli and ham", "kcal": 320},
        {"title": "Bulgur with vegetables", "kcal": 350},
        {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
        {"title": "Oatmeal with honey and peanuts", "kcal": 440}]

kcals = [x["kcal"] for x in meals]

print(sum(kcals))




