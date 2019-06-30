"""
Creates a personal daily to-do list that 
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

class todo:
    def __init__(self,name,time,slot=''):
        # time is time taken and slow if the preferred slot
        self.time = time       #[hour,minute]
        self.slot = slot        #str, 24hr format
        self.name = name
    def __str__(self):
        return f"I am {self.name} and my timeslot is {self.slot}. I need {self.time} hours"


class schedule:
    def __init__(self,capacity = 0):
        self.capacity = capacity    #max number of todo
        self.columns =['Start','End', 'Item']
        self.schedule = pd.DataFrame(columns=self.columns)      #number of work hours
    def __str__(self):
        return f"I have {self.capacity} todos."
    def assign(self, todo):
        if self.capacity <= 10:    
            if len(todo.slot) == 0:      #no appt
            #Assigns somthing to do into the earliest possible timeslot            
                time = 800
                for i in range(len(self.schedule)):
                    endtime = time + timelist_to_int(todo.time)
                    if time <= int(self.schedule['Start'][i]) and endtime <= int(self.schedule['Start'][i]):
                    #append it
                        arr = pd.Series([int_to_timestr(time),int_to_timestr(endtime), todo.name],index = self.columns)
                        self.schedule = self.schedule.append(arr,ignore_index=True)
                        assigned = True
                        break
                    else: 
                        time = int(self.schedule['End'][i])

            else:       #add into the designated timeslot
                timing_start = todo.slot     #str format
                timing_end = str((int(timing_start) + timelist_to_int(todo.time)))
                arr = pd.Series([timing_start,timing_end, todo.name],index = self.columns)
                self.schedule = self.schedule.append(arr,ignore_index=True)
            #sort the dataframe
            self.schedule['Sorting'] = self.schedule['Start'].apply(lambda x: int(x))
            self.schedule = self.schedule.sort_values(by='Sorting')
            #add to capacity
            self.capacity+=1
        else:
            print("Sorry, your day is overload. Don't give yourself stress!")
    def print_schedule(self):
        print("This is your schedule of the day: \n")
        print(self.schedule[self.columns])

if __name__=='__main__':
    #print(int_to_timestr(100))

    daily = schedule()
    planning = True
    while planning:
        daily.print_schedule()
        choice = input("Do you still want to add something? y/n\n")
        if choice.lower() == 'y':
            list = input("What do you want to do\n")

            time = input("Enter time needed in this format: h,min\n")
            #fix the time to a proper format
            time = time.split(',')
            for i in range(len(time)):
                time[i] = int(time[i])
            print(time)
            
            start = input("What time does it begin? (Put 0 if it isn't fixed. Else put it in 24h format)\n")
            if start == '0':
                item = todo(list, time)
            else: 
                item = todo(list, time, start)
            daily.assign(item)
        elif choice.lower() == 'n':
            planning = False
        else:
            print("Please enter 'y' or 'n'")
    
    print("Here is your final schedule of the day:")
    print('\n')
    daily.print_schedule()
