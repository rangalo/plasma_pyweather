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
                               "thunder":"thunderstorms.svgz"
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
    
    def getMappedImageName(self,condition):
        lower_condition = condition.lower()
        
        if "rain" in lower_condition or "shower" in lower_condition or  "drizzle" in lower_condition :
            return self._getRainyImage()        
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
        