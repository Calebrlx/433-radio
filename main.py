import serial
import time

def send_command(ser, cmd):
    """Send a serial command to Baofeng radio."""
    ser.write(cmd.encode() + b'\r\n')
    time.sleep(0.5)
    response = ser.read(100).decode('utf-8').strip()
    return response

def transmit_cw():
    """Set frequency, power level, and transmit for 5 seconds."""
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
    time.sleep(2)

    print("Setting frequency to 433 MHz...")
    send_command(ser, 'VFO A 433000')
    send_command(ser, 'VFO A SELECT')

    print("Setting power to LOW (1W)...")
    send_command(ser, 'POWER LOW')

    print("Starting transmission...")
    ser.setRTS(True)  # Activate PTT
    time.sleep(5)  # Hold for 5 seconds
    ser.setRTS(False)  # Release PTT

    print("Transmission complete.")
    ser.close()

if __name__ == "__main__":
    transmit_cw()