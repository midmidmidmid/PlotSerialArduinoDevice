import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
i = 0

# Initialize communication with Teensy
ser = serial.Serial("COM4", 9600)

# Format plot
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.30)
plt.title('Infrared Sensor Intensity')
plt.ylabel('Infrared Raw Intensity (arb. units)')
plt.ion()

while(True):
    var = ser.readline()
    wim = int(var)
    xs.append(i)
    ys.append(wim)
    print(xs[i])
    i = i + 1
    ax.plot(xs, ys)
    mod = i % 200
    if(mod==1):
        plt.close()
        plt.plot(xs, ys)
        plt.pause(0.05)
    plt.show(block=False)
    
plt.close()
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
