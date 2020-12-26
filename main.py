import time
import datetime
import os
import sys

#working hours are pre-defined as 9am to 6pm : set your hours according your shift hrs
try:
    while True:
        now = datetime.datetime.now()
        print(now)
        tminus9 = now.replace(hour=9, minute=0, second=0, microsecond=0) # 24hr format
        tminus18 = now.replace(hour=18, minute=0, second=0, microsecond=0) #24hr format
        if now >= tminus9 and now <=tminus18:
           print('Alive Feature started')
           for i in range(0,3):
               file1 = open("myfile.txt", "w") 
               file1.write('RandomText') 
               file1.close()              
               time.sleep(300)
        else:
            print(f'Off Working hours:{now}')
            print('\n feature stopped')
            os.remove("myfile.txt")
            print('file rmoved')
            break

        


except Exception as err:
    print(err.__context__)
    print()
    print(err.__cause__)

