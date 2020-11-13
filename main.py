import random
import sys
from os import system
from ascii import bomb, logo, win
from word_dict import dict
system('title '+ 'pyBomb')


breaker = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'

state = True
while state:

    chosen_word = random.choice(dict).lower()
    # print(chosen_word) hack, i guess.
    guessed_word = []
    chances = 10
    wlength = len(chosen_word)  # wordlength
    print(logo)
    for char in range(wlength):
        guessed_word += '_'
    print('\nword: ', *guessed_word)
    print('>>>', guessed_word.count('_'), 'letter(s) remaining.', '\n>>>', chances, 'chance(s) remaining.')

    #update()
    def update():
        print(f'\n{breaker}')
        print('\nword: ', *guessed_word)
        print('>>>', guessed_word.count('_'), 'letter(s) remaining.', '\n>>>', chances, 'chance(s) remaining.')


    def end():
        print(breaker + '\ntype \'a\' to see information about the program.')
        ans = input('do you want to play again? y/n: ')[:1].lower()
        if ans == 'y':
            global state
            global game
            game = False
            state = True

        elif ans == 'a':
            breakabout = '----------------------------------------------------'
            print(f'''\n{breakabout}\n{logo}\n{breakabout}\n12/Nov/2020\nKIM SONG @CaptKrakenatic\nwith Python3 using modules: random, sys, os.\na hangman game but make it **bombs**\n{breakabout}\n''')
            end()
        elif ans == 'n':
            print('\nbye bye!')
            sys.exit()
        else:
            print('\n>>enter \'y\', \'n\', or \'a\' only.\n')
            end()


    game = True
    while game:


        guess = input('guess a letter: ')[:1].lower()
        if guess in guessed_word:
            print(f'you\'ve already guessed "{guess}" correctly. you still have {chances} chances remaining.')
            update()
            game = True
        else:
            l = ''
            for position in range(wlength):
                letter = chosen_word[position]
                if letter == guess:
                    l = letter
                    guessed_word[position] = letter
            # it was printing multiple lines of "you entered". it's because i put it in the loop.
            # i tried to fix it, i ran out of idea.
            # so this is the response for the right guess
            if l == guess:
                print(f'>>> you entered \"{guess}\". it was right! nice guessing, pal.')
                update()
            # player wins. no underscore(_) = no missing letter
            if '_' not in guessed_word:
                print(breaker, '\n', win)
                end()

            if guess not in chosen_word:
                chances -= 1
                if chances == 0:
                    print(bomb[0])
                    print(f'>>> the word was \"{chosen_word}\" <<<\n')
                    end()
                else:
                    print(bomb[chances])
                    print(f'>>> you guessed "{guess}". it was a wrong one, buddy. you just lost a life.')
                    update()
