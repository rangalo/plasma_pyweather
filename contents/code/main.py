# -*- coding: utf-8 -*-
 
#######################################################
#
# @Author: Hardik Mehta <hard.mehta@gmail.com>
#
# @version: 0.1 basic script
#
########################################################
 
from PyQt4.QtCore import QTimer, QString, Qt, SIGNAL
from PyQt4.QtGui import QGraphicsGridLayout,QGraphicsLinearLayout
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
 
from weatherInfo import WeatherInfo
from conditionMapper import ConditionMapper
from weather import Weather
import images_rc
 
class WeatherApplet(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
        self._unit = "SI"
        self._image_prefix = ":/images/"
        
        self._img_width = 16
        self._img_height = 16
        self._big_img_width = 48
        self._big_img_height = 48
        self._fc_column_width = 100
        
    def init(self):
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
        
        
        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)
 
        # self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
        self.layout_main = QGraphicsGridLayout(self.applet)
        self.layout_top_left = QGraphicsLinearLayout(Qt.Vertical,self.layout_main)
        self.layout_bottom = QGraphicsGridLayout(self.layout_main)
        self.layout_bottom.setColumnMaximumWidth(0,self._fc_column_width)
        self.layout_bottom.setColumnMaximumWidth(1,self._fc_column_width)
        self.layout_bottom.setColumnMaximumWidth(2,self._fc_column_width)
        
        self.lb_location = Plasma.Label(self.applet)
        self.lb_temperature = Plasma.Label(self.applet)
        self.lb_condition = Plasma.Label(self.applet)
        self.lb_humidity = Plasma.Label(self.applet)
        self.lb_wind = Plasma.Label(self.applet)
        
        # create svg widgets for conditions
        self.svg_w_current = Plasma.SvgWidget(self.applet)
        self.svg_w_fc1 = Plasma.SvgWidget(self.applet)
        self.svg_w_fc2 = Plasma.SvgWidget(self.applet)
        self.svg_w_fc3 = Plasma.SvgWidget(self.applet)
        
# self.svg_w_fc1.resize(self._img_width,self._img_height)
        
 
        # create labels for forecast
        self.lb_temp_fc1 = Plasma.Label(self.applet)
        self.lb_temp_fc2 = Plasma.Label(self.applet)
        self.lb_temp_fc3 = Plasma.Label(self.applet)
        
 
        
        self.lb_day_fc1 = Plasma.Label(self.applet)
        self.lb_day_fc2 = Plasma.Label(self.applet)
        self.lb_day_fc3 = Plasma.Label(self.applet)
        
        
        # create images to display conditions
        self.svg_current = Plasma.Svg(self.applet)
        self.svg_fc1 = Plasma.Svg(self.applet)
        self.svg_fc2 = Plasma.Svg(self.applet)
        self.svg_fc3 = Plasma.Svg(self.applet)
        
        
       
        self.layout_main.addItem(self.layout_top_left,0,0)
        self.layout_main.addItem(self.svg_w_current,0,1)
        self.layout_main.addItem(self.layout_bottom,1,0,1,2,Qt.Alignment(Qt.AlignCenter))
        
        # add current conditions
        self.layout_top_left.addItem(self.lb_location)
        self.layout_top_left.addItem(self.lb_temperature)
        self.layout_top_left.addItem(self.lb_condition)
        self.layout_top_left.addItem(self.lb_humidity)
        self.layout_top_left.addItem(self.lb_wind)
 
        # add forecast labels for days
        self.layout_bottom.addItem(self.lb_day_fc1,0,0,1,1,Qt.Alignment(Qt.AlignHorizontal_Mask))
        self.layout_bottom.addItem(self.lb_day_fc2,0,1,1,1,Qt.Alignment(Qt.AlignHCenter))
        self.layout_bottom.addItem(self.lb_day_fc3,0,2,1,1,Qt.Alignment(Qt.AlignHCenter))
        # add forecast images
        self.layout_bottom.addItem(self.svg_w_fc1,1,0,1,1,Qt.Alignment(Qt.AlignLeft))
        self.layout_bottom.addItem(self.svg_w_fc2,1,1,1,1,Qt.Alignment(Qt.AlignLeft))
        self.layout_bottom.addItem(self.svg_w_fc3,1,2,1,1,Qt.Alignment(Qt.AlignLeft))
        # add forecast labels for temp
        self.layout_bottom.addItem(self.lb_temp_fc1,2,0,1,1,Qt.Alignment(Qt.AlignCenter))
        self.layout_bottom.addItem(self.lb_temp_fc2,2,1,1,1,Qt.Alignment(Qt.AlignCenter))
        self.layout_bottom.addItem(self.lb_temp_fc3,2,2,1,1,Qt.Alignment(Qt.AlignCenter))
        
        
        self.setLayout(self.layout_main)
        self.resize(375,375)
        
        self.checkWeather()
        
        self.timer = QTimer()
        self.connect(self.timer,SIGNAL("timeout()"),self.checkWeather)
        self.timer.start(0.5*60000)
 
  
    def checkWeather(self):
        wi = WeatherInfo()
        mapper = ConditionMapper()
        wi.parse()
        weather = Weather()
        weather.extractData(wi,self._unit)
        
 
        self.lb_location.setText("Location: " + weather.location)
            
            
        self.lb_temperature.setText(weather.current_temperature)
        self.lb_condition.setText("Condition: " + weather.current_condition)
        self.lb_humidity.setText(weather.current_humidity)
        self.lb_wind.setText(weather.current_wind)
        
        # current condition image
        self.svg_current.setImagePath(self._image_prefix+mapper.getMappedImageName(weather.current_condition))
        self.svg_current.resize(self._big_img_width,self._big_img_height)
        self.svg_w_current.setSvg(self.svg_current)
        
        # load forecast days
        fc_day = weather.fc_dl[0]
        #self.lb_day_fc1.setText("Tomorrow")
        self.lb_day_fc1.setText(fc_day)
        
        fc_day = weather.fc_dl[1]
        self.lb_day_fc2.setText(fc_day)
        
        fc_day = weather.fc_dl[2]
        self.lb_day_fc3.setText(fc_day)
        
        # load forecast images
        fc = weather.fc_conditions[0]
        print fc
        self.svg_fc1.setImagePath(self._image_prefix + mapper.getMappedImageName(fc))
        self.svg_fc1.resize(self._img_width,self._img_height)
        self.svg_w_fc1.setSvg(self.svg_fc1)
        
        fc = weather.fc_conditions[1]
        print fc
        self.svg_fc2.setImagePath(self._image_prefix + mapper.getMappedImageName(fc))
        self.svg_fc2.resize(self._img_width,self._img_height)
        self.svg_w_fc2.setSvg(self.svg_fc2)
        
        fc = weather.fc_conditions[2]
        print fc
        self.svg_fc3.setImagePath(self._image_prefix + mapper.getMappedImageName(fc))
        self.svg_fc3.resize(self._img_width,self._img_height)
        self.svg_w_fc3.setSvg(self.svg_fc3)
        
        
        
        self.lb_temp_fc1.setText(weather.fc_low_high[0])
        self.lb_temp_fc2.setText(weather.fc_low_high[1])
        self.lb_temp_fc3.setText(weather.fc_low_high[2])
 
        # self.layout.addItem(label)
        # self.setLayout(self.layout)
        self.update()
 
def CreateApplet(parent):
    return WeatherApplet(parent)
 