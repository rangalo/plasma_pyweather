#!/usr/bin/env python
 
from weatherInfo import WeatherInfo
 
class Weather:
    def __init__(self):
        self.location = "N/A"
        self.current_temperature = "N/A"
        self.current_condition = "N/A"
        self.current_humidity = "N/A"
        self.current_wind = "N/A"
        self._degree_symbol = unichr(176)
        
        self.fc_dl = []
        self.fc_conditions = []
        self.fc_low_high = []
    
    def _fromUStoSI(self,temp_in_f):
        return str(int( round ((int(temp_in_f) - 32) * 5 / 9.0, 0))) + " " + self._degree_symbol + "C"
 
    def _fromSItoUS(self,temp_in_c):
        return str(int(round((int(temp_in_c) * (9.0 / 5.0)) + 32, 0)) ) + " " + self._degree_symbol + "F"
        
    def _fromMilesToKms(self,dist_in_miles):
        return round(1.61 * dist_in_miles,1)
 
    def _fromKmsToMiles(self,dist_in_kms):
        return round(dist_in_kms/1.61, 1)
        
    def extractData(self,wi,reqUnit):
        self.location = wi.general["location"]
        
        xmlUnit = wi.general["unit"]
        if xmlUnit == "US":
            xmlUnit = "Imperial"
        else:
            xmlUnit = "Metric"
        
        if reqUnit == "Metric":
            self.current_temperature = wi.current_condition["temp_c"] + " " + self._degree_symbol + "C"
        elif reqUnit == "Imperial":
            self.current_temperature = wi.current_condition["temp_f"] + " " + self._degree_symbol + "F"
        else:
            self.current_temperature = "N/A"
        
        self.current_condition = wi.current_condition["condition"]
        self.current_humidity = wi.current_condition["humidity"]
        
        strWind = wi.current_condition["wind_condition"]
        print 'Str Wind: ' + strWind
        
        if not strWind:
            self.current_wind = "Wind: N/A"
        else:
            # Sometimes strWinds looks like "Wind: mph". It has the wrong format
            windCondition = "Wind: "
            strSpeed = "N/A"
            try:
                strWindArr = strWind.split()
                windCondition = strWindArr[0] + " " + strWindArr[1] + " " + strWindArr[2]
                speed = int(strWindArr[3])
            
                if reqUnit == xmlUnit:
                    strSpeed = str(speed) + " " + strWindArr[4]
                elif reqUnit == "Metric":
                    strSpeed = str(self._fromMilesToKms(speed)) + " kmph"
                elif reqUnit == "Imperial":
                    strSpeed = str(self._fromKmsToMiles(speed)) + " mph"
                else:
                    strSpeed = "N/A"
            except (IndexError):
                print "EXCEPTION: Wind string is in the wrong format: ",  strWind
            
            self.current_wind = windCondition +" "+ strSpeed
        
        fc_length = len(wi.forecast_conditions)
        
        # if no forecast available, put N/A everywhere
        if fc_length <= 1:
            for i in range(0,3):
                self.fc_dl.append("N/A")
                self.fc_conditions.append("N/A")
                self.fc_low_high.append("N/A")
            return
        
        
        for i in range(1,fc_length):
            self.fc_dl.append(wi.forecast_conditions[i]["day_of_week"])
            self.fc_conditions.append(wi.forecast_conditions[i]["condition"])
            if reqUnit == xmlUnit:
                if reqUnit == "Metric":
                    self.fc_low_high.append(wi.forecast_conditions[i]["low"] 
                                            + " " + self._degree_symbol + "C / " 
                                            + wi.forecast_conditions[i]["high"] 
                                            + " " + self._degree_symbol + "C")
                else:
                    self.fc_low_high.append(wi.forecast_conditions[i]["low"] 
                                            + " " + self._degree_symbol + "F / " 
                                            + wi.forecast_conditions[i]["high"] 
                                            + " " + self._degree_symbol + "F")
            elif reqUnit == "Metric":
                self.fc_low_high.append(self._fromUStoSI(wi.forecast_conditions[i]["low"])
                                        + " / "
                                        + self._fromUStoSI(wi.forecast_conditions[i]["high"]))
            elif reqUnit == "Imperial":
                self.fc_low_high.append(self._fromSItoUS(wi.forecast_conditions[i]["low"])
                                        + " / "
                                        + self._fromSItoUS(wi.forecast_conditions[i]["high"]))
            else:
                self.fc_low_high.append("N/A")
                
                
                    
        
    def show(self):
        print self.location
        print self.current_temperature
        print self.current_condition
        print self.current_humidity
        print self.current_wind
        
        print ""
        
        strprn = " "
        for d in self.fc_dl:
            strprn = strprn + d + " "
        print strprn
        
        print ""
        
        strprn = " "
        for c in self.fc_conditions:
            strprn = strprn + c + " "
        print strprn
        
        print " "
    
        strprn = " "
        for t in self.fc_low_high:
            strprn = strprn + t + " "
        print strprn
