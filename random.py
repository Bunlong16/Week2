'''
    Exercise: Rock Paper Scissors
'''
import random
rocks = '''
        _    ,-,    ,-,
 ,--, /: :| |': :`.|: :|
|`;  ' `,'   `.;    `: |
|    |     |  '  |     |.
| :  |     |     |     ||
| :. |  :  |  :  |  :  | /
 |__|: :.. : :.. | :.. |  )
      `---',/___/,|___/ /'
           `==._ .. . /'
                `-::-'
'''
papers = '''
     _
               _  / |
              / | | | /|
               | || |/ /
                | / | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|

'''
scissors = '''
  ,--.
 (    )____ ___________________________
  `--'---,-'  ,.  |--------------------`-.
  ,--.---`-.  `'  |_______________________`>
 (    )"""" """""""""""""""""""""""""""""""
  `--'
'''
print(rocks,papers,scissors)
images = [rocks,papers,scissors]
cp = random.randint(0,2)
ppl = int(input('Welcome to Rock, Paper, Scissor Game\nWhat do you choose?\nRock (0), Paper (1), Scissor (2)\n=> '))

if ppl >= 3 or ppl < 0:
    print("You type an invalid number")
else: 
    print(images[ppl])

    print("The computer choose: ")
    print(images[cp])

    if ppl == cp:
        print("Draw")
    elif ppl == 0 and cp == 2:
        print("You win")
    elif ppl == 2 and cp == 0:
        print("You Lose")
    elif cp > ppl:
        print('You lose')
    elif ppl > cp:
        print("You win")
    else:
        pass