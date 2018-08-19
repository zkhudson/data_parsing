# Data parsing using Python

**Files**

The app.py script is intended to parse the text file input001.txt.

This script takes the "input001.txt" file included and parses the appropiate data, based on the coloumn selection. Once a define threshold has been exceeded for a defined X number of times, the timestamp associated with when the threshold was exceeded are printed out.

The first line of the text file contains the parameters for column being analyzed (3), threshold (10), and threshold exceeded value (4).

Example:
When data in column 3 > 10, for 4 consecutive times the timestamp for when this starts is printed out to the console.

Note: I am also printing out the entire column and timestamp data set as a cross reference in the console. Only column 3 and 1 are currently functional.
