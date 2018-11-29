from datetime import datetime, timedelta

from database.get import select_all_from_category, select_time_by_start_end, select_money_by_start_end, select_once_by_start_end
from times import days_hours_minutes

def calculate_points_by_range_date(start, end):
    categories = select_all_from_category()
    points = []
    for category in categories:
        if category[2] == 1: # time
            allTime = select_time_by_start_end(category[0], start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
            points.append(calculate_points_category(category, start, end, allTime, calculate_points_time))
        elif category[3] == 1: # money
            allMoneys = select_money_by_start_end(category[0], start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
            points.append(calculate_points_category(category, start, end, allMoneys, calculate_points_money))
        elif category[4] == 1: # once
            allOnces = select_once_by_start_end(category[0], start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
            points.append(calculate_points_category(category, start, end, allOnces, calculate_points_once))
    return combine_points_on_day(points)

def combine_points_on_day(points):
    pointsToReturn = [0] * len(points[0])
    for i in range(len(points[0])):
        for row in points:
            pointsToReturn[i] += row[i]
    return pointsToReturn

# gets a function to calculate the categories 
# i is used as the index for the points, and days is used to check the day in the date. 
def calculate_points_category(category, start, end, dataset, func):
    if end.day > start.day : # like start = 23/5 end = 30/5
        points = [0] * (end.day - start.day + 1)
        i = 0
        for day in range(start.day, end.day + 1):
            func(category, points, day, dataset, i)
            i += 1

    else : # like start = 30/5 end = 6/6 
        next_month = start.replace(day=28) + timedelta(days=4)  # this will never fail
        endMonth = next_month - timedelta(days=next_month.day)
        points = [0] * (end.day + endMonth.day - start.day + 1)           
        day = start.day 
        for i in range(len(points)):
            func(category, points, day, dataset, i)
            if day == endMonth.day:
                day = 0
            day += 1

    return [int(p) for p in points]

def calculate_points_time(category, points, day, allTimes, i):
    for time in allTimes:
        if time[2].day == day:
            if time[4] != None:
                hours, minutes = days_hours_minutes(time[4] - time[3])
                points[i] += category[5] * hours + (minutes/60) * category[5]
            else :
                points[i] += 0

def calculate_points_money(category, points, day, allMoneys, i):
        for money in allMoneys:
            if money[3].day == day:
                points[i] += category[5] * money[2]

# calculate all the point for a category where there is a once
def calculate_points_once(category, points, day, allOnces, i):
        for once in allOnces:
            if once[2].day == day:
                points[i] += category[5]
