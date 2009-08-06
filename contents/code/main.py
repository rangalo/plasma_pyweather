# -*- coding: utf-8 -*-
 
#######################################################
#
# @Author: Hardik Mehta <hard.mehta@gmail.com>
#
# @version: 0.1 basic script
#
########################################################
 
from PyQt4.QtCore import QTimer, QString, Qt, SIGNAL, QRect
from PyQt4.QtGui import QPainter, QStyleOptionGraphicsItem, QBrush, QColor, QFont
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
 
from weatherInfo import WeatherInfo
from conditionMapper import ConditionMapper
from weather import Weather
import images_rc
 
class WeatherApplet(plasmascript.Applet):
    def __init__(self,parent,args=None):
        
        # as it looks ugly, we will get rid of widgets
        
        plasmascript.Applet.__init__(self,parent)
        self._unit = "SI"
        self._location = "Munich,Germany"
        self._weather = Weather()
        self._mapper = ConditionMapper()        
        self._image_prefix = ":/images/"
        
        self._img_width = 16
        self._img_height = 16
        self._big_img_width = 48
        self._big_img_height = 48
        self._fc_column_width = 100
        
        
    def init(self):
        self.setHasConfigurationInterface(False)
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
        
        self.resize(375,375)
        
        self.checkWeather()
        
        self.timer = QTimer()
        self.connect(self.timer,SIGNAL("timeout()"),self.checkWeather)
        self.timer.start(0.5*60000)
 
  
    def checkWeather(self):
        wi = WeatherInfo()
        wi.parse(self._location)
        
        newWeather = Weather()
        newWeather.extractData(wi,self._unit)
        self._weather = newWeather 
      
        self.update()

    def paintInterface(self,painter,option,contentRect):
        # define some parameters
        padding = contentRect.height()/50
        fontSize = contentRect.height()/35
        
        txtFieldWidth = contentRect.width()/2 - 2*padding
        txtFieldHeight = contentRect.height()/20
        
        
        current_img_width = contentRect.height()/3
        current_img_height = contentRect.height()/3
        
        whiteBrush10p = QBrush(QColor.fromCmyk(0,0,0,0,5))
        whiteBrush20p = QBrush(QColor.fromCmyk(0,0,0,0,40))
        
        fcRectWidth = (contentRect.width() - 4 * padding)/3
        fcRectHeight = current_img_height + 2 * padding + 2 * txtFieldHeight
        
        
        
        textColor = Plasma.Theme.defaultTheme().color(Plasma.Theme.TextColor)
        bgColor = Plasma.Theme.defaultTheme().color(Plasma.Theme.BackgroundColor)
        textFont = Plasma.Theme.defaultTheme().font(Plasma.Theme.DefaultFont)
        
        # create text rects
        rect_text_location = QRect(contentRect.left() + padding ,contentRect.top() + 2*padding, txtFieldWidth, txtFieldHeight)
        rect_text_temperature = QRect(contentRect.left() + padding ,contentRect.top() + 3* padding + 1 * txtFieldHeight , txtFieldWidth, txtFieldHeight)
        rect_text_condition = QRect(contentRect.left() + padding ,contentRect.top() + 4* padding + 2 * txtFieldHeight , txtFieldWidth, txtFieldHeight)
        rect_text_humidity = QRect(contentRect.left() + padding ,contentRect.top() + 5* padding + 3 * txtFieldHeight , txtFieldWidth, txtFieldHeight)
        rect_text_wind = QRect(contentRect.left() + padding , contentRect.top() + 6* padding + 4 * txtFieldHeight , txtFieldWidth, txtFieldHeight)
        
        painter.save()
        
        painter.setPen(textColor)
        textFont.setPointSize(fontSize)
        painter.setFont(textFont)
        
        painter.drawText(rect_text_location,Qt.Alignment(Qt.AlignLeft),"Location: " + self._weather.location)
        painter.drawText(rect_text_temperature,Qt.Alignment(Qt.AlignLeft),"Temperature: " + self._weather.current_temperature)
        painter.drawText(rect_text_condition,Qt.Alignment(Qt.AlignLeft),"Condition: " + self._weather.current_condition)
        painter.drawText(rect_text_humidity,Qt.Alignment(Qt.AlignLeft),self._weather.current_humidity)
        painter.drawText(rect_text_wind,Qt.Alignment(Qt.AlignLeft),self._weather.current_wind)
        
        svg_current = Plasma.Svg()
        svg_current.setImagePath(self._image_prefix + self._mapper.getMappedImageName(self._weather.current_condition))
        svg_current.resize(current_img_width,current_img_height)
        xOffset = contentRect.width()/2 + contentRect.width()/2 - current_img_width
        yOffset = contentRect.top() + 2 * padding
        svg_current.paint(painter,contentRect.left() + xOffset, yOffset)
        
        # create forecast blocks
        fc_rect1 = QRect(contentRect.left() + padding, contentRect.bottom() - fcRectHeight, fcRectWidth, fcRectHeight)
        fc_rect2 = QRect(fc_rect1.right() + padding, contentRect.bottom() - fcRectHeight, fcRectWidth, fcRectHeight)
        fc_rect3 = QRect(fc_rect2.right() + padding, contentRect.bottom() - fcRectHeight, fcRectWidth, fcRectHeight)
        
        painter.setPen(bgColor)
        painter.setBrush(whiteBrush20p)
        painter.drawRect(fc_rect1)
        painter.drawRect(fc_rect3)
        painter.setBrush(whiteBrush10p)
        painter.drawRect(fc_rect2)
        
        # text rects for day list
        rect_text_dl1 = QRect(fc_rect1.left(),fc_rect1.top() + padding,fcRectWidth,txtFieldHeight)
        rect_text_dl2 = QRect(fc_rect2.left(),fc_rect2.top() + padding,fcRectWidth,txtFieldHeight)
        rect_text_dl3 = QRect(fc_rect3.left(),fc_rect3.top() + padding,fcRectWidth,txtFieldHeight)
        
        painter.setPen(textColor)
        painter.drawText(rect_text_dl1,Qt.Alignment(Qt.AlignCenter),self._weather.fc_dl[0])
        painter.drawText(rect_text_dl2,Qt.Alignment(Qt.AlignCenter),self._weather.fc_dl[1])
        painter.drawText(rect_text_dl3,Qt.Alignment(Qt.AlignCenter),self._weather.fc_dl[2])
        
        fc_svg1 = Plasma.Svg()
        fc_svg2 = Plasma.Svg()
        fc_svg3 = Plasma.Svg()
        
        fc_svg1.setImagePath(self._image_prefix + self._mapper.getMappedImageName(self._weather.fc_conditions[0]))
        fc_svg2.setImagePath(self._image_prefix + self._mapper.getMappedImageName(self._weather.fc_conditions[1]))
        fc_svg3.setImagePath(self._image_prefix + self._mapper.getMappedImageName(self._weather.fc_conditions[2]))
        
        fc_svg1.resize(current_img_width,current_img_height)
        fc_svg2.resize(current_img_width,current_img_height)
        fc_svg3.resize(current_img_width,current_img_height)
        
        xOffSet = fc_rect1.left() + (fc_rect1.width() - current_img_width)/2
        fc_svg1.paint(painter,xOffSet, fc_rect1.top() + txtFieldHeight + 2* padding)
        xOffSet = fc_rect2.left() + (fc_rect2.width() - current_img_width)/2
        fc_svg2.paint(painter,xOffSet, fc_rect2.top() + txtFieldHeight + 2* padding)
        xOffSet = fc_rect3.left() + (fc_rect3.width() - current_img_width)/2
        fc_svg3.paint(painter,xOffSet, fc_rect3.top() + txtFieldHeight + 2* padding)
        
        # text rects for high/low temperatures
        
        rect_text_temp1 = QRect(fc_rect1.left(),fc_rect1.bottom() - 3 * padding,fcRectWidth,txtFieldHeight)
        rect_text_temp2 = QRect(fc_rect2.left(),fc_rect2.bottom() - 3 * padding,fcRectWidth,txtFieldHeight)
        rect_text_temp3 = QRect(fc_rect3.left(),fc_rect3.bottom() - 3 * padding,fcRectWidth,txtFieldHeight)
        painter.setPen(textColor)
        painter.drawText(rect_text_temp1,Qt.Alignment(Qt.AlignCenter),self._weather.fc_low_high[0])
        painter.drawText(rect_text_temp2,Qt.Alignment(Qt.AlignCenter),self._weather.fc_low_high[1])
        painter.drawText(rect_text_temp3,Qt.Alignment(Qt.AlignCenter),self._weather.fc_low_high[2])
        
        
        painter.restore()
        
        
 
def CreateApplet(parent):
    return WeatherApplet(parent)
 