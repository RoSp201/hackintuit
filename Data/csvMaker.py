import pandas as pd
import requests
import StringIO



code_to_name = {'S0601_C02_036E':'educational attainment',
                'S0601_C01_039E':'income 0-10K',
                'S0601_C01_040E':'income 10-15K',
                'S0601_C01_041E':'income 15-25K',
                'S0601_C01_042E':'income 25-35K',
                'S0601_C01_043E':'income 35-50K',
                'S0601_C01_044E':'income 50-65K',
                'S0601_C01_045E':'income 65-75K',
                'S0601_C01_046E':'income 75K-end',
                'S2411_C01_001E':'median income',
                'S2411_C01_004E':'Management income',
                'S2411_C01_005E':'Busineess Finance Operations',
                'S2411_C01_006E':'Computer engineer/science',
                'S2411_C01_007E':'Computer and Math',
                'S2411_C01_008E':'Architectural engineering',
                'S2411_C01_009E':'Life/Social/Physical science',
                'S2411_C01_011E':'Community and Social',
                'S2411_C01_012E':'Legal',
                'S2411_C01_013E':'Education',
                'S2411_C01_014E':'Arts,sports,design',
                'S2411_C01_016E':'Health Diagnosing',
                'S2411_C01_017E':"Health Technical",
                'S2411_C01_019E':'Health Support',
                'S2411_C01_021E':'Fire Fighting',
                'S2411_C01_022E':'Law Enforcement',
                'S2411_C01_023E':'Food Service',
                'S2411_C01_024E':'Building/Grounds Maintenance',
                'S2411_C01_025E':'Personal care and service',
                'S2411_C01_027E':'Sales',
                'S2411_C01_028E':'Office Administrative',
                'S2411_C01_030E':'Farming, fishing, forestry',
                'S2411_C01_031E':'Construcation & Extraction',
                'S2411_C01_032E':'Installation, maintenance, repair',
                'S2411_C01_034E':'Production Occupation',
                'S2411_C01_035E':'Transportation',
                'S2411_C01_036E':'Material Moving',
                'S0601_C01_001E':'Population'
                 }

convert = {'S0601_C02_036E':'educational attainment',
                'S0601_C01_039E':'income 0-10K',
                'S0601_C01_040E':'income 10-15K',
                'S0601_C01_041E':'income 15-25K',
                'S0601_C01_042E':'income 25-35K',
                'S0601_C01_043E':'income 35-50K',
                'S0601_C01_044E':'income 50-65K',
                'S0601_C01_045E':'income 65-75K',
                'S0601_C01_046E':'income 75K-end',
                'S2411_C01_001E':'median income',
                'S2411_C01_004E':'Management income',
                'S2411_C01_005E':'Busineess Finance Operations',
                'S2411_C01_006E':'Computer engineer/science',
                'S2411_C01_007E':'Computer and Math',
                'S2411_C01_008E':'Architectural engineering',
                'S2411_C01_009E':'Life/Social/Physical science',
                'S2411_C01_011E':'Community and Social',
                'S2411_C01_012E':'Legal',
                'S2411_C01_013E':'Education',
                'S2411_C01_014E':'Arts,sports,design',
                'S2411_C01_016E':'Health Diagnosing',
                'S2411_C01_017E':"Health Technical",
                'S2411_C01_019E':'Health Support',
                'S2411_C01_021E':'Fire Fighting',
                'S2411_C01_022E':'Law Enforcement',
                'S2411_C01_023E':'Food Service',
                'S2411_C01_024E':'Building/Grounds Maintenance',
                'S2411_C01_025E':'Personal care and service',
                'S2411_C01_027E':'Sales',
                'S2411_C01_028E':'Office Administrative',
                'S2411_C01_030E':'Farming, fishing, forestry',
                'S2411_C01_031E':'Construcation & Extraction',
                'S2411_C01_032E':'Installation, maintenance, repair',
                'S2411_C01_034E':'Production Occupation',
                'S2411_C01_035E':'Transportation',
                'S2411_C01_036E':'Material Moving',
                'S0601_C01_001E':'Population',
                'DP03_0062E':"Median Household"
                 }
jobs = {
	            'S2411_C01_004E':'Management income',
                'S2411_C01_005E':'Busineess Finance Operations',
                'S2411_C01_006E':'Computer engineer/science',
                'S2411_C01_007E':'Computer and Math',
                'S2411_C01_008E':'Architectural engineering',
                'S2411_C01_009E':'Life/Social/Physical science',
                'S2411_C01_011E':'Community and Social',
                'S2411_C01_012E':'Legal',
                'S2411_C01_013E':'Education',
                'S2411_C01_014E':'Arts,sports,design',
                'S2411_C01_016E':'Health Diagnosing',
                'S2411_C01_017E':"Health Technical",
                'S2411_C01_019E':'Health Support',
                'S2411_C01_021E':'Fire Fighting',
                'S2411_C01_022E':'Law Enforcement',
                'S2411_C01_023E':'Food Service',
                'S2411_C01_024E':'Building/Grounds Maintenance',
                'S2411_C01_025E':'Personal care and service',
                'S2411_C01_027E':'Sales',
                'S2411_C01_028E':'Office Administrative',
                'S2411_C01_030E':'Farming, fishing, forestry',
                'S2411_C01_031E':'Construcation & Extraction',
                'S2411_C01_032E':'Installation, maintenance, repair',
                'S2411_C01_034E':'Production Occupation',
                'S2411_C01_035E':'Transportation',
                'S2411_C01_036E':'Material Moving'
}
arrPD = []
X = 0
for year in range(2012,2015):
	y = str(year)
	base = 'http://api.census.gov/data/'+y+'/acs1/profile?get=NAME,'
	args = 'DP03_0062E'
	end = '&for=county:*&key=53ea32379702c3b68d65622b31b575f41aaae962'
	url = base+args+end
	print url
	r = requests.get(url)
	line = r.content
	line = line.replace('[','')
	line = line.replace(']','')

	interFile = "out"+y+".csv"
	text_file = open(interFile, "w")
	text_file.write(line)
	text_file.close()
	X = pd.read_csv(interFile)

	for i in X:
		try:
			X.rename(columns={i:convert[i]}, inplace=True)
		except:
			pass

	file_name = "clean_data"+y+".csv"
	X.to_csv(file_name)
	arrPD.append(X)

year = 2015
y = str(year)
base = 'http://api.census.gov/data/'+y+'/acs1/subject?get=NAME,'
args = ''
for i in code_to_name:
	if len(args)==0:
		args = i;
	args = args+','+i
end = '&for=county:*&key=53ea32379702c3b68d65622b31b575f41aaae962'
url = base+args+end

r = requests.get(url)
line = r.content
line = line.replace('[','')
line = line.replace(']','')

interFile = "out"+y+".csv"
text_file = open(interFile, "w")
text_file.write(line)
text_file.close()
X = pd.read_csv(interFile)

for i in X:
	try:
		X.rename(columns={i:convert[i]}, inplace=True)
	except:
		pass

file_name = "clean_data"+y+".csv"
X.to_csv(file_name)
arrPD.append(X)

# just a look up function
def query(location, job_type):
	return X[X['NAME'] == location][job_type]

# what can I ask for in the second arg of query
def what_infos():
	result = []
	for i in code_to_name:
		print code_to_name[i]
		result.append(code_to_name[i])
	return result

# what can I ask for in the first arg of query
def what_locations():
	result  = []
	for i in X['NAME']:
		print i
		result.append(i)
	return result

def what_jobs():
	result = []
	for i in jobs:
		print jobs[i]
		result.append(jobs[i])
	return result