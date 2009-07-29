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
        return str( round ((int(temp_in_f) - 32) * 5 / 9.0, 1)) + " " + self._degree_symbol + "C"
 
    def _fromSItoUS(self,temp_in_c):
        return str(round((int(temp_in_c) * 9 / 5.0) + 32, 2) ) + " " + self._degree_symbol + "F"
        
    def _fromMilesToKms(self,dist_in_miles):
        return round(1.61 * dist_in_miles,1)
 
    def _fromKmsToMiles(self,dist_in_kms):
        return round(dist_in_kms/1.61, 1)
        
    def extractData(self,wi,reqUnit):
        self.location = wi.general["location"]
        
        xmlUnit = wi.general["unit"]
        
        if reqUnit == "SI":
            self.current_temperature = wi.current_condition["temp_c"] + " " + self._degree_symbol + "C"
        elif reqUnit == "US":
            self.current_temperature = wi.current_condition["temp_f"] + " " + self._degree_symbol + "F"
        else:
            self.current_temperature = "N/A"
        
        self.current_condition = wi.current_condition["condition"]
        self.current_humidity = wi.current_condition["humidity"]
        
        strWind = wi.current_condition["wind_condition"]
        strWindArr = strWind.split()
        windCondition = strWindArr[0] + " " + strWindArr[1] + " " + strWindArr[2]
        speed = int(strWindArr[3])
        
        if reqUnit == xmlUnit:
            strSpeed = str(speed) + " " + strWindArr[4]
        elif reqUnit == "SI":
            strSpeed = str(self._fromMilesToKms(speed)) + " kmph"
        elif reqUnit == "US":
            strSpeed = str(seelf._fromKmsToMiles(speed)) + " mph"
        else:
            strSpeed = "N/A"
        
        self.current_wind = windCondition +" "+ strSpeed
        
        # prepare the day list
        for i in [1,2,3]:
            self.fc_dl.append(wi.forecast_conditions[i]["day_of_week"])
        
        # read the conditions
        for i in [1,2,3]:
            self.fc_conditions.append(wi.forecast_conditions[i]["condition"])
        
        # prepare the string with low/high temperature
        if reqUnit == xmlUnit:
            if reqUnit == "SI":
                for i in [1,2,3]:
                    self.fc_low_high.append(wi.forecast_conditions[i]["low"]
                                            + " " +self._degree_symbol + "C / "
                                            + wi.forecast_conditions[i]["high"]
                                            + " " +self._degree_symbol +"C")
            else:
                for i in [1,2,3]:
                    self.fc_low_high.append(wi.forecast_conditions[i]["low"]
                                            + " " +self._degree_symbol + "F / "
                                            + wi.forecast_conditions[i]["high"]
                                            + " " +self._degree_symbol +"F")
        elif reqUnit == "SI":
            for i in [1,2,3]:
                self.fc_low_high.append(self._fromUStoSI(wi.forecast_conditions[i]["low"])
                                        + " / "
                                        + self._fromUStoSI(wi.forecast_conditions[i]["high"]))
        elif reqUnit == "US":
            for i in [1,2,3]:
                self.fc_low_high.append(self._fromSItoUS(wi.forecast_conditions[i]["low"])
                                        + " / "
                                        + self._fromSItoUS(wi.forecast_conditions[i]["high"]))
        else:
            for i in [1,2,3]:
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