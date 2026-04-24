import serial

PORT = '/dev/ttyUSB0'
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

print(f"串口 {PORT} 已打开，等待接收数据...")

while True:
    if ser.in_waiting:
        line = ser.readline().decode().strip()
        print(line)