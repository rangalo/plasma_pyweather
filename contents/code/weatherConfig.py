'''
Created on Aug 6, 2009

@author: hardik
'''

from PyQt4.QtGui import QWidget
from configForm_ui import Ui_Dialog

class WeatherConfig(QWidget,Ui_Dialog):
    '''
    classdocs
    '''


    def __init__(self,parent,defaultConfig = None):
        '''
        Constructor
        '''
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        if defaultConfig:
            self.txtCity.setText(defaultConfig['city'])
            self.txtCountry.setText(defaultConfig['country'])
            idx = self.cmbUnit.findText(defaultConfig['unit'])
            self.cmbUnit.setCurrentIndex(idx)
    
    def getLocation(self):
        strCity = str.strip(str(self.txtCity.text()))
        strCountry = str.strip(str(self.txtCountry.text()))
        return strCity + "," + strCountry
    
    def getCity(self):
        strCity = str.strip(str(self.txtCity.text()))
        return strCity
    
    def getCountry(self):
        strCountry = str.strip(str(self.txtCountry.text()))
        return strCountry
    
    def getUnit(self):
        strUnit = str.strip(str(self.cmbUnit.currentText()))
        return strUnit