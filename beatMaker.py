import wave
import numpy as np
# beat_generator is a function that take a string that point to your wave file as a first argument
# and the number of mouvments you want your poppit to do in 1s as second argument
# and return a numpy list that contain the moments where you should have your poppit moving ie (the beats)
def beat_gen(song, moves):
    spf = wave.open(song, "r")
    signal = spf.readframes(-1)
    signal = np.frombuffer(signal, "int16")
    signal = signal.astype(float)
    fs = spf.getframerate()
    movess = [np.sum(np.absolute(np.asarray(signal[j:j+2*fs], dtype=float)))/fs
              for j in range(0, int(len(signal)-fs), 2*fs)]
    movess = np.asarray(movess, dtype=float)
    movess = np.round((movess/max(movess))*moves)
    movess = movess - (movess/5) 
    movess = np.round((movess/max(movess))*moves)
    print(movess)
    beats = []
    for j in range(0, int(len(signal)-fs), 2*fs):
        i = movess[int(j/(2*fs))]
        if i > 0 :
          beats.append(
            [j+k + (np.where(signal[j+k:j+k+int(2*fs/i)] ==
                           max(signal[j+k:j+k+int(fs/i)]))[0][0])
                           for k in range(0, 2*fs, int((2*fs)/i))])
       
    beats = np.hstack(beats)
    return np.asarray(beats, dtype=float)/(2*fs)
