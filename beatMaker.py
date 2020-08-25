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
    movess = [np.sum(np.absolute(np.asarray(signal[j:j+fs], dtype=float)))/fs
              for j in range(0, (int(len(signal)/2)-fs), fs)]
    movess = np.asarray(movess, dtype=float)
    movess = np.round((movess/max(movess))*moves)
    movess[movess == 0] = 1
    movess = movess - (movess/5) 
    movess = np.round((movess/max(movess))*moves)
    print(np.sum(movess))
    beats = []
    for j in range(0, int(len(signal)/2-fs), fs):
        i = movess[int(j/fs)]
        beats.append(
            [j+k + (np.where(signal[j+k:j+k+int(fs/i)] ==
                           max(signal[j+k:j+k+int(fs/i)]))[0][0])
                           for k in range(0, fs, int(fs/i))])
       
    beats = np.hstack(beats)
    return np.asarray(beats, dtype=float)/fs
