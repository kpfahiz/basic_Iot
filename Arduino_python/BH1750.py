import time
from PyMata.pymata import PyMata
port = PyMata("COM5")
port.i2c_config(0, port.ANALOG, 4, 5)
# Request BH1750 to send 2 bytes
port.i2c_read(0x23, 0, 2, port.I2C_READ)
# Wait for BH1750 to send the data
time.sleep(3)
# Read data from BH1750
data = port.i2c_get_read_data(0x23)
# Obtain lux values from received data
LuxSum = (data[1] << 8 | data[2]) >> 4
lux = LuxSum/1.2
print str(lux) + ' lux'
firmata.close()