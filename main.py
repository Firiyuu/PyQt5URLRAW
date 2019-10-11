from PyQt5 import QtWidgets,QtCore
import sys
import os
import sip
from PyQt5.QtGui import QIcon, QPixmap
import datetime
import requests

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window,self).__init__()

        centwid=QtWidgets.QWidget()

        #Seting layouts
        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box1 =QtWidgets.QVBoxLayout()


  
        #In the window put a textEdit
        self.mylineEdit = QtWidgets.QLineEdit()
        self.textBrowser = QtWidgets.QTextBrowser()




        #Set window label
        self.welcome = QtWidgets.QLabel(centwid)
        self.welcome.setText("LARRY'S TEST")
        f = self.welcome.font()
        f.setPointSize(24) # sets the size to 27
        f.setBold(True)
        self.welcome.setFont(f)


        #REQUEST HEADER
        self.request = QtWidgets.QLabel(centwid)
        self.request.setText("STATUS: No request yet")
        f = self.request.font()
        f.setPointSize(15) # sets the size to 27
        f.setBold(True)
        self.request.setFont(f)


        #PUSH BUTTON
        self.send_request = QtWidgets.QPushButton('Send Request')
        self.send_request.setSizePolicy(
        QtWidgets.QSizePolicy.Preferred,
        QtWidgets.QSizePolicy.Expanding)


        #QTextBrowser
        self.resultText = QtWidgets.QTextBrowser(centwid)

        self.v_box1.addWidget(self.welcome)
        self.v_box1.addWidget(self.mylineEdit)
        self.v_box1.addWidget(self.send_request)


        self.v_box.addWidget(self.request)
        self.v_box.addWidget(self.resultText)


        lay=QtWidgets.QVBoxLayout()
        lay.addLayout(self.v_box1)
        lay.addLayout(self.v_box)
 

        centwid.setLayout(lay)
        self.send_request.clicked.connect(self.btn_click)
        self.setCentralWidget(centwid)
        self.show()


    def _request(self, url_):
        try:

            req = requests.get(url_)
            text_ = req.text
            self.resultText.setText(str(text_))

            return True
        except Exception as e:
            print(e)
            return False

    def btn_click(self):
      
        sender = self.sender()

        if self.mylineEdit.text() != '':
            if sender.text() == 'Send Request':
                    print(self.mylineEdit.text())
                    url_ = self.mylineEdit.text()
                    self._request(url_)
                    self.request.setText("STATUS: Request Made")
        else:
        	self.request.setText("STATUS: Request Failed")










# Create an application in QT using Python with a window that’s 600px tall by 800px wide. Then 
# in the window put a textEdit and a Push button. Then underneath put a QTextBrowser. The goal 
# of the program is to type a URL into thetextEdit, then when you click the pushButton a request 
# is made to get the contents of the response provided from the URL. By contents we mean the raw
# markup of a webpage or JSON of a web service.   


#Create an application in QT using Python 
app=QtWidgets.QApplication(sys.argv)

ex=window()
ex.setWindowTitle('Larry Test')

#With a window that’s 600px tall by 800px wide
ex.setFixedSize(640, 480)
sys.exit(app.exec_())
