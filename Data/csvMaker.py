import pandas as pd
import requests
from pylab import *

# just a look up function
def query(location, job_type, year):
	i =find_index(location)
	b = X.loc[find_index(location)][job_type]
	x = year - 2015
	m = slopes[i]
	print "Moving forward ",x, " years"
	print "income changes by ",m," every year"
	print "In 2015, your income is ", b
	p = prediction(m,b,x)
	print "your income in ",year," is ", p
	return p

def find_index(location):
	c = 0
	for i in X['NAME']:
		if str(i) == location:
			return c
		c +=1
	return -1

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

def get_slope(a,b,c):
	# d1 = b-a
	# d2 = c-b
	return (c-a)/2

def prediction(m,b,x):
	return m*x+b

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

def cleanData(a,b):
	b_list = list(b['NAME'])
	for i in a['NAME']:
		if i not in b_list:
			print i
			a = a[a['NAME'] != i]
	return a

for i in range(0,4):
	arrPD[i] = cleanData(arrPD[i],arrPD[0])

for i in range(0,4):
	arrPD[0] = cleanData(arrPD[0],arrPD[i])

for i in range(0,4):
	arrPD[i] = cleanData(arrPD[i],arrPD[0])

slopes = []
for i  in arrPD:
	print i.shape

points = zip(list(arrPD[0]['Median Household']),list(arrPD[1]['Median Household']),list(arrPD[2]['Median Household']))
for a,b,c in points:
	slopes.append(get_slope(a,b,c))
	


X = arrPD[3]

LOC = ['Baldwin County, Alabama', 'Calhoun County, Alabama', 'Cullman County, Alabama', 'DeKalb County, Alabama', 'Elmore County, Alabama', 'Etowah County, Alabama', 'Houston County, Alabama', 'Jefferson County, Alabama', 'Lauderdale County, Alabama', 'Lee County, Alabama', 'Limestone County, Alabama', 'Madison County, Alabama', 'Marshall County, Alabama', 'Mobile County, Alabama', 'Montgomery County, Alabama', 'Morgan County, Alabama', 'St. Clair County, Alabama', 'Shelby County, Alabama', 'Talladega County, Alabama', 'Tuscaloosa County, Alabama', 'Walker County, Alabama', 'Anchorage Municipality, Alaska', 'Fairbanks North Star Borough, Alaska', 'Matanuska-Susitna Borough, Alaska', 'Apache County, Arizona', 'Cochise County, Arizona', 'Coconino County, Arizona', 'Maricopa County, Arizona', 'Mohave County, Arizona', 'Navajo County, Arizona', 'Pima County, Arizona', 'Pinal County, Arizona', 'Yavapai County, Arizona', 'Yuma County, Arizona', 'Benton County, Arkansas', 'Craighead County, Arkansas', 'Faulkner County, Arkansas', 'Garland County, Arkansas', 'Jefferson County, Arkansas', 'Lonoke County, Arkansas', 'Pulaski County, Arkansas', 'Saline County, Arkansas', 'Sebastian County, Arkansas', 'Washington County, Arkansas', 'White County, Arkansas', 'Alameda County, California', 'Butte County, California', 'Contra Costa County, California', 'El Dorado County, California', 'Fresno County, California', 'Humboldt County, California', 'Imperial County, California', 'Kern County, California', 'Kings County, California', 'Lake County, California', 'Los Angeles County, California', 'Madera County, California', 'Marin County, California', 'Mendocino County, California', 'Merced County, California', 'Monterey County, California', 'Napa County, California', 'Nevada County, California', 'Orange County, California', 'Placer County, California', 'Riverside County, California', 'Sacramento County, California', 'San Bernardino County, California', 'San Diego County, California', 'San Francisco County, California', 'San Joaquin County, California', 'San Luis Obispo County, California', 'San Mateo County, California', 'Santa Barbara County, California', 'Santa Clara County, California', 'Santa Cruz County, California', 'Shasta County, California', 'Solano County, California', 'Sonoma County, California', 'Stanislaus County, California', 'Sutter County, California', 'Tulare County, California', 'Ventura County, California', 'Yolo County, California', 'Yuba County, California', 'Adams County, Colorado', 'Arapahoe County, Colorado', 'Boulder County, Colorado', 'Denver County, Colorado', 'Douglas County, Colorado', 'El Paso County, Colorado', 'Jefferson County, Colorado', 'Larimer County, Colorado', 'Mesa County, Colorado', 'Pueblo County, Colorado', 'Weld County, Colorado', 'Fairfield County, Connecticut', 'Hartford County, Connecticut', 'Litchfield County, Connecticut', 'Middlesex County, Connecticut', 'New Haven County, Connecticut', 'New London County, Connecticut', 'Tolland County, Connecticut', 'Windham County, Connecticut', 'Kent County, Delaware', 'New Castle County, Delaware', 'Sussex County, Delaware', 'District of Columbia, District of Columbia', 'Alachua County, Florida', 'Bay County, Florida', 'Brevard County, Florida', 'Broward County, Florida', 'Charlotte County, Florida', 'Citrus County, Florida', 'Clay County, Florida', 'Collier County, Florida', 'Columbia County, Florida', 'Duval County, Florida', 'Escambia County, Florida', 'Flagler County, Florida', 'Hernando County, Florida', 'Highlands County, Florida', 'Hillsborough County, Florida', 'Indian River County, Florida', 'Lake County, Florida', 'Lee County, Florida', 'Leon County, Florida', 'Manatee County, Florida', 'Marion County, Florida', 'Martin County, Florida', 'Miami-Dade County, Florida', 'Monroe County, Florida', 'Nassau County, Florida', 'Okaloosa County, Florida', 'Orange County, Florida', 'Osceola County, Florida', 'Palm Beach County, Florida', 'Pasco County, Florida', 'Pinellas County, Florida', 'Polk County, Florida', 'Putnam County, Florida', 'St. Johns County, Florida', 'St. Lucie County, Florida', 'Santa Rosa County, Florida', 'Sarasota County, Florida', 'Seminole County, Florida', 'Sumter County, Florida', 'Volusia County, Florida', 'Barrow County, Georgia', 'Bartow County, Georgia', 'Bibb County, Georgia', 'Bulloch County, Georgia', 'Carroll County, Georgia', 'Catoosa County, Georgia', 'Chatham County, Georgia', 'Cherokee County, Georgia', 'Clarke County, Georgia', 'Clayton County, Georgia', 'Cobb County, Georgia', 'Columbia County, Georgia', 'Coweta County, Georgia', 'DeKalb County, Georgia', 'Dougherty County, Georgia', 'Douglas County, Georgia', 'Fayette County, Georgia', 'Floyd County, Georgia', 'Forsyth County, Georgia', 'Fulton County, Georgia', 'Glynn County, Georgia', 'Gwinnett County, Georgia', 'Hall County, Georgia', 'Henry County, Georgia', 'Houston County, Georgia', 'Liberty County, Georgia', 'Lowndes County, Georgia', 'Muscogee County, Georgia', 'Newton County, Georgia', 'Paulding County, Georgia', 'Richmond County, Georgia', 'Rockdale County, Georgia', 'Troup County, Georgia', 'Walker County, Georgia', 'Walton County, Georgia', 'Whitfield County, Georgia', 'Hawaii County, Hawaii', 'Honolulu County, Hawaii', 'Kauai County, Hawaii', 'Maui County, Hawaii', 'Ada County, Idaho', 'Bannock County, Idaho', 'Bonneville County, Idaho', 'Canyon County, Idaho', 'Kootenai County, Idaho', 'Twin Falls County, Idaho', 'Adams County, Illinois', 'Champaign County, Illinois', 'Cook County, Illinois', 'DeKalb County, Illinois', 'DuPage County, Illinois', 'Kane County, Illinois', 'Kankakee County, Illinois', 'Kendall County, Illinois', 'Lake County, Illinois', 'LaSalle County, Illinois', 'McHenry County, Illinois', 'McLean County, Illinois', 'Macon County, Illinois', 'Madison County, Illinois', 'Peoria County, Illinois', 'Rock Island County, Illinois', 'St. Clair County, Illinois', 'Sangamon County, Illinois', 'Tazewell County, Illinois', 'Vermilion County, Illinois', 'Will County, Illinois', 'Williamson County, Illinois', 'Winnebago County, Illinois', 'Allen County, Indiana', 'Bartholomew County, Indiana', 'Clark County, Indiana', 'Delaware County, Indiana', 'Elkhart County, Indiana', 'Floyd County, Indiana', 'Grant County, Indiana', 'Hamilton County, Indiana', 'Hancock County, Indiana', 'Hendricks County, Indiana', 'Howard County, Indiana', 'Johnson County, Indiana', 'Kosciusko County, Indiana', 'Lake County, Indiana', 'LaPorte County, Indiana', 'Madison County, Indiana', 'Marion County, Indiana', 'Monroe County, Indiana', 'Morgan County, Indiana', 'Porter County, Indiana', 'St. Joseph County, Indiana', 'Tippecanoe County, Indiana', 'Vanderburgh County, Indiana', 'Vigo County, Indiana', 'Wayne County, Indiana', 'Black Hawk County, Iowa', 'Dallas County, Iowa', 'Dubuque County, Iowa', 'Johnson County, Iowa', 'Linn County, Iowa', 'Polk County, Iowa', 'Pottawattamie County, Iowa', 'Scott County, Iowa', 'Story County, Iowa', 'Woodbury County, Iowa', 'Butler County, Kansas', 'Douglas County, Kansas', 'Johnson County, Kansas', 'Leavenworth County, Kansas', 'Riley County, Kansas', 'Sedgwick County, Kansas', 'Shawnee County, Kansas', 'Wyandotte County, Kansas', 'Boone County, Kentucky', 'Bullitt County, Kentucky', 'Campbell County, Kentucky', 'Christian County, Kentucky', 'Daviess County, Kentucky', 'Fayette County, Kentucky', 'Hardin County, Kentucky', 'Jefferson County, Kentucky', 'Kenton County, Kentucky', 'McCracken County, Kentucky', 'Madison County, Kentucky', 'Pike County, Kentucky', 'Warren County, Kentucky', 'Ascension Parish, Louisiana', 'Bossier Parish, Louisiana', 'Caddo Parish, Louisiana', 'Calcasieu Parish, Louisiana', 'East Baton Rouge Parish, Louisiana', 'Iberia Parish, Louisiana', 'Jefferson Parish, Louisiana', 'Lafayette Parish, Louisiana', 'Lafourche Parish, Louisiana', 'Livingston Parish, Louisiana', 'Orleans Parish, Louisiana', 'Ouachita Parish, Louisiana', 'Rapides Parish, Louisiana', 'St. Landry Parish, Louisiana', 'St. Tammany Parish, Louisiana', 'Tangipahoa Parish, Louisiana', 'Terrebonne Parish, Louisiana', 'Androscoggin County, Maine', 'Aroostook County, Maine', 'Cumberland County, Maine', 'Kennebec County, Maine', 'Penobscot County, Maine', 'York County, Maine', 'Allegany County, Maryland', 'Anne Arundel County, Maryland', 'Baltimore County, Maryland', 'Calvert County, Maryland', 'Carroll County, Maryland', 'Cecil County, Maryland', 'Charles County, Maryland', 'Frederick County, Maryland', 'Harford County, Maryland', 'Howard County, Maryland', 'Montgomery County, Maryland', "Prince George's County, Maryland", "St. Mary's County, Maryland", 'Washington County, Maryland', 'Wicomico County, Maryland', 'Baltimore city, Maryland', 'Barnstable County, Massachusetts', 'Berkshire County, Massachusetts', 'Bristol County, Massachusetts', 'Essex County, Massachusetts', 'Franklin County, Massachusetts', 'Hampden County, Massachusetts', 'Hampshire County, Massachusetts', 'Middlesex County, Massachusetts', 'Norfolk County, Massachusetts', 'Plymouth County, Massachusetts', 'Suffolk County, Massachusetts', 'Worcester County, Massachusetts', 'Allegan County, Michigan', 'Bay County, Michigan', 'Berrien County, Michigan', 'Calhoun County, Michigan', 'Clinton County, Michigan', 'Eaton County, Michigan', 'Genesee County, Michigan', 'Grand Traverse County, Michigan', 'Ingham County, Michigan', 'Isabella County, Michigan', 'Jackson County, Michigan', 'Kalamazoo County, Michigan', 'Kent County, Michigan', 'Lapeer County, Michigan', 'Lenawee County, Michigan', 'Livingston County, Michigan', 'Macomb County, Michigan', 'Marquette County, Michigan', 'Midland County, Michigan', 'Monroe County, Michigan', 'Muskegon County, Michigan', 'Oakland County, Michigan', 'Ottawa County, Michigan', 'Saginaw County, Michigan', 'St. Clair County, Michigan', 'Shiawassee County, Michigan', 'Van Buren County, Michigan', 'Washtenaw County, Michigan', 'Wayne County, Michigan', 'Anoka County, Minnesota', 'Blue Earth County, Minnesota', 'Carver County, Minnesota', 'Dakota County, Minnesota', 'Hennepin County, Minnesota', 'Olmsted County, Minnesota', 'Ramsey County, Minnesota', 'St. Louis County, Minnesota', 'Scott County, Minnesota', 'Sherburne County, Minnesota', 'Stearns County, Minnesota', 'Washington County, Minnesota', 'Wright County, Minnesota', 'DeSoto County, Mississippi', 'Forrest County, Mississippi', 'Harrison County, Mississippi', 'Hinds County, Mississippi', 'Jackson County, Mississippi', 'Jones County, Mississippi', 'Lauderdale County, Mississippi', 'Lee County, Mississippi', 'Madison County, Mississippi', 'Rankin County, Mississippi', 'Boone County, Missouri', 'Buchanan County, Missouri', 'Cape Girardeau County, Missouri', 'Cass County, Missouri', 'Christian County, Missouri', 'Clay County, Missouri', 'Cole County, Missouri', 'Franklin County, Missouri', 'Greene County, Missouri', 'Jackson County, Missouri', 'Jasper County, Missouri', 'Jefferson County, Missouri', 'Platte County, Missouri', 'St. Charles County, Missouri', 'St. Francois County, Missouri', 'St. Louis County, Missouri', 'St. Louis city, Missouri', 'Cascade County, Montana', 'Flathead County, Montana', 'Gallatin County, Montana', 'Missoula County, Montana', 'Yellowstone County, Montana', 'Douglas County, Nebraska', 'Lancaster County, Nebraska', 'Sarpy County, Nebraska', 'Clark County, Nevada', 'Washoe County, Nevada', 'Cheshire County, New Hampshire', 'Grafton County, New Hampshire', 'Hillsborough County, New Hampshire', 'Merrimack County, New Hampshire', 'Rockingham County, New Hampshire', 'Strafford County, New Hampshire', 'Atlantic County, New Jersey', 'Bergen County, New Jersey', 'Burlington County, New Jersey', 'Camden County, New Jersey', 'Cape May County, New Jersey', 'Cumberland County, New Jersey', 'Essex County, New Jersey', 'Gloucester County, New Jersey', 'Hudson County, New Jersey', 'Hunterdon County, New Jersey', 'Mercer County, New Jersey', 'Middlesex County, New Jersey', 'Monmouth County, New Jersey', 'Morris County, New Jersey', 'Ocean County, New Jersey', 'Passaic County, New Jersey', 'Salem County, New Jersey', 'Somerset County, New Jersey', 'Sussex County, New Jersey', 'Union County, New Jersey', 'Warren County, New Jersey', 'Bernalillo County, New Mexico', 'Chaves County, New Mexico', 'Do\xc3\xb1a Ana County, New Mexico', 'Lea County, New Mexico', 'McKinley County, New Mexico', 'Otero County, New Mexico', 'Sandoval County, New Mexico', 'San Juan County, New Mexico', 'Santa Fe County, New Mexico', 'Valencia County, New Mexico', 'Albany County, New York', 'Bronx County, New York', 'Broome County, New York', 'Cattaraugus County, New York', 'Cayuga County, New York', 'Chautauqua County, New York', 'Chemung County, New York', 'Clinton County, New York', 'Dutchess County, New York', 'Erie County, New York', 'Jefferson County, New York', 'Kings County, New York', 'Livingston County, New York', 'Madison County, New York', 'Monroe County, New York', 'Nassau County, New York', 'New York County, New York', 'Niagara County, New York', 'Oneida County, New York', 'Onondaga County, New York', 'Ontario County, New York', 'Orange County, New York', 'Oswego County, New York', 'Putnam County, New York', 'Queens County, New York', 'Rensselaer County, New York', 'Richmond County, New York', 'Rockland County, New York', 'St. Lawrence County, New York', 'Saratoga County, New York', 'Schenectady County, New York', 'Steuben County, New York', 'Suffolk County, New York', 'Sullivan County, New York', 'Tompkins County, New York', 'Ulster County, New York', 'Warren County, New York', 'Wayne County, New York', 'Westchester County, New York', 'Alamance County, North Carolina', 'Brunswick County, North Carolina', 'Buncombe County, North Carolina', 'Burke County, North Carolina', 'Cabarrus County, North Carolina', 'Caldwell County, North Carolina', 'Carteret County, North Carolina', 'Catawba County, North Carolina', 'Chatham County, North Carolina', 'Cleveland County, North Carolina', 'Craven County, North Carolina', 'Cumberland County, North Carolina', 'Davidson County, North Carolina', 'Durham County, North Carolina', 'Forsyth County, North Carolina', 'Gaston County, North Carolina', 'Guilford County, North Carolina', 'Harnett County, North Carolina', 'Henderson County, North Carolina', 'Iredell County, North Carolina', 'Johnston County, North Carolina', 'Lincoln County, North Carolina', 'Mecklenburg County, North Carolina', 'Moore County, North Carolina', 'Nash County, North Carolina', 'New Hanover County, North Carolina', 'Onslow County, North Carolina', 'Orange County, North Carolina', 'Pitt County, North Carolina', 'Randolph County, North Carolina', 'Robeson County, North Carolina', 'Rockingham County, North Carolina', 'Rowan County, North Carolina', 'Rutherford County, North Carolina', 'Surry County, North Carolina', 'Union County, North Carolina', 'Wake County, North Carolina', 'Wayne County, North Carolina', 'Wilkes County, North Carolina', 'Wilson County, North Carolina', 'Burleigh County, North Dakota', 'Cass County, North Dakota', 'Grand Forks County, North Dakota', 'Allen County, Ohio', 'Ashtabula County, Ohio', 'Belmont County, Ohio', 'Butler County, Ohio', 'Clark County, Ohio', 'Clermont County, Ohio', 'Columbiana County, Ohio', 'Cuyahoga County, Ohio', 'Delaware County, Ohio', 'Erie County, Ohio', 'Fairfield County, Ohio', 'Franklin County, Ohio', 'Geauga County, Ohio', 'Greene County, Ohio', 'Hamilton County, Ohio', 'Hancock County, Ohio', 'Jefferson County, Ohio', 'Lake County, Ohio', 'Licking County, Ohio', 'Lorain County, Ohio', 'Lucas County, Ohio', 'Mahoning County, Ohio', 'Marion County, Ohio', 'Medina County, Ohio', 'Miami County, Ohio', 'Montgomery County, Ohio', 'Muskingum County, Ohio', 'Portage County, Ohio', 'Richland County, Ohio', 'Ross County, Ohio', 'Scioto County, Ohio', 'Stark County, Ohio', 'Summit County, Ohio', 'Trumbull County, Ohio', 'Tuscarawas County, Ohio', 'Warren County, Ohio', 'Wayne County, Ohio', 'Wood County, Ohio', 'Canadian County, Oklahoma', 'Cleveland County, Oklahoma', 'Comanche County, Oklahoma', 'Creek County, Oklahoma', 'Muskogee County, Oklahoma', 'Oklahoma County, Oklahoma', 'Payne County, Oklahoma', 'Pottawatomie County, Oklahoma', 'Rogers County, Oklahoma', 'Tulsa County, Oklahoma', 'Wagoner County, Oklahoma', 'Benton County, Oregon', 'Clackamas County, Oregon', 'Deschutes County, Oregon', 'Douglas County, Oregon', 'Jackson County, Oregon', 'Josephine County, Oregon', 'Klamath County, Oregon', 'Lane County, Oregon', 'Linn County, Oregon', 'Marion County, Oregon', 'Multnomah County, Oregon', 'Polk County, Oregon', 'Umatilla County, Oregon', 'Washington County, Oregon', 'Yamhill County, Oregon', 'Adams County, Pennsylvania', 'Allegheny County, Pennsylvania', 'Armstrong County, Pennsylvania', 'Beaver County, Pennsylvania', 'Berks County, Pennsylvania', 'Blair County, Pennsylvania', 'Bucks County, Pennsylvania', 'Butler County, Pennsylvania', 'Cambria County, Pennsylvania', 'Carbon County, Pennsylvania', 'Centre County, Pennsylvania', 'Chester County, Pennsylvania', 'Clearfield County, Pennsylvania', 'Columbia County, Pennsylvania', 'Crawford County, Pennsylvania', 'Cumberland County, Pennsylvania', 'Dauphin County, Pennsylvania', 'Delaware County, Pennsylvania', 'Erie County, Pennsylvania', 'Fayette County, Pennsylvania', 'Franklin County, Pennsylvania', 'Indiana County, Pennsylvania', 'Lackawanna County, Pennsylvania', 'Lancaster County, Pennsylvania', 'Lawrence County, Pennsylvania', 'Lebanon County, Pennsylvania', 'Lehigh County, Pennsylvania', 'Luzerne County, Pennsylvania', 'Lycoming County, Pennsylvania', 'Mercer County, Pennsylvania', 'Monroe County, Pennsylvania', 'Montgomery County, Pennsylvania', 'Northampton County, Pennsylvania', 'Northumberland County, Pennsylvania', 'Philadelphia County, Pennsylvania', 'Schuylkill County, Pennsylvania', 'Somerset County, Pennsylvania', 'Washington County, Pennsylvania', 'Westmoreland County, Pennsylvania', 'York County, Pennsylvania', 'Kent County, Rhode Island', 'Newport County, Rhode Island', 'Providence County, Rhode Island', 'Washington County, Rhode Island', 'Aiken County, South Carolina', 'Anderson County, South Carolina', 'Beaufort County, South Carolina', 'Berkeley County, South Carolina', 'Charleston County, South Carolina', 'Darlington County, South Carolina', 'Dorchester County, South Carolina', 'Florence County, South Carolina', 'Greenville County, South Carolina', 'Greenwood County, South Carolina', 'Horry County, South Carolina', 'Lancaster County, South Carolina', 'Laurens County, South Carolina', 'Lexington County, South Carolina', 'Oconee County, South Carolina', 'Orangeburg County, South Carolina', 'Pickens County, South Carolina', 'Richland County, South Carolina', 'Spartanburg County, South Carolina', 'Sumter County, South Carolina', 'York County, South Carolina', 'Minnehaha County, South Dakota', 'Pennington County, South Dakota', 'Anderson County, Tennessee', 'Blount County, Tennessee', 'Bradley County, Tennessee', 'Davidson County, Tennessee', 'Greene County, Tennessee', 'Hamilton County, Tennessee', 'Knox County, Tennessee', 'Madison County, Tennessee', 'Maury County, Tennessee', 'Montgomery County, Tennessee', 'Putnam County, Tennessee', 'Robertson County, Tennessee', 'Rutherford County, Tennessee', 'Sevier County, Tennessee', 'Shelby County, Tennessee', 'Sullivan County, Tennessee', 'Sumner County, Tennessee', 'Washington County, Tennessee', 'Williamson County, Tennessee', 'Wilson County, Tennessee', 'Angelina County, Texas', 'Bastrop County, Texas', 'Bell County, Texas', 'Bexar County, Texas', 'Bowie County, Texas', 'Brazoria County, Texas', 'Brazos County, Texas', 'Cameron County, Texas', 'Collin County, Texas', 'Comal County, Texas', 'Coryell County, Texas', 'Dallas County, Texas', 'Denton County, Texas', 'Ector County, Texas', 'Ellis County, Texas', 'El Paso County, Texas', 'Fort Bend County, Texas', 'Galveston County, Texas', 'Grayson County, Texas', 'Gregg County, Texas', 'Guadalupe County, Texas', 'Harris County, Texas', 'Harrison County, Texas', 'Hays County, Texas', 'Henderson County, Texas', 'Hidalgo County, Texas', 'Hunt County, Texas', 'Jefferson County, Texas', 'Johnson County, Texas', 'Kaufman County, Texas', 'Liberty County, Texas', 'Lubbock County, Texas', 'McLennan County, Texas', 'Midland County, Texas', 'Montgomery County, Texas', 'Nacogdoches County, Texas', 'Nueces County, Texas', 'Orange County, Texas', 'Parker County, Texas', 'Potter County, Texas', 'Randall County, Texas', 'Rockwall County, Texas', 'San Patricio County, Texas', 'Smith County, Texas', 'Tarrant County, Texas', 'Taylor County, Texas', 'Tom Green County, Texas', 'Travis County, Texas', 'Victoria County, Texas', 'Walker County, Texas', 'Webb County, Texas', 'Wichita County, Texas', 'Williamson County, Texas', 'Cache County, Utah', 'Davis County, Utah', 'Salt Lake County, Utah', 'Utah County, Utah', 'Washington County, Utah', 'Weber County, Utah', 'Chittenden County, Vermont', 'Albemarle County, Virginia', 'Arlington County, Virginia', 'Augusta County, Virginia', 'Bedford County, Virginia', 'Chesterfield County, Virginia', 'Fairfax County, Virginia', 'Fauquier County, Virginia', 'Frederick County, Virginia', 'Hanover County, Virginia', 'Henrico County, Virginia', 'James City County, Virginia', 'Loudoun County, Virginia', 'Montgomery County, Virginia', 'Prince William County, Virginia', 'Roanoke County, Virginia', 'Rockingham County, Virginia', 'Spotsylvania County, Virginia', 'Stafford County, Virginia', 'York County, Virginia', 'Alexandria city, Virginia', 'Chesapeake city, Virginia', 'Hampton city, Virginia', 'Lynchburg city, Virginia', 'Newport News city, Virginia', 'Norfolk city, Virginia', 'Portsmouth city, Virginia', 'Richmond city, Virginia', 'Roanoke city, Virginia', 'Suffolk city, Virginia', 'Virginia Beach city, Virginia', 'Benton County, Washington', 'Chelan County, Washington', 'Clallam County, Washington', 'Clark County, Washington', 'Cowlitz County, Washington', 'Franklin County, Washington', 'Grant County, Washington', 'Grays Harbor County, Washington', 'Island County, Washington', 'King County, Washington', 'Kitsap County, Washington', 'Lewis County, Washington', 'Pierce County, Washington', 'Skagit County, Washington', 'Snohomish County, Washington', 'Spokane County, Washington', 'Thurston County, Washington', 'Whatcom County, Washington', 'Yakima County, Washington', 'Berkeley County, West Virginia', 'Cabell County, West Virginia', 'Harrison County, West Virginia', 'Kanawha County, West Virginia', 'Monongalia County, West Virginia', 'Raleigh County, West Virginia', 'Wood County, West Virginia', 'Brown County, Wisconsin', 'Dane County, Wisconsin', 'Dodge County, Wisconsin', 'Eau Claire County, Wisconsin', 'Fond du Lac County, Wisconsin', 'Jefferson County, Wisconsin', 'Kenosha County, Wisconsin', 'La Crosse County, Wisconsin', 'Manitowoc County, Wisconsin', 'Marathon County, Wisconsin', 'Milwaukee County, Wisconsin', 'Outagamie County, Wisconsin', 'Ozaukee County, Wisconsin', 'Portage County, Wisconsin', 'Racine County, Wisconsin', 'Rock County, Wisconsin', 'St. Croix County, Wisconsin', 'Sheboygan County, Wisconsin', 'Walworth County, Wisconsin', 'Washington County, Wisconsin', 'Waukesha County, Wisconsin', 'Winnebago County, Wisconsin', 'Wood County, Wisconsin', 'Laramie County, Wyoming', 'Natrona County, Wyoming', 'Arecibo Municipio, Puerto Rico', 'Bayam\xc3\xb3n Municipio, Puerto Rico', 'Caguas Municipio, Puerto Rico', 'Carolina Municipio, Puerto Rico', 'Guaynabo Municipio, Puerto Rico', 'Mayag\xc3\xbcez Municipio, Puerto Rico', 'Ponce Municipio, Puerto Rico', 'San Juan Municipio, Puerto Rico', 'Toa Alta Municipio, Puerto Rico', 'Toa Baja Municipio, Puerto Rico', 'Trujillo Alto Municipio, Puerto Rico']
