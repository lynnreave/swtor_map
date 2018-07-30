import re
import os

regex_string_1 = 'add_resource = {\s*\n\s+resource = %s\s*\n\s+amount = \d+\s*\n\s+replace = yes\s*\n\s+}'
regex_string_2 = 'add_resource = {\s*\n\s+resource = %s\s*\n\s+amount = \d+\s*\n\s+}'
replc_string = 'set_deposit = d_%s_deposit'
resources = [
    ['minerals', 'mineral'],
    ['energy', 'energy'],
    ['food', 'farmland'],
    ['engineering_research', 'engineering'],
    ['society_research', 'society'],
    ['physics_research', 'physics'],
]
warnings = []

path = os.getcwdu()
contents = os.listdir(path)
for item in contents:
    if str(item) in ['example.txt', 'update.py']:
        pass
    else:
        print item
        if '.txt' in str(item):
            dir_path = path
            inits = [item]
        else:
            dir_path = path + '\\' + item
            inits = os.listdir(dir_path)
        for init in inits:
            init_path = dir_path + '\\' + init
            f = open(init_path, 'r')
            data = f.read()
            f.close()
            data = str(data)
            for resource in resources:
                r1 = regex_string_1 % resource[0]
                r2 = regex_string_2 % resource[0]
                s = replc_string % resource[1]
                matches = re.findall(r1, data)
                for match in matches:
                    #print(match)
                    #print (s)
                    data = data.replace(str(match), str(s))
                matches = re.findall(r2, data)
                for match in matches:
                    data = data.replace(str(match), str(s))
            if len(re.findall('add_resource', data)) > 0:
                warnings.append(init)
            #print(data)
            f = open(init_path, 'w')
            f.write(data)
            f.close()
            
for warning in warnings:
    print warning
