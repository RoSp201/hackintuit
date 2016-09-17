


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
                'S2411_C01_036E':'Material Moving'
                 }


base = 'http://api.census.gov/data/2015/acs1/subject?get=NAME,'
args = 'S0601_C02_036E,S0601_C01_039E,S0601_C01_040E,S0601_C01_041E,S0601_C01_042E,S0601_C01_043E,S0601_C01_044E,S0601_C01_045E,S0601_C01_046E,S2411_C01_001E,S2411_C01_004E,S2411_C01_005E,S2411_C01_006E,S2411_C01_007E,S2411_C01_008E,S2411_C01_009E,S2411_C01_011E,S2411_C01_012E,S2411_C01_013E,S2411_C01_014E,S2411_C01_016E,S2411_C01_017E,S2411_C01_019E,S2411_C01_021E,S2411_C01_022E,S2411_C01_023E,S2411_C01_024E,S2411_C01_025E,S2411_C01_027E,S2411_C01_028E,S2411_C01_030E,S2411_C01_031E,S2411_C01_032E,S2411_C01_034E,S2411_C01_035E,S2411_C01_036E'
end = '&for=county:*&key=53ea32379702c3b68d65622b31b575f41aaae962'
url = base+args+end

