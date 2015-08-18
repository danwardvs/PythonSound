import time ## Import 'time' library. Allows us to use 'sleep'

import math
import pyaudio

#sudo apt-get install python-pyaudio
PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000 #number of frames per second/frameset.      






def beep(LENGTH):
    #See http://www.phy.mtu.edu/~suits/notefreqs.html
    FREQUENCY = 900 #Hz, waves per second, 261.63=C4-note.


    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = 0
    WAVEDATA = ''    

    for x in xrange(NUMBEROFFRAMES):
     WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

    #fill remainder of frameset with silence
    for x in xrange(RESTFRAMES): 
     WAVEDATA = WAVEDATA+chr(128)

    p = PyAudio()



    stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)
    
    stream.write(WAVEDATA)

    stream.stop_stream()
    stream.close()
    p.terminate()



CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
def get_message():
        message_morse = ""
        msg = raw_input('MESSAGE: ')

        for char in msg:
                message_morse  = message_morse + str(CODE[char.upper()],) + " "
        print message_morse

        for i in message_morse:
                if i == ".":
                        beep(0.3)
                if i == "-":
                        beep(0.6)
                if i == " ":
                        time.sleep(0.7)
                
 
get_message()



