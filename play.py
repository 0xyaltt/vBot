import math
import gd
import mouse
import pickle

mem = gd.memory.get_memory()
file = input('Macro to play: ')
data = open('macros/' + file, 'rb').read()
jump_at = pickle.loads(data)

input('be on the main menu or its gonna bug')
print('the bot will play the macro once its on the level you want')
while 1:
    while mem.is_in_level():
        print('running macro..')
        for dict in jump_at:
            if dict['pos'] == mem.x_pos:
                mouse.play([dict['event']])
            
        if mem.is_dead():
            print('u died, restarting..')
        if math.floor(mem.percent) == 100:
            print('all clear!')
            break
