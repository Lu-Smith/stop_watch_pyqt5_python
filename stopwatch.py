#PyQt5 Stopwatch

import sys
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton)

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
    pass
  
  def start(self):
    pass
  
  def stop(self):
    pass
  
  def reset(self):
    pass
  
def main():
  app = QApplication(sys.argv)
  stopwatch = Stopwatch()
  stopwatch.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()
