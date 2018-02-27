### FUNCTIONS TO MANIPULATE DATA

# Edit timeStamp to be ISO-8601 formated
# Convert time from US/Pacific time to US/Eastern
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



