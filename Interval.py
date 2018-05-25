#   class to store a starting date, starting time, end date and end time for specific events
#   for easy comparison the 'start' and 'end' attributes give an integer presentation of the
#   start and end datetimes respectively

import datetime


class Interval:
    def __init__(self, startDate: str, startTime: str, endDate: str, endTime: str):

        if startDate == '':
            #   if an empty startDate is supplied, set all values to 0
            splitDate = ['0000', '00', '00']
        else:
            #   separate year, month and day
            splitDate = startDate.split('-')

        if startTime == '':
            #   if an empty startTime is supplied, set all values to 0
            splitTime = ['00', '00', '00']
        else:
            #   separate hours, minutes and seconds
            splitTime = startTime.split(':')

        #   create an integer with the following format: yyyymmddHHMMSS
        self.start = int(splitDate[2] + splitDate[1] + splitDate[0] + splitTime[0] + splitTime[1] + splitTime[2])

        #   repeat above process for 'end' variable
        if endDate == '':
            splitDate = ['0000', '00', '00']
        else:
            #   separate year, month and day
            splitDate = endDate.split('-')

        if endTime == '':
            splitTime = ['00', '00', '00']
        else:
            #   separate hours, minutes and seconds
            splitTime = endTime.split(':')

        self.end = int(splitDate[2] + splitDate[1] + splitDate[0] + splitTime[0] + splitTime[1] + splitTime[2])

        #   set other class attributes
        self.startDate = startDate
        self.endDate = endDate
        self.startTime = startTime
        self.endTime = endTime

    #   the 'hourly' method acts as a second constructor to load data from
    #   the KNMI dataset to allow TrafficNodes and WeatherNodes to both use
    #   the Interval class for easy comparison when making edges
    @classmethod
    def hourly(cls, date: str, hour: str):
        #   load the supplied date and hourly period into a datetime object
        #   in the KNMI dataset, if the hourly period is set to 2 it means
        #   from 01:00:00 to 02:00:00
        #   therefore hour-1 is loaded into the datetime object to get the
        #   startDateTime
        startDateTime = datetime.datetime(int(date[:4]), int(date[4:6]), int(date[-2:]), int(hour) - 1, 0, 0)

        #   the function strftime simply formats the information in the
        #   datetime object to a specific layout in this case e.g.
        #   yyyy-mm-dd for a date and HH:MM:SS for time
        startDate = startDateTime.strftime("%y-%m-%d")
        startTime = startDateTime.strftime("%H:%M:%S")

        #   add an hour to the startDateTime object so it now holds
        #   the time and date at the end of the interval
        startDateTime += datetime.timedelta(hours=1)

        endDate = startDateTime.strftime("%y-%m-%d")
        endTime = startDateTime.strftime("%H:%M:%S")

        #   pass the created variables to the constructor
        return cls(startDate, startTime, endDate, endTime)

    def __str__(self):
        return str(self.startDate) + ', ' + str(self.startTime) + ', ' + str(self.endDate) + ', ' + str(
            self.endTime)
