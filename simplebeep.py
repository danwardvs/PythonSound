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
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
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


beep(0.3)
beep(0.3)
beep(0.7)
beep(0.7)




