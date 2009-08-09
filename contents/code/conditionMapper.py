'''
Created on Jul 25, 2009

@author: hardik
'''

class ConditionMapper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._condition_map = {"rain":"showers.svgz",
                               "sunny":"sunny.svgz",
                               "na":"not-available.svgz",
                               "cloudy":"cloudy.svgz",
                               "snow":"snow.svgz",
                               "thunder":"thunderstorms.svgz",
                               "haze" : "haze.svgz",
                               "drizzle" : "drizzle.svgz",
                               "windy" : "windy.svgz"
                               }
        
    def _getRainyImage(self):
        return self._condition_map["rain"]
    
    def _getSunnyImage(self):
        return self._condition_map["sunny"]
    
    def _getCloudyImage(self):
        return self._condition_map["cloudy"]
    
    def _getSnowyImage(self):
        return self._condition_map["snow"]
    
    def _getNAImage(self):
        return self._condition_map["na"]
    
    def _getThunderImage(self):
        return self._condition_map["thunder"]
    def _getHazeImage(self):
        return self._condition_map["haze"]
    def _getWindyImage(self):
        return self._condition_map["windy"]
    def _getDrizzleImage(self):
        return self._condition_map["drizzle"]
    
    
    def getMappedImageName(self,condition):
        lower_condition = condition.lower()
        
        if "rain" in lower_condition or "shower" in lower_condition:
            return self._getRainyImage()        
        elif "drizzle" in lower_condition:
            return self._getDrizzleImage()
        elif "haze" in lower_condition:
            return self._getHazeImage()
        elif "windy" in lower_condition:
            return self._getWindyImage()
        elif "fair" in lower_condition or "sunny" in lower_condition or "clear" in lower_condition:
            return self._getSunnyImage()
        elif "snow" in lower_condition or "flurries" in lower_condition or "wintry" in lower_condition:
            return self._getSnowyImage()
        elif "thunder" in lower_condition or "storm" in lower_condition:
            return self._getThunderImage()
        elif "cloud" in lower_condition:
            return self._getCloudyImage()
        else:
            return self._getNAImage() 
        