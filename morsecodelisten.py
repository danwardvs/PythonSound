#!/usr/bin/python

# open a microphone in pyAudio and listen for taps


import pyaudio
import struct
import math
import string

CODE = {'.-': 'A',     '-...': 'B',   '-.-.': 'C', 
        '-..':'D',    '.': 'E',      '..-.': 'F',
        '--.': 'G',    '....': 'H',   '..': 'I',
        '.---': 'J',   '-.-': 'K',    '.-..': 'L',
        '--': 'M',     '-.': 'N',     '---': 'O',
        '.--.': 'P',   '--.-': 'Q',   '.-.': 'R',
        '...': 'S',    '-': 'T',      '..-': 'U',
        '...-': 'V',   '.--': 'W',    '-..-': 'X',
        '-.--': 'Y',   '--..': 'Z',
        
        '-----': '0',  '.----': '1',  '..---': '2',
        '...--': '3',  '....-': '4',  '.....': '5',
        '-....': '6',  '--...': '7',  '---..': '8',
        '----.': '9' 
        }


def decode(code):
    code = code + " "
    letter = ""
    message = ""
    for i in range(0, len(code)):
        if code[i] != " ":
            letter = letter + code[i]
        
        if code[i] == " ":
            decoded_letter = str(CODE[letter],)
            message = message + decoded_letter
            letter = ""
        if code[i] == "/":
            message = message + " "
            
        
    print message
    



INITIAL_TAP_THRESHOLD = 0.010
FORMAT = pyaudio.paInt16 
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100  
INPUT_BLOCK_TIME = 0.10
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
# if we get this many noisy blocks in a row, increase the threshold
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
# if we get this many quiet blocks in a row, decrease the threshold
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
# if the noise was longer than this many blocks, it's not a 'tap'
MAX_TAP_BLOCKS = 5

def get_rms( block ):
    # RMS amplitude is defined as the square root of the 
    # mean over time of the square of the amplitude.
    # so we need to convert this string of bytes into 
    # a string of 16-bit samples...

    # we will get one short out for each 
    # two chars in the string.
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
        # sample is a signed short in +/- 32768. 
        # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )

class TapTester(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1 
        self.quietcount = 0 
        self.errorcount = 0
        self.letter = ""
        self.code = ""
        self.added_space = False
        self.done = False

    def stop(self):
        self.stream.close()

    def find_input_device(self):
        device_index = None            
        for i in range( self.pa.get_device_count() ):     
            devinfo = self.pa.get_device_info_by_index(i)   
            print( "Device %d: %s"%(i,devinfo["name"]) )

            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower():
                    print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                    device_index = i
                    return device_index

        if device_index == None:
            print( "No preferred input found; using default input device." )

        return device_index

    def open_mic_stream( self ):
        device_index = self.find_input_device()

        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = device_index,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

        return stream

    def shortTapDetected(self):
        self.added_space = False
        self.letter = self.letter + "."
        

    def longTapDetected(self):
        self.added_space = False
        self.letter = self.letter + "-"
        
        

    def listen(self):
        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
        except IOError, e:
            # dammit. 
            self.errorcount += 1
            print( "(%d) Error recording: %s"%(self.errorcount,e) )
            self.noisycount = 1
            return

        amplitude = get_rms( block )
        if amplitude > self.tap_threshold:
            # noisy block
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > OVERSENSITIVE:
                # turn down the sensitivity
                self.tap_threshold *= 1.1
        else:            
            # quiet block.
            
            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                self.shortTapDetected()
                

            elif 1 <= self.noisycount <= 10:
                self.longTapDetected()
                
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > UNDERSENSITIVE:
                # turn up the sensitivity
                self.tap_threshold *= 0.9

        if self.quietcount > 3 and self.added_space == False:
            self.added_space = True
            self.code = self.code + " "
            self.code = self.code + self.letter
            self.letter = ""
        if self.quietcount > 40:
            print(self.code)
            print("Done!")
            self.done = True
            
            

if __name__ == "__main__":
    tt = TapTester()
    raw_input("Press Enter to continue")
    tt.noisycount = 0
    tt.quietcount = 0
    print("Listening...")
    while tt.done != True:
        tt.listen()
    tt.code = tt.code.lstrip(' ')
    decode(str(tt.code))
