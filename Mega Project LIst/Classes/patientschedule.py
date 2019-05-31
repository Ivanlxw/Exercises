"""
Create a patient class and a doctor class. 
Have a doctor that can handle multiple patients and setup a scheduling program 
where a doctor can only handle 16 patients during an 8 hr work day.
"""
import numpy as np
import pandas as pd

def timelist_to_int(list):
    if list[0] <24 and list[1]<60:
        return list[0]*100+list[1]
    else:
        return f'Invalid timelist'

def int_to_timestr(n):
    return f"{n:04}"

class Patient:
    def __init__(self,name,time,slot=''):
        # time is time taken and slow if the preferred slot
        self.time = time       #[hour,minute]
        self.slot = slot        #str, 24hr format
        self.name = name
    def __str__(self):
        return f"I am {self.name} and my timeslot is {self.slot}. I need {self.time} hours"


class Doctor:
    def __init__(self,capacity = 0):
        self.capacity = capacity    #max number of patients
        self.columns =['Start','End', 'Patient']
        self.schedule = pd.DataFrame(columns=self.columns)      #number of work hours
    def __str__(self):
        return f"I have {self.capacity} patients."
    def assign(self, Patient):    
        #Assigns a patient into the earliest possible timeslot            
        if len(Patient.slot) == 0:      #no appt
            time = 800
            for i in range(len(self.schedule)):
                endtime = time + timelist_to_int(Patient.time)
                if time <= int(self.schedule['Start'][i]) and endtime <= int(self.schedule['Start'][i]):
                #append it
                    arr = pd.Series([int_to_timestr(time),int_to_timestr(endtime), Patient.name],index = self.columns)
                    self.schedule = self.schedule.append(arr,ignore_index=True)
                    assigned = True
                    break
                else: 
                    time = int(self.schedule['End'][i])

        else:   
            timing_start = Patient.slot     #str format
            timing_end = str((int(timing_start) + timelist_to_int(Patient.time)))
            arr = pd.Series([timing_start,timing_end, Patient.name],index = self.columns)
            self.schedule = self.schedule.append(arr,ignore_index=True)
        #sort the dataframe
        self.schedule['Sorting'] = self.schedule['Start'].apply(lambda x: int(x))
        self.schedule = self.schedule.sort_values(by='Sorting')
        #add to capacity
        self.capacity+=1
    def print_schedule(self):
        print("Here is your timetable of the day: \n")
        print(self.schedule[self.columns])

if __name__=='__main__':
    #print(int_to_timestr(100))

    doc = Doctor()
    pat = Patient('Ivan', [2,0], '1000')
    pat2 = Patient('John', [1,0],'1500')
    pat3 = Patient('Mark',[3,0])
    doc.assign(pat)
    doc.assign(pat2)
    doc.assign(pat3)
    doc.print_schedule()