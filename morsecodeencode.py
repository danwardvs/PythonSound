import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(0, GPIO.OUT) ## Setup GPIO Pin 7 to OUT



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
                        beep_short()
                if i == "-":
                        beep_long()
                if i == " ":
                        time.sleep(0.7)
                

def beep_short():
        GPIO.output(17,True)## Switch on pin 7
        time.sleep(0.1)## Wait
        GPIO.output(17,False)## Switch off pin 7
        time.sleep(0.1)## Wait

def beep_long():
        GPIO.output(17,True)## Switch on pin 7
        time.sleep(0.3)## Wait
        GPIO.output(17,False)## Switch off pin 7
        time.sleep(0.3)## Wait


get_message()



