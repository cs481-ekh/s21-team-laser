import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft
def plot(filename):
    ###########   INPUT DATA   ###########
    # https://stackoverflow.com/questions/46614526/how-to-import-a-csv-file-into-a-data-array
    raw_data = np.genfromtxt(filename)

    ###########   EXTRACT AXES AND ACTUAL DATA   ###########
    # this is the format for TA data at BSU and can be hard-coded safely
    # the value of -10000 at coordinates (0,0) is simply a registration value and is not needed for anything
    wlax = raw_data[1:,0]
    tax  = raw_data[0,1:]
    data = raw_data[1:,1:]

    ###########   SPEED OF LIGHT (nm/ps)   ###########
    # often comes in handy but may or may not use
    cc = 299792.5

    ###########   PLOT RAW DATA WITH AXES   ###########
    maxxer = np.max(abs(data))
    plt.figure(1)
    plt.pcolor(tax, wlax, data, cmap='bwr', vmin=-maxxer, vmax=maxxer, shading='auto')
    plt.xlabel('delay time (ps)')
    plt.ylabel('detection wavelength (nm)')
    plt.title('raw TA spectrum ($\Delta T/T$)')
    plt.colorbar()
    plt.show()

# ###########   PLOT DATA WITHOUT AXES TO IDENTIFY CUT POINTS  ###########
# # typically the nonresonant response at time zero is quite bright
# # hence I zoom in the colourscale a bit to see better where to cut
# plt.figure(2)
# plt.imshow(data, cmap='bwr', vmin=-0.5*maxxer, vmax=0.5*maxxer)
# plt.xlabel('delay time (index)')
# plt.ylabel('detection wavelength (index)')
# plt.title('raw TA spectrum ($\Delta T/T$)')
# plt.show()

# ###########   TRUNCATE AXES AND DATA USING CUT POINTS   ###########
# wlaxcp1 = 550
# wlaxcp2 = 1750
# taxcp = 300
# # I assume we use the time domain data all the way to the end

# trunc_tax = tax[taxcp:]
# trunc_wlax = wlax[wlaxcp1:wlaxcp2]
# trunc_data = data[wlaxcp1:wlaxcp2,taxcp:]


# ###########   REMOVE UNDERLYING 'STATIC' SIGNAL   ###########
# # The non-oscillatory background signal has an exponential decay.
# # However the decay time is very long relative to oscillatory signals.
# # Therefore, for simplicity, I simply subtract an averaged background signal.
# bkgrd = np.mean(trunc_data[:,-10:],1)  # average of 10 final time points
# trunc_data_subtracted = trunc_data - np.transpose(np.tile(bkgrd, (np.size(trunc_tax), 1)))


# ###########   PLOT TRUNCATED DATA WITH AXES   ###########
# maxxer2 = np.max(abs(trunc_data_subtracted))
# plt.figure(3)
# plt.pcolor(trunc_tax, trunc_wlax, trunc_data_subtracted, cmap='bwr', vmin=-maxxer2, vmax=maxxer2, shading='auto')
# plt.xlabel('delay time (ps)')
# plt.ylabel('detection wavelength (nm)')
# plt.title('truncated raw TA spectrum with static signals subtracted ($\Delta T/T$)')
# plt.colorbar()
# plt.show()


# ###########   FOURIER TRANSFORM OVER DELAY-TIME DIMENSION   ###########
# # Somehow Python understands that I want to only Fourier transform along 1 dimension
# # and it knows what dimension I want.
# # That's confusing and a point of potential errors.
# fft_data = fft(trunc_data_subtracted)

# ###########   PLOT SPECTRUM WITHOUT AXES   ###########
# maxxerf = np.max(abs(fft_data))
# # Typically there is a spike at zero frequency.
# # Therefore we often have to adjust the colorscale by a user-defined amount to see anything.

# plt.figure(4)
# plt.imshow(abs(fft_data), cmap='Reds', vmin=0, vmax=0.1*maxxerf)
# plt.xlabel('oscillation frequency (index)')
# plt.ylabel('detection wavelength (index)')
# plt.title('amplitude FFT of truncated TA spectrum')
# bounder1 = round(np.size(trunc_tax)/2)
# plt.xlim(0, bounder1)
# plt.colorbar()
# # plt.xlim(200, 230)
# plt.show()

# # One confusing thing is that FFTs produce a duplicate set of symmetric data.
# # The only useful data is the first half.
# # Due to potential for odd numbers, it's hard to write scripts that select only half the data.
# # Therefore typically I just retain everything and zoom in the axis using axis limits.



# ###########   CREATE OSCILLATION FREQUENCY AXIS   ###########
# dt = np.mean(np.diff(trunc_tax))  # find the mean of the difference between time points
# df = 1/(dt*trunc_tax.size) # calculate here the frequency spacing
# ftax = df*np.arange(trunc_tax.size) # actually create the frequency axis here


# ###########   SUM THE ABSOLUTE VALUE OF THE SPECTRUM TO CREATE 1D PLOT   ###########
# spec_sum = abs(np.sum(fft_data, axis=0))

# ###########   PLOT 1D SPECTRUM WITH AXES   ###########
# plt.figure(5)
# # plt.plot(spec_sum)
# plt.plot(ftax, spec_sum)
# plt.xlabel('oscillation frequency (THz)')
# plt.title('total vibronic spectrum')
# plt.xlim(0, 100)
# # plt.xlim(0, 40)  # I used these bounds to zoom in on one peak
# # Due to the physics, we should be safe to hard-code the bounds to 0 and 100 THz
# plt.ylim(0, 500)
# plt.show()


# ###########   FCS PLOT FOR A SPECIFIED FREQUENCY   ###########
# freqoi = 16 # index of the frequency of interest
# # I found this index value by patiently adjusting bounds of figure 5,
# # but we will want a GUI method of zooming in and selecting which frequency to view
# freqoi_freq = 0.01*round(100*ftax[freqoi]) # the frequency value of this index
# fcs_ext = fft_data[:,freqoi] # extract data of this oscillation frequency
# fcs_amp = abs(fcs_ext)/np.max(abs(fcs_ext)) # normalized amplitude profile
# fcs_phs = np.unwrap(np.angle(fcs_ext))/np.pi # unwrapped phase profile in units of pi radians

# # plotting the amplitude and phase profiles with a shared horizontal axis
# fig6, ax0 = plt.subplots()
# ax0.plot(trunc_wlax, fcs_amp, c='k', linewidth=3.0)
# ax0.set_ylim(0, 1.1)
# ax0.set_yticks([0, 1])
# plt.xlabel('detection wavelength (nm)')
# ax0.set_xlim(500, 750) # fairly safe to hard-code these limits
# ax0.set_ylabel('amplitude (arb. unit)')

# ax1 = ax0.twinx()  # instantiate a second axes that shares the same x-axis
# ax1.plot(trunc_wlax, fcs_phs - min(fcs_phs), c='r', linewidth=3.0)
# ax1.set_ylabel('phase (radians/$\pi$)')
# plt.title('FCS of ' + str(freqoi_freq) + ' THz')
# fig6.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.show()
# # fig6.savefig('example.pdf', format='pdf')

# # We will need a way to save the Fourier data (trunc_wlax, fcs_amp, fcs_phs) to an ascii file so that
# # non-expert users could import and adjust in something terrible like Microsoft Excel.