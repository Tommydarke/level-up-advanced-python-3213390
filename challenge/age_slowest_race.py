# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 day

from datetime import date,datetime

def mtn(x):
    months = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    a = x.strip()[:3].lower()
    try:
        ez = months[a]
        return ez
    except:
        raise ValueError('Not a month')
        pass



def numOfDays(DOB, Event_Date):
    #DOB=date(yyyy,mm,dd)
    DOByyyy=DOB[2]
    DOBmm=mtn(DOB[1])
    DOBdd=DOB[0]
    Evyyyy=Event_Date[2]
    Evmm=mtn(Event_Date[1])
    Evdd=Event_Date[0]
    Event_Date=date(int(Evyyyy),int(Evmm),int(Evdd))
    DOB=date(int(DOByyyy),int(DOBmm),int(DOBdd))
    Age_yrs = (Event_Date-DOB).days/365.25
    Age_days = round((Age_yrs - int(Age_yrs))*365.25)
    print(Age_days)
    Age_yrs = int(Age_yrs)
    Age_yrs_days = [Age_yrs, Age_days]
    return Age_yrs_days
"""
# Get month number from abbreviated month name
s_mn = list(calendar.month_abbr).index(sn)
print('Month Number:', s_mn)
"""

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    Rhines=[]
    races = get_data()
    millis=[]
    ages=[]
    for line in races:
        if line.find("Jennifer Rhines")==-1:
            pass
        else:
            #Age at race
            racedate = (line[56:68].strip()).split()
            dob = line[73:85].strip().split()
            age=numOfDays(dob, racedate)
            ages.append(age)
            #time achieved
            time = line[0:12].strip()
            if len(time)<6:
                dt_obj = datetime.strptime(time,'%M:%S')

            else:
                dt_obj = datetime.strptime(time,'%M:%S.%f')

            millisec = dt_obj.timestamp()/1000
            millis.append(millisec)
            Rhines.append(time)

    milli=millis.index(max(millis))
    slowTime = [Rhines[milli],ages[milli]]
    #print(milli)
    return slowTime
    

    
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    slowest = get_event_time(races)
    slowest = [str(slowest[1][0])+"y"+str(slowest[1][1])+"d", slowest[0]]
    #age = get_age(slowest)
    print(slowest)
    return slowest




