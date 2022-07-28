# v1.0
from random import choice
print('choose one side to shoot:')
print('left,center,right')
you = input()
print('You kicked %s' % (you))
direction = ['left', 'center', 'right']
com = choice(direction)
print('Computer saved %s' % (com))
if you != com:
    print('Goal')
else:
    print('Oops...')
