# Traitement_signal
In this tutorial ,I try to explain some use case of signal processing with python.
i'll use the different filter like bessel_filter, cheby_filter,Elliptic_filter, iirnotch_filter et iirpeak_filter.

bessel_filter:

scipy.signal.bessel

scipy.signal.bessel(N, Wn, btype='low', analog=False, output='ba', norm='phase', fs=None)

    Bessel/Thomson digital and analog filter design.

    Design an Nth-order digital or analog Bessel filter and return the filter coefficients.

    
Also known as a Thomson filter, the analog Bessel filter has maximally flat group delay and maximally linear phase response, with very little ringing in the step response.
The Bessel is inherently an analog filter. This function generates digital Bessel filters using the bilinear transform, which does not preserve the phase response of the analog filter. As such, it is only approximately correct at frequencies below about fs/4. To get maximally-flat group delay at higher frequencies, the analog Bessel filter must be transformed using phase-preserving techniques.
    
 For more information about parameters and other filter, check the python documentation of Scipy.signal
 (Matlab-style IIR filter design) :
 
 https://docs.scipy.org/doc/scipy/reference/signal.html
 
