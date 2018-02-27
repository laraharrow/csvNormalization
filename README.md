# CSV-Normalization


## Given problem: CSV-normalization
Please write a tool that reads a CSV formatted file on stdin and emits a normalized CSV formatted file on stdout. Normalized, in this case, means:

###### * The entire CSV is in the UTF-8 character set.
###### * The Timestamp column should be formatted in ISO-8601 format.
###### * The Timestamp column should be assumed to be in US/Pacific time; please convert it to US/Eastern.
###### * All ZIP codes should be formatted as 5 digits. If there are less than 5 digits, assume 0 as the prefix.
###### * All name columns should be converted to uppercase. There will be non-English names.
###### * The Address column should be passed through as is, except for Unicode validation. Please note there are commas in the Address field; your CSV parsing will need to take that into account. Commas will only be present inside a quoted string.
###### * The columns 'FooDuration' and 'BarDuration' are in HH:MM:SS.MS format (where MS is milliseconds); please convert them to a floating point seconds format.
###### * The column "TotalDuration" is filled with garbage data. For each row, please replace the value of TotalDuration with the sum of FooDuration and BarDuration.
###### * The column "Notes" is free form text input by end-users; please do not perform any transformations on this column. If there are invalid UTF-8 characters, please replace them with the Unicode Replacement Character.


You can assume that the input document is in UTF-8 and that any times that are missing timezone information are in US/Pacific.

## Content:

> sample.csv - given file to use as input
> sample-with-broken-utf8.csv - given file to use as input
> CSV.py - file with my code
> README.md 


## Comments:

 Requirement:
Python 2.7.10


###### Clone this repo to your machine
```
	git clone https://github.com/laraismael1/csvNormalization.git
```
###### Runnignthe script:

```
	python CSV.py < stdin.csv > stdout.csv
```

Where:

- CSV.py is the file that contains my Python code
- stdin.csv is the file you are passing as input
- stdout.csv is the file that will contain the output (you can pass a existent file or just a file name and the program creates a new file on the directure to store the output)


## Disclosure:

* I'm a JavaScript developer but after some research it seemed reasonable to write this program in Python.

* This Terminal program was writen in 4 hours as it was one of the requirements so in the code there are a few thigs I would like to add to the code that are now as comments.

