#PyQt5 Stopwatch

import sys
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QDesktopWidget, QVBoxLayout,
                             QHBoxLayout)
from PyQt5.QtGui import QIcon

class Stopwatch(QWidget):
  def __init__(self):
    super().__init__()
    self.time = QTime(0, 0, 0, 0)
    self.time_label = QLabel("00:00:00:00", self)
    self.start_button = QPushButton("Start", self)
    self.stop_button = QPushButton("Stop", self)
    self.reset_button = QPushButton("Reset", self)
    self.timer = QTimer(self)
    self.initUI()
    
  def initUI(self):
    self.setWindowTitle("Stopwatch")
    self.resize(300, 200)
    self.setWindowIcon(QIcon("clock.jpg"))
    
    vbox = QVBoxLayout()
    vbox.addWidget((self.time_label))
    vbox.addWidget((self.start_button))
    vbox.addWidget((self.stop_button))
    vbox.addWidget((self.reset_button))
    
    self.setLayout(vbox)
    
    self.time_label.setAlignment(Qt.AlignCenter)
    
    hbox = QHBoxLayout()
    hbox.addWidget((self.start_button))
    hbox.addWidget((self.stop_button))
    hbox.addWidget((self.reset_button))
    
    vbox.addLayout(hbox)
    
    self.setStyleSheet("""
    QPushButton{
      font-size: 50px;
    }
    QLabel{
      font-size: 120px;
      background-color: hsl(200, 100%, 85%);
      border-radius: 20px;
    }
    """)
    
    self.center()
  
  def start(self):
    pass
  
  def stop(self):
    pass
  
  def reset(self):
    pass
  
  def center(self):
    screen = QDesktopWidget().availableGeometry().center()
    frame = self.frameGeometry()
    frame.moveCenter(screen)
  
def main():
  app = QApplication(sys.argv)
  stopwatch = Stopwatch()
  stopwatch.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()
