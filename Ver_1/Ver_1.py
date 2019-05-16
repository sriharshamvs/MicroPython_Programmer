import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from subprocess import *
import scanSerial as scan


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "MicroPython Programmer Ver 1.0"
        self.setWindowIcon(QIcon('icon.png'))
        self.left = 800
        self.top = 200
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createUSBComboBox()
        self.createCommandComboBox()
        self.createButtons()
        self.createFileLabel()
        self.createSelectFileButton()

        self.WindowSelectFileLayout = QHBoxLayout()
        self.WindowSelectFileLayout.addWidget(self.selectFileButton)
        self.WindowSelectFileLayout.addWidget(self.fileLabel)

        self.WindowComboBoxLayout = QHBoxLayout()
        self.WindowComboBoxLayout.addWidget(self.usbCB)
        self.WindowComboBoxLayout.addWidget(self.commandCB)

        self.WindowMainLayout = QVBoxLayout()
        self.WindowMainLayout.addLayout(self.WindowSelectFileLayout)
        self.WindowMainLayout.addLayout(self.WindowComboBoxLayout)
        self.WindowMainLayout.addWidget(self.buttonBox)
        self.setLayout(self.WindowMainLayout)

    def createSelectFileButton(self):
        self.selectFileButton = QPushButton("Browse File")
        self.selectFileButton.clicked.connect(self.SelectFile_method)

    def createButtons(self):
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.Ok_slot_method)
        self.buttonBox.rejected.connect(self.Cancel_slot_method)

    def createCommandComboBox(self):
        CBlayout = QHBoxLayout()

        self.commandCB = QComboBox()
        self.commandList = ["put", "ls", "mkdir", "get",
                            "reset", "rm", "rmdir", "run"]
        self.commandCB.addItems(self.commandList)
        CBlayout.addWidget(self.commandCB)
        # self.cb.setLayout(CBlayout)

    def createUSBComboBox(self):
        usbCBlayout = QHBoxLayout()

        self.usbCB = QComboBox()
        self.rs = scan.scanPorts()
        self.port = self.rs.scanUSBtoSerial()
        self.list = self.rs.getPortList(self.port)
        self.usbCB.clear()
        self.usbCB.addItems(self.list)
        usbCBlayout.addWidget(self.usbCB)

    def createFileLabel(self):
        self.fileLabel = QLabel()
        self.fileLabel.setText("File Not Selected")
        self.fileLabel.setFont(QFont("Monofonto", 12, QFont.Bold))
        self.fileLabel.setAlignment(Qt.AlignCenter)

    @pyqtSlot()
    def SelectFile_method(self):
        self.options = QFileDialog.Options()
        self.options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=self.options)
        if self.fileName:
            self.head, self.tail = os.path.split(self.fileName)
            self.fileLabel.setText(self.tail)
            self.fileLabel.setFont(QFont("Monofonto", 12, QFont.Bold))
            print(self.fileName)

    def Ok_slot_method(self):

        # command : ampy --port /dev/ttyUSB0 command file

        self.selectedPort = self.usbCB.currentText()
        self.selectedCommand = self.commandCB.currentText()
        self.selectedFile = self.fileName

        self.command = "ampy --port"
        self.command = self.command + " "+self.selectedPort+" "+self.selectedCommand+" "+self.selectedFile
        print(self.command)
        os.system(self.command)

    def Cancel_slot_method(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
