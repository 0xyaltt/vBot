import keyboard
import pickle
import mouse
import gd

print('enter a level to start recording')
mem = gd.memory.get_memory()

jump_at = []
def handle(event):
    jump_at.append({'pos':mem.x_pos,'event':event})

while 1:
    if mem.is_in_level():
        mouse.hook(handle)
        print('Recording')
        break

keyboard.wait('s')
mouse.unhook(handle)

file = input('what do you want to name this macro? ')

pickled = pickle.dumps(jump_at)

with open('macros/' + file,'wb') as f:
    f.write(pickled)

print('saved. ')
