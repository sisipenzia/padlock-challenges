#Solution for Challenge 1
def padlock1():
    code = 0
    for i in range(1, 41):
        code += i
    print(f'Code 1 : {code}')
padlock1()

#Solution for Challenge 2
def padlock2():
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if (digit1 < digit2) and (digit2 < digit3):
                    code += 1 
    print(f'Code 2 : {code}')
padlock2()

#Solution for Challenge 3
def padlock3():
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if (digit1 % 2 == 0) and (digit2 % 2 == 0) and (digit3 % 2 == 0):
                    code += 1
    print(f'Code 3 : {code}')
padlock3()

#Solution for Challenge 4
def padlock4():
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if (digit1 + digit2 + digit3) % 2 != 0:
                    code += 1
    print(f'Code 4 : {code}')
padlock4()

#Solution for Challenge 5
def padlock5():
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if (digit1 == digit2) | (digit2 == digit3) | (digit1 == digit3):
                    code += 1
    print(f'Code 5 : {code}')
padlock5()