from datetime import datetime, timedelta, timezone


#def getTime(start, end):




start = datetime.now() - timedelta(hours=1)
# start = start.strftime('%H:%M:%S')
end = datetime.today()#.strftime('%H:%M:%S')
#timezone = datetime.timezone

print(f'end: {end}')
print(f'start: {start}')
verschil = (end-start)

print(str(verschil))

