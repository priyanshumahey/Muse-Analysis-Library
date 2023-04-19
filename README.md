# Muse-Analysis-Library (old test version, do not use!)
This is a library built for analaysis of a specific set of signal data.
To use the code, read through the documentation to learn more. This is simply an early library and will be updated much more later on.

## Import
```py
import muse_an_libr
#overview
#Base validation 
from muse_an_libr import Validate

#Random Data Generator
from muse_an_libr import RandomData

#Filters
from muse_an_libr import Filter

#For Visualization Purposes
from muse_an_libr import Visualize
```

## Base
The base module consists of the class Validate and this is primarily used for validation and extracting specific data from the data. 

``` py
#muse_an_libr.Validate is the class from the base module

#muse_an_libr.Validate.Valid() Checks if the format is proper. False or error means that the format would not be correct for the requirements of other projects.
print(muse_an_libr.Validate.Valid([[1,[1,1]]])) #returns False
print(muse_an_libr.Validate.Valid([[1,[1,1,1,1,1]]])) #returns True
```

For data extraction from a valid dataset, you can use:
muse_an_libr.Validate.TimeStamp to get the timestamps
muse_an_libr.Validate.Values to get the values
muse_an_libr.Validate.ValuesSpecific to get specific values from a specific channel

## Random Data Generator
We can generate random data to work with using RandomData. 
``` py
x = muse_an_libr.RandomData.sample_muse(3)
print(x)
muse_an_libr.Visualize.plot_rand(x)

y = muse_an_libr.RandomData.sig_gen(10, 200, 100, 10, 15)
print(y)
muse_an_libr.Visualize.plot_rand(y)
```

## Filters
The filters are a bit more complex. The filters include fft, low pass and high pass as of now.

### FFT
Fast fourier transform is an algorithm that computes Fourier transforms. 
To use:

``` py
z = muse_an_libr.Filter.fft(muse_an_libr.RandomData.sig_gen(3, 2, 80, 50, 3), 3)
```

### Low Pass
The low pass filter passes frequencies that are lower than a certain cutoff frequency and it attenuates signals that have a higher frequency than desired. The current method takes from the fft to get the cuttoff.

``` py
cutoff = muse_an_libr.Filter.amp_calc(z[1])
peak_freq = freq_calc(z[0], z[2], 3)
filt_data = muse_an_libr.Filter.butter_lowpass_filter(y, peak_freq[0], 50, 2)
```

### High Pass
The high pass filter passes frequencies that are higher than a certain cutoff frequency and it attenuates signals that have a lower frequency than desired.
``` py
high = muse_an_libr.Filter.butter_highpass_filter(muse_an_libr.RandomData.sig_gen(5, 6, 80, 1, 1), peak_freq[0], 50)
```

## Visualize
The visualization functions will be more robust going onwards but as of now, there is only a simple plot function designed initially for the random data generated.
``` py
y = muse_an_libr.RandomData.sig_gen(10, 200, 100, 10, 15)
muse_an_libr.Visualize.plot_rand(y)
```
