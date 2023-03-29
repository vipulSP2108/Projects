import os

command = 'say'
os.system(f'{command} Hi! Welcome to Robospeaker')
os.system(f'{command} For ending the conversation print end')
while True:
    speak = input('say : ')
    if speak.lower() == 'end':
        os.system(f'{command} Bye! See you soon')
        break
    os.system(f'{command} speak')
