## Introduction
The company has now rapidly grown to around 2000 employees and a report needs to be
compiled on how much salary each employee should receive at the end of the month.
All employees have filed reports on how much they have worked this last month, and
someone from the IT department have assembled them into one single file. Each line in the
file represents a day when the person is said to have worked, and the start and stop time on
any given day. The file also contains a person’s social security number [Personnummer] but
the last four digits have been masked out due to a questionable interpretation of GDPR. At your 
disposal there is also a staff catalogue, structured in almost the same way. There, the
salaries, and names of the employees are stated, as well as date of birth.

Even though the social security number is incomplete, as luck would have It, there are no two
people with the same name born on the same day. You can therefore assume that the
combination of first name, last name and date of birth is unique.

However, you have reason to suspect foul play in the reporting. Not only do people appear to
work less on certain days of the week, but you’ve also heard rumors that someone has been
cheating with the time report. Today’s mission is to determine if someone’s cheated, and if
so, how much money they’ve tried to acquire. Secondly you are to find out if people have
systematically been avoiding certain days of the week. (Note that the business is closed on
weekends).


## Merging the data
Now that the content of the files has been imported and split up into columns, it’s time to join
the two tables together. Since it has been stated that the combination of names and date of
birth uniquely identifies an employee, these columns can be concatenated [“Glued together”]
to form a unique key. To join these two tables together, the identifying columns must have
the same format. Use the LEFT/RIGHT/MID/SUBSTITUTE functions to format the columns to
have the same format.
• From the reporting table, date of birth must be extracted from the social security
number
• From the employee catalogue, the date of birth column as to be formatted the same
way as in the reporting table. Since the social security number denotes years with only
two letters, you may want to trim down the date of birth here to look the same
Once you have three columns looking the same in both tables, concatenate the columns into
a composite key and use INDEX – MATCH (For newer versions of Excel XLOOKUP is also ok) to
import the relevant columns from the employee catalogue into the reporting sheet.

## Number crunching
With the data merged it is time to calculate people’s salaries. Here it must be considered that
employees have the right to overtime compensation of an additional 35% when working after
17:30. Start by calculating the salary for each individual row on the report sheet. To use 17:30
inside a formula, you may find the TIME function useful, but other solutions are of course also
an option.

Is there any substantial difference between the days of the week? Illustrate with a suitable
graph.

Compile on a new sheet using a pivot table, how much salary each employee expects to
receive. Give the sheet a suitable name e.g. “Salaries”.
Do you find someone who seems to have cheated in their reporting? If so, take note of the
person's name and the sum of the person's expected salary (round to nearest Euro).
