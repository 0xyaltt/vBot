import pickle

while 1:
  cmd = input('vB$ ')
  if cmd == 'play':
      import play
  if cmd == 'save':
      import record
  if cmd != 'save' and cmd != 'play':
      print(f'{cmd} is not a command.')
