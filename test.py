import random
import datetime,time
a = random.randint(1000,9999)
b = datetime.datetime.now()
c =time.mktime(datetime.datetime.now().timetuple()) 
random.seed(int(c))
a = random.randint(1000,9999)
print(a)
f'your secre is {a}'