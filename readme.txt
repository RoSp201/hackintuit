README FILE

COMMAND LINE INTERFACE

Run the command

>>> python -i csvMaker.py

Enter a query

>>> query(<location>, <job>, <year>)

To find valid locations:

>>> what_locations()

To find valid jobs

>>> what_jobs()

Any year is valid. The data is best used for dates centered around 2015



How does it work?

The growth of income of each county is calculated from year 2012 to 2014

The initial value of the income of a sector is grabbed from year 2015

Forward calculation and back calculation or just multiples of the growth times 
the offset of the year from 2015 plus the initial value at 2015


Who cares?

If one want to optimize the location to work based on expected salary at a given year
one would use this tool to find the best paying places during that year for a certain sector

or you could look for the highest paying sector at your location

or you could see if the pay is declining or increasing



What weaknesses? 

Only 3 years of data used to calculate slop. 
	-- Time constraint 
No comparison data found as of this point
	-- Time constraint
Assumes linearization of growth. Most of the time this is exponential
	-- 3% growth usually, for short term this can be modeled as linear
Assumes growth on the overall applies to the growth of each sector uniformly
	-- it is likely that economies grow together, exceptions do exist
		think movies in hollywood, tech in SV, finances in NY
		

