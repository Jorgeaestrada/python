from scipy.fftpack import fft, fftfreq
from numpy import pi

import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np

frecuencia, data = wav.read('sample.wav')

stereo_channel = data
left_channel = data.T[0]
rigth_channel = data.T[1]

# this is 16-bit track, b is now normalized on [-1,1]
normalized_stereo_channel = [(elements / 2**16.) * 2 - 1 for elements in stereo_channel] 
normalized_left_channel = [(elements / 2**16.) * 2 - 1 for elements in left_channel] 
normalized_rigth_channel = [(elements / 2**16.) * 2 - 1 for elements in rigth_channel] 

# audio simple
tiempo = float(len(data)) / float(frecuencia)

plt.subplot(221)
plt.title('simple left channel audio')
plt.plot(data.T[0])
#plt.xlim(0, tiempo)
plt.xlabel('Tiempo (s)')
plt.ylabel('$y(t)$')

# Sonido con FFT
left_fft_out = fft(normalized_left_channel) # calculate fourier transform (complex numbers list)
rigth_fft_out = fft(normalized_rigth_channel) # calculate fourier transform (complex numbers list)
stereo_fft_out = fft(normalized_stereo_channel) # calculate fourier transform (complex numbers list)



# espectro del hi-hat
plt.subplot(222)
plt.title('hihat con fft')
plt.plot(abs(left_fft_out[13500+256:14592]))
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Im($Y$)')

# espectro del bombo
plt.subplot(223)
plt.title('bombo con fft')
plt.plot(abs(left_fft_out[256:1280]))
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Im($Y$)')

# espectro de la tarola
plt.subplot(224)
plt.title('tarola con fft')
plt.plot(abs(left_fft_out[23552:27648]))
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Im($Y$)')

plt.show()
print(len(data)/1024)

tam_muestra = 1024
total_muestras = len(data)/tam_muestra
ax = 256
bx = tam_muestra + ax

for i in range(total_muestras):
	# print(np.amax(abs(left_fft_out[ax:bx])), '---->',    ax, ':',bx)
	ax = bx + 1
	bx = bx + tam_muestra
	
	
	
	
	
	
	
	
	
	
