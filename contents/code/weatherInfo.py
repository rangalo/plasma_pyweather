#!/usr/bin/env python
#######################################################
#
# @Author: Hardik Mehta <hard.mehta@gmail.com>
#
# @version: 0.1 basic script
#
########################################################

import sys, urllib, codecs
from xml.dom import minidom, Node

class WeatherInfo:
    def __init__(self,location="Munich,Germany"):

        #self._urlPart = "http://www.google.com/ig/api?weather="
        #self.url = "http://www.google.de/ig/api?weather=" + location
        self._urlPart = "http://www.google.com/ig/api?"

        self.general = {"location": "N/A", "unit":"Metric","city":"N/A"}
        self.current_condition = {"condition":"N/A","temp_c":"N/A","temp_f":"N/A","humidity":"N/A","wind_condition":"N/A"}
        self.forecast_conditions = [{"day_of_week":"N/A","low":"N/A","high":"N/A","condition":"N/A"}]    

    def parse(self,location="Munich,Germany"):
        #strUrl = self._urlPart + location
        strUrl = self._urlPart + urllib.urlencode({'weather' : location}) 
        #+'&' + urllib.urlencode({'hl':'it'})
         
        print strUrl
        
        try:
            sock = urllib.urlopen(strUrl)
        except IOError:
            self.general["location"] = "Connection Error"
            return
        
        #encoding = sock.headers['Content-type'].split('charset=')[1]
        #print encoding;
        
        #strUtf = strResponse.decode(encoding).encode('utf-8')
    
        #doc = minidom.parseString(strUtf)
        
        doc = minidom.parse(sock)
        nodes = doc.getElementsByTagName("forecast_information")

        # fetch general info
        if len(nodes) <> 0:
            node = nodes[0]
            self.general["location"] = (node.getElementsByTagName("postal_code")[0]).getAttribute("data")
            self.general["unit"] = (node.getElementsByTagName("unit_system")[0]).getAttribute("data")
            self.general["city"] = (node.getElementsByTagName("city")[0]).getAttribute("data")
            self.general["city"] = (node.getElementsByTagName("city")[0]).getAttribute("data")
        
        # fetch current conditions
        nodes = doc.getElementsByTagName("current_conditions")
        if len(nodes) <> 0:
            node = nodes[0]
            for key in self.current_condition.keys():
                self.current_condition[key] = (node.getElementsByTagName(key)[0]).getAttribute("data")
 
        # fetch forecast conditions
        fc = doc.getElementsByTagName("forecast_conditions")
        if len(fc) <> 0:
            fc_conditions = list()
            for elem in fc:
                condition = dict()
                for key in self.forecast_conditions[0].keys():
                    condition[key] = (elem.getElementsByTagName(key)[0]).getAttribute("data")
                fc_conditions.append(condition)
            self.forecast_conditions = fc_conditions
 
    def show(self):
        for k, v in self.general.iteritems():
            print k, v
        print "\n"
        for k, v in self.current_condition.iteritems():
            print k, v
        print "\n"
        for fc in self.forecast_conditions:
            for k, v in fc.iteritems():
                print k, v
            print ""
    


if __name__ == "__main__":
    wi = WeatherInfo()
    wi.show()
    wi.parse();
    print("-------------")
    wi.show()
