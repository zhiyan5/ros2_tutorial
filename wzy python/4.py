import serial

PORT = '/dev/ttyUSB0'
BAUD = 115200
 
ser = serial.Serial(PORT, BAUD, timeout=0.5)

print(f"串口 {PORT} 已打开，输入消息后按回车发送（输入 exit 退出）")

while True:
    msg = input("> ")
    if msg.lower() == "exit":
        break
    ser.write((msg + '\n').encode())