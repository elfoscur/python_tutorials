#https://www.py4e.com/lectures/Py4Inf-11-Regex-Guide.pdf
import re #import the regular expression library

log = '''This is a simple log file to log the values of the variables in a program.
It has a timestamp and the variables with an equal sign

20180113 16:55:01 - a=10 b=20 c=30
20180113 16:55:02 - a=1 b=2 c=33
20180113 16:55:03 - a=13 b=22 c=33 d=20
Memory usage 10%
20180113 16:55:04 - a=13 b=22 c=33 d=20

20180115 01:55:01 - a=10
20180115 01:55:02 - a=1 b=2
Don't extract this! b=20
'''


#regular expressions
for ln in log.splitlines(): #iterate the lines of the string
    print(ln)
    #if re.search('^2018.* 01.*',ln): #search for the logs in 2018 at 01 am
    # FINDALL RETURN A LIST!
    #    print(re.findall('^2018.* 01.*',ln))

         #print(re.findall('\S+=\S+',ln)) #\S it's a character that it's not a space
                                          #+ is 1 or more.. so it search for the variables=value
#if I don't want to extract the last line, I have to add the timestamp at the match, but
#if I want to extact only the variables and the values I have to use the parenthesis that
#specifies to the findall what to extract from the match
    print(re.findall('^2018.+(\S+=\S+)',ln))
