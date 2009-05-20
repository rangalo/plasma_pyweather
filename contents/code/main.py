#######################################################
#
# @Author: Hardik Mehta <hard.mehta@gmail.com>
#
# @version: 0.1 basic script
#
########################################################

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript

class WeatherApplet(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)

    def init(self):
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.Square)
        

        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)


        self.layout = QGraphicsLinearLayout(Qt.Horizontal, self.applet)
        self.label = Plasma.Label(self.applet)
        self.label.setText("Hello world!")
        self.layout.addItem(self.label)
        self.setLayout(self.layout)
        self.resize(125,125)
        
        self.timer = QTimer()
        self.connect(self.timer,SIGNAL("timeout()"),self.checkWeather)
        self.timer.start(0.5*60000)

    def checkWeather(self):
        label = Plasma.Label(self.applet)
        label.setText("Temp: 23")
        self.label.setText("now temps")
        self.layout.addItem(label)
        self.setLayout(self.layout)
        self.update()

def CreateApplet(parent):
    return WeatherApplet(parent)

