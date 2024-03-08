# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime
from statistics import mean 
 
def Average(lst): 
    return mean(lst) 

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    Rhines=[]
    races = get_data()
    for line in races:
        if line.find("Jennifer Rhines")==-1:
            pass
        else:
            Rhines.append(line[0:12].strip())
    return Rhines

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    times = get_rhines_times()
    millis = []
    for time in times:
        mins=int(time[0:2])*60000
        secs=int(time[3:5])*1000
        milli=time.split(".")
        if 2 > len(milli):
            millis.append(mins+secs)
        else:
            millis.append(mins+secs+int(milli[1]))
    average_millis=Average(millis)
    #print (average_millis)
    str_average_millis=convert(average_millis)
    return str_average_millis

def convert(millis):
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    mils = int(str(millis-(seconds*1000+minutes*60000))[0])

    string = ("%d:%d.%d" % (minutes, seconds, mils))

    return string

