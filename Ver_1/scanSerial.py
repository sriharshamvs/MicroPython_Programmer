import serial
import glob


class scanPorts:
    def __init__(self):
        super(scanPorts, self).__init__()

    def scanSerialPort(self):
        self.serialPort = glob.glob("/dev/tty*")
        serialPortList = self.getPortList(self.serialPort)
        return serialPortList

    def scanUSBtoSerial(self):
        self.usbPort = glob.glob("/dev/ttyUSB*")
        usbPortList = self.getPortList(self.usbPort)
        return usbPortList

    def getPortList(self, portList):

        if not portList:
            print("Empty List")
        else:
            portList.reverse()
        return portList

    def printDevices(self, port):
        print(port)


if __name__ == "__main__":
    print("custom PySerial Module")
    s = scanPorts()

    serialPorts = s.scanSerialPort()
    s.printDevices(serialPorts)

    usbPort = s.scanUSBtoSerial()
    s.printDevices(usbPort)
