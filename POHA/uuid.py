import os
import datetime

now=datetime.datetime.now()

timestring=str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"+str(now.time())

print("UUID :",timestring)

