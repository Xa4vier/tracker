from datetime import datetime, timedelta

dt = datetime.today()
start = dt - timedelta(days=dt.weekday - 1)
end = start + timedelta(days=6)
mondayLastWeek = start - timedelta(weeks=1)

print(f"{start.strftime('%d-%m-%Y')} - {end.strftime('%d-%m-%Y')} - {mondayLastWeek.strftime('%d-%m-%Y')}")
