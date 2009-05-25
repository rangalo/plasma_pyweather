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
from weatherInfo import WeatherInfo

class WeatherApplet(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)

    def init(self):
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.Square)
        

        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)


        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
        self.lb_location  = Plasma.Label(self.applet)
        self.lb_temperature  = Plasma.Label(self.applet)
        self.lb_condition  = Plasma.Label(self.applet)
        self.lb_humidity  = Plasma.Label(self.applet)
        self.lb_wind  = Plasma.Label(self.applet)

        self.layout.addItem(self.lb_location)
        self.layout.addItem(self.lb_temperature)
        self.layout.addItem(self.lb_condition)
        self.layout.addItem(self.lb_humidity)
        self.layout.addItem(self.lb_wind)

        self.setLayout(self.layout)
        self.resize(250,200)
        
        self.timer = QTimer()
        self.connect(self.timer,SIGNAL("timeout()"),self.checkWeather)
        self.timer.start(0.5*60000)

    def checkWeather(self):
        wi = WeatherInfo()
        wi.parse()

        self.lb_location.setText("Location: " + wi.general["location"])
        self.lb_temperature.setText("Temperature: " + wi.current_condition["temp_c"])
        self.lb_condition.setText("Condition: " + wi.current_condition["condition"])
        self.lb_humidity.setText(wi.current_condition["humidity"])
        self.lb_wind.setText(wi.current_condition["wind_condition"])
        

        # self.layout.addItem(label)
        # self.setLayout(self.layout)
        self.update()

def CreateApplet(parent):
    return WeatherApplet(parent)

