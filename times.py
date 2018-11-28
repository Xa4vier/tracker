from datetime import datetime, timedelta

def days_hours_minutes(td):
    return td.seconds//3600, (td.seconds//60) % 60 # hours, minutes

def start_end_this_week():
    dt = datetime.today()
    start = dt - timedelta(days=dt.weekday())
    return start, start + timedelta(days=6)

def start_end_last_week(start):
    start -= timedelta(days=2)
    start -= timedelta(days=start.weekday())
    return start , start + timedelta(days=6)   

def start_end_next_week(end):
    end += timedelta(days=2)
    start = end - timedelta(days=end.weekday())
    return start, start + timedelta(days=6)

def start_end_this_month():
    dt = datetime.today()        
    start = dt - timedelta(days=dt.day - 1)
    next_month = start.replace(day=28) + timedelta(days=4)
    return start, next_month - timedelta(days=next_month.day)

def start_end_next_month(end):
    end += timedelta(days=2)
    start = end - timedelta(days=end.day - 1)
    next_month = end.replace(day=28) + timedelta(days=4)
    return start, next_month - timedelta(days=next_month.day)

def start_end_last_month(start):
    end = start.replace(day=1) - timedelta(days=1)
    return end - timedelta(days=end.day - 1), end