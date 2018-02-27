### FUNCTIONS TO MANIPULATE DATA

# Edit timeStamp to be ISO-8601 formated and convert time from US/Pacific time to US/Eastern
def timeStampUpdates(timeStamp):
  timeList = timeStamp.split(' ')
  date = timeList[0].split('/')
  time = timeList[1].split(':')
  ampm = timeList[2]  
  # setup time first so date can be adjusted after EST update
  hour = int(time[0])
  # covert PST EST
  hour = hour + 3
  if (hour > 24):
    date[0] = date[0] + 1
    hour = hour - 24
  # setup time to 24hr hours
  if ampm == ('pm' or 'PM'):
    hour = hour + 12
  #setpu date
  year = '20' + date[2]
  month = date[1]
  if len(month) < 2:
    month = '0' + month
  day = date[0]
  if len(day) < 2:
    day = '0' + day
  # final setup
  time = str(hour) + ':' + time[1] + ':' + time[2] + ' EST'
  date = year + '-' + month + '-' + day
  return (date + ' ' + time)
  # TODO: find a method that formats time in ISO-8601 


# Edit ZIPcode to be formated with 5 digits
def zipCodeUpdates(ZIP):
  if len(ZIP) < 5:
    while len(ZIP) < 5:
      ZIP = '0' + ZIP
  elif len(ZIP) > 5:
      ZIP = ZIP[0:4]
  return ZIP


# edit fullName column to be all uppercase
def fullNameUpdate(name):
  name = name.upper()
  return (name)
  # TODO: manage the non-English names

"""
I compared the Address given to the one my code create using diff to check for commas. 
TODO: create function to confirm Address column still has commas in right place

"""

# update format of foo and bar to floating point seconds
# update totalDuration to the sum of foo and bar after reformated
def durationUpdate(foo, bar, total):
  foo = foo.split(':')
  bar = bar.split(':')

  fooSec = (float(foo[0]) * 3600) + (float(foo[1]) * 60) + float(foo[2])
  barSec = (float(bar[0]) * 3600) + (float(bar[1]) * 60) + float(bar[2])
  dur = [repr(fooSec), repr(barSec), repr((fooSec + barSec))]
  return dur

# make the first and lest index of strings in Address and Notes a "
  # to return strings on the end for now since I didnt have time to
  # look into the details of return csv files.
def makeStringUpdate(string):
  return '"' + string + '"' 

### RUNNUNG FUNCTIONS

# separating headers from file saved as list of string
headers = sys.stdin.readline()
headers = headers[:-2]
headers = headers.split(',')


# add data from csv file to list
data = []
for row in sys.stdin:
  for column in csv.reader([row], skipinitialspace=True):
    data.append(column)

# run functions on data to update column values
for column in data:
  column[0] = timeStampUpdates(column[0])
  column[1] = makeStringUpdate(column[1])
  column[2] = zipCodeUpdates(column[2])
  column[3] = fullNameUpdate(column[3])
  duration = durationUpdate(column[4], column[5], column[6])
  column[4] = duration[0]
  column[5] = duration[1]
  column[6] = duration[2]
  column[7] = makeStringUpdate(column[7])

# add headers to data and return it as stdout string
data.insert(0, headers)
for row in data:
  print ','.join(row)

"""

IF MORE TIME: find a way to return a csv file instead of a string
* look into csv.writer

"""


