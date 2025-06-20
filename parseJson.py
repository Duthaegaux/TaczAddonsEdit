import os
import re

def change(string: str, dat: dict, re_pat: str, out):
    if dat == 0: 
        out.write(string)
        return
    for el in dat.keys():
        if f"\"{el}\":" in string:
            out.write(string.replace(re.findall(re_pat, string)[0], str(dat[el])))
            return
    out.write(string)

jsons = os.listdir("./jsons")
data = {
    "602x41": {
        "damage": 10.2,
        "speed": 800,
        "head_shot_multiplier": 1.5,
        "armor_ignore": 0.45,
        "life": 1.2,
        "gravity": 0.0,
        "knockback": 0.0
    },
    "762x39": {
        "damage": 7.0,
        "speed": 760,
        "head_shot_multiplier": 2.0,
        "armor_ignore": 0.3,
        "life": 1.2,
        "gravity": 0.0,
        "knockback": 0.0
    },
    "545x39": {
        "damage": 5.5,
        "speed": 800,
        "head_shot_multiplier": 1.2,
        "armor_ignore": 0.3,
        "life": 1.2,
        "gravity": 0.0,
        "knockback": 0.0
    },
    "556x45": {
        "damage": 6.5,
        "speed": 900,
        "head_shot_multiplier": 1.7,
        "armor_ignore": 0.3,
        "life": 1.2,
        "gravity": 0.0,
        "knockback": 0.0
    },
    "308": {
        "damage": 17.0,
        "speed": 840,
        "head_shot_multiplier": 2.0,
        "armor_ignore": 0.3,
        "life": 1.2,
        "gravity": 0.0,
        "knockback": 0.0
    },
    "9mm": {
        "damage": 4.2,
        "speed": 365,
        "head_shot_multiplier": 1.2,
        "armor_ignore": 0.1,
        "life": 1.2,
        "gravity": 0.0,
        "knockback": 0.0
    },
    "50beowulf": {},
    "300blk": {},
    "57x28": {},
    "300winmag": {},
    "223remington": {},
    "50bmg":{},
    "can_blanks":{},
    "556x30": {},
    "12g_db": {},
    "12g": {},
    "762x54": {},
    "12g_fl": {},
    "75fk": {},
    "40mm": {},
    "338": {},
    "45acp": {},
    "416barrett": {},
    "30_06": {},
    "nails": {},
    "bannana": {},
    "65creedmoor": {},
    "50ae": {},
    "laser": {}
}

grav, knock = 0.0, 0.0

# reAmmo = r"[\d]+x[\d]+"
# reXz = r":[\d]+[\w]+"
# reWtf = r":[^,]+"
# reComb = f":{reWtf}|:{reXz}|:{reAmmo}|:{reNum}"

reNum = r"[\d]+[.]{0,1}[\d]*"
reAbsolute = r":[^,^\"^ ]+"

for json in jsons:
    file = open(f"./jsons/{json}", "r")
    output = open(f"./output/{json}", "w")

    print(f"Working on {json} - ", end="")

    lines = file.readlines()
    dat = 0
    for line in lines:
        if "ammo" in line and dat == 0:
            print(re.findall(reAbsolute, line)[0][1::])
            dat  = data[re.findall(reAbsolute, line)[0][1::]]
            
        change(line, dat, reNum, output)
    
    file.close()
    output.close()

print("Ready! Check output folder.")
