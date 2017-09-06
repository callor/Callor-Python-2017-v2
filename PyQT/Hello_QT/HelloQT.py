'''
Created on 2017. 9. 6.

@author: callor
'''
from sys import *
from PyQt5.QtWidgets import *

# argv sys.argv 상수
app = QApplication(argv)
w = QWidget()
w.resize(500,500)
w.move(300,300)
w.setWindowTitle("QT 연습")
w.show()

exit(app.exec_())




