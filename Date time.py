import datetime
data=datetime.datetime.now()
data=str(data).split()
date=data[0]
time=data[1]
time=time.split('.')
time=time[0]
print(f'Date:{date} Time:{time}')
