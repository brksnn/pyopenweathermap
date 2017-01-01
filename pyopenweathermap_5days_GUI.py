#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from pyopenweathermap_5days_class import PyOpenWeatherMap
from pyopenweathermap_GUI import Ui_Form

class Main(QtWidgets.QWidget):
    def __init__(self,Parent=None):
        super(Main, self).__init__(Parent)
        self.call_GUI()
        
    def call_GUI(self):
        self.Ui_Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Ui_Form)
        self.Ui_Form.show()
        self.ui.label_city.setText("WELCOME!...")
        self.ui.pushButton.clicked.connect(self.call_PyOpenWeatherMap)

    def call_PyOpenWeatherMap(self):
        self.API = self.ui.lineEditAPIKEY.text()
        self.location = self.ui.lineEditCity.text()
        self.limit = 5
        self.powm = PyOpenWeatherMap(self.API,self.location,self.limit)
        self.ui.label_city.setText(self.API)
        self.powm.Multi_Days_Forecasts()
        self.LOC = self.powm.Location_Data()
        self.WEA = self.powm.Weather_Data()
        self.powm.PRINT_DATA()
        self.set_GUI()
	
    def set_GUI(self):
        self.ui.label_city.setText(self.LOC[0] + ", " + self.LOC[3] + \
	" (Coord: " + "{:.3f}".format(self.LOC[1]) + ", " + "{:.3f}".format(self.LOC[2]) + ")")
        self.labelCOND = []
        self.labelTEMP = []
        self.labelHUMI = []
        self.labelWIND = []
        self.labelICON = []
        for i in range(self.limit):
            self.labelCOND.append(getattr(self.ui, "label_cond_%d" %(i+2)))
            self.labelCOND[i].setText(self.WEA[6][i])
            self.labelTEMP.append(getattr(self.ui, "label_temp_%d" %(i+2)))
            self.labelTEMP[i].setText(str(self.WEA[4][i]['day']) + "°C")
            self.labelHUMI.append(getattr(self.ui, "label_humidity_%d" %(i+2)))
            self.labelHUMI[i].setText(str(self.WEA[5][i]) + "%")
            self.labelWIND.append(getattr(self.ui, "label_wind_%d" %(i+2)))
            self.labelWIND[i].setText(str(self.WEA[0][i]['speed']) + " m/s")
            self.labelICON.append(getattr(self.ui, "label_icon%d" %(i+1)))
            if self.labelCOND[i].text() == "Clear":
                self.labelICON[i].setPixmap(QtGui.QPixmap("icons/7.png"))
            elif self.labelCOND[i].text() == "Rain":
                self.labelICON[i].setPixmap(QtGui.QPixmap("icons/4.png"))
            elif self.labelCOND[i].text() == "Snow":
                self.labelICON[i].setPixmap(QtGui.QPixmap("icons/3.png"))
            elif self.labelCOND[i].text() == "Clouds":
                self.labelICON[i].setPixmap(QtGui.QPixmap("icons/10.png"))

        """
        self.ui.label_cond_2.setText(self.WEA[6][0])
        self.ui.label_cond_3.setText(self.WEA[6][1])
        self.ui.label_cond_4.setText(self.WEA[6][2])
        self.ui.label_cond_5.setText(self.WEA[6][3])
        self.ui.label_cond_6.setText(self.WEA[6][4])
        self.ui.label_temp_2.setText(str(self.WEA[4][0]['day']))"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Main()
    sys.exit(app.exec_())
