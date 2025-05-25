import random

operators = ['+', '-', '*', '/']

def play_game(points, level, operators):
    question = 1
    print("Solve as quick as possible")

    while question <= 5:
        if level == 1:
            a, b = random.randint(1, 100), random.randint(1, 100)
        elif level == 2:
            a, b = round(random.uniform(101, 500), random.randint(1, 2)), round(random.uniform(101, 500), random.randint(1, 2))
        else:
            a, b = round(random.uniform(501, 1000), random.randint(2, 4)), round(random.uniform(501, 1000), random.randint(2, 4))

        print(f"Q{question}'s out")
        op = random.choice(operators)

        if op == '+':
            answer = a + b
        elif op == '-':
            answer = a - b
        elif op == '*':
            answer = a * b
        else:
            answer = a / b

        print(f'{a} {op} {b} = ', end='')
        user = float(input())

        if user == answer:
            points += 1
            print('WoW : +1')
        else:
            points -= 1
            print('What a Blunder : -1')

        question += 1

    print(f'Total points obtained : {points}')

def play_again():
    print("""
        ===== For playing again =====
        ---------- Press 1 ----------
        ====== For Leaving game =====
        ---------- Press 2 ----------
        """)
    choice = int(input('Enter here 1 / 2 : '))
    return choice == 1

keep_playing = True

while keep_playing:
    print('\n \t===============================')
    print('\tWelcome to the PUZZLE world!')
    print('\t===============================')
    print('''
          Game Instruction:
          -> For complexity - medium - use only 1 digit after point
          -> For complexity - hard - use only 2 digit after point
          ''')
    print("""\tChoose complexity
            1. Easy
            2. Medium
            3. Hard""")

    score = 0
    level = int(input('Choose complexity from the above : '))

    if level in [1, 2, 3]:
        print("-- Let's see how quick you are! --")
        play_game(score, level, operators)
        keep_playing = play_again()
    else:
        print('Enter a valid choice')
