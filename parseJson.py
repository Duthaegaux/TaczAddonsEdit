import os
import re
import settings
import time

def change(line: str, data: list, re_pat: str, out):
    if data == 0:
        out.write(line)
        return
    for key in data.keys():
        if f"\"{key}\":" in line:
            mod_pat = f"\"{key}\": {re_pat}"
            num = re.findall(mod_pat, line)
            if len(num) == 1:
                out.write(line.replace(num[0], f"\"{key}\": {data[key]}"))
                return
    out.write(line)

def trace(weapon: str, cal: str, info: dict):
    if cal in info:
        info[cal].append(weapon)
        return info
    info[cal] = [weapon]
    return info

def outp(dct: dict):
    info = open("info.txt", "w")
    for key in dct.keys():
        info.write(f"\n\n{key}\n\t")
        c = 1
        for element in dct[key]:
            info.write(f"{element} ")
            if c % 6 == 0:
                info.write("\n\t")
            c+=1
    info.close()
            

jsons = os.listdir("./jsons")

data = settings.data
standart = settings.standart

reNum = r"[\d]+[.]{0,1}[\d]*"
reAbsolute = r":[^,^\"^ ]+"

info = dict()

for json in jsons:
    file = open(f"./jsons/{json}", "r")
    output = open(f"./output/{json}", "w")

    print(f"Working on {json} - ", end="")

    lines = file.readlines()
    dat = 0
    for line in lines:
        if "ammo" in line and dat == 0:
            cal = re.findall(reAbsolute, line)[0][1::]
            print(cal)

            if cal not in data:
                data[cal] = dict()
                print(f"\t{cal} not in settings! Adding it to avoid error")
            dat = standart | data[cal]

            info = trace(json.replace(".json", ""), cal, info)
            
            
        change(line, dat, reNum, output)
    
    file.close()
    output.close()

print("\nReady! Check output folder.")

outp(info)
print("\nCreated info.txt file with sort by caliber.")
