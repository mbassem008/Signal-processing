#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:56:44 2019

@author: bassem
"""
import numpy as np

from scipy import signal
import matplotlib.pyplot as plt
b, a = signal.butter(4, 5000, 'low', analog=True)
w, h = signal.freqs(b, a)
plt.figure(figsize=(6,6))
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(5000, color='green')
plt.axvline(20000, color='green')

b1, a1 = signal.butter(4, 10000, 'High', analog=True)
w1, h1 = signal.freqs(b1, a1)
plt.semilogx(w1, 20 * np.log10(abs(h1)))
plt.show()

'''notre signale'''
from scipy import signal
import pandas as pd
from scipy import fftpack
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
df= pd.read_csv("/home/bassem/Downloads/trait_de_signal/signaljour1.txt",sep=',',header=None)
print(df)




import signaljour1 as sig
x=sig.exer
plt.figure(figsize= (6,6))
plt.title("Signal d'entreé")
plt.plot(x)
f_s =48000

X = fftpack.fft(x)
freqs = fftpack.fftfreq(len(x)) * f_s
fig, ax = plt.subplots()

ax.stem(freqs, np.abs(X))
ax.set_xlabel('Frequency in Hertz [Hz]')
ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
ax.set_xlim(0, f_s / 2)
ax.set_ylim(-5, 110)
'''application'''
'''butterworth_filter'''

fc=5000#fréquence de coupure
freq = fc / (f_s / 2) # Normalize the frequency
b, a = signal.butter(6, freq, 'low')
w, h = signal.freqs(b, a)
plt.figure(figsize=(6,6))
sig_filtred = signal.filtfilt(b,a,x)
plt.title('Butterworth_low_filter')
plt.plot(sig_filtred,label="butter" )

'''bessel'''
#fc=5000#fréquence de coupure
#w = fc / (f_s / 2) #
b1, a1 = signal.bessel(6,freq,'low')
#w1, h1 = signal.freqs(b1, a1)
plt.figure(figsize=(6,6))
sig_filtred1= signal.filtfilt(b1,a1,x)
plt.title('Bessel_low_filter')
plt.plot(sig_filtred1,label="butter")
plt.show()

'''cheby'''
b2, a2 = signal.cheby1(6,5,freq,'low')
plt.title('cheby1')
sig_filtred2 = signal.filtfilt(b2,a2,x)
plt.plot(sig_filtred2 )

'''Elliptic'''
b3, a3 = signal.ellip(6,1,100,freq,'low')
plt.title('Elliptic')
sig_filtred3 = signal.filtfilt(b3,a3,x)
plt.plot(sig_filtred3 )

'''iirnotch'''
fs = f_s# Sample frequency (Hz)
f0 = 15000  # Frequency to be removed from signal (Hz)
Q = 10.0  # Quality factor
b4, a4 = signal.iirnotch(f0,Q,fs)
plt.title('iirnotch')
sig_filtred4 = signal.filtfilt(b4,a4,x)
plt.plot(sig_filtred4)
'''iirpeak'''
fs = f_s# Sample frequency (Hz)
f0 = 15000  # Frequency to be retained from signal (Hz)
Q = 1.0  # Quality factor
b5, a5 = signal.iirnotch(f0,Q,fs)
plt.title('iirpeak')
sig_filtred5 = signal.filtfilt(b5,a5,x)
plt.plot(sig_filtred5)

