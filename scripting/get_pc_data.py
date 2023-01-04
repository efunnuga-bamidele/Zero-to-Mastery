import serial

# open the serial port
ser = serial.Serial("/dev/ttyUSB0", 9600)

while True:
  # read a line from the serial port
  request = ser.readline().strip()

  # if the request is for the operating system, send a response
  if request == "get operating_system":
    ser.write("Windows 10\n")