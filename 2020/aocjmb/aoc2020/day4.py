from aocd import data
from itertools import combinations
import re


def part_a(data):
    data = [ dict( n.split(":") for n in re.split(" |\n", x) ) for x in data.strip().split("\n\n") ]
    valid_ppts = 0
    for ppt in data:
        valid = True
        for field in req_fields: 
            if field not in ppt.keys():
                valid = False
                break
        if valid:
            valid_ppts = valid_ppts + 1

    return valid_ppts

def part_b(data):
    data = [ dict( n.split(":") for n in re.split(" |\n", x) ) for x in data.strip().split("\n\n") ]
    valid_ppts = 0
    for ppt in data:
        valid = True
        for field in req_fields: 
            if field not in ppt.keys():
                valid = False
            else:
                if field == "byr":
                    try:
                        val = int(ppt[field])
                        if val < 1920 or val > 2002:
                            valid = False
                            break
                    except ValueError:
                        valid = False
                        break
                elif field == "iyr":
                    try:
                        val = int(ppt[field])
                        if val < 2010 or val > 2020:
                            valid = False
                            break
                    except ValueError:
                        valid = False
                        break
                elif field == "eyr":
                    try:
                        val = int(ppt[field])
                        if val < 2020 or val > 2030:
                            valid = False
                            break
                    except ValueError:
                        valid = False
                        break
                elif field == "hgt":
                    unit = ppt[field][-2:]
                    hgt = ppt[field][:-2]
                    try:
                        hgt = int(hgt)
                        if unit == "cm":
                            if hgt < 150 or hgt > 193:
                                valid = False
                                break
                        elif unit == "in":
                            if hgt < 59 or hgt > 76:
                                valid = False
                                break
                        else:
                            valid = False
                            break
                    except ValueError:
                        valid = False
                        break
                elif field == "hcl":
                    if not re.match("^#([a-f]|[0-9]){6}i$", ppt[field]):
                        valid = False
                        break
                elif field == "ecl":
                    if ppt[field] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        valid = False
                        break
                elif field == "pid":
                    if len(ppt[field]) != 9 or not ppt[field].isnumeric():
                        valid = False
                        break
        if valid:
            valid_ppts = valid_ppts + 1

    return valid_ppts


test_data1 = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

test_data2 = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

if __name__ == "__main__":
    assert part_a(test_data1) == 2
    assert part_b(test_data2) == 4
    print(part_a(data))
    print(part_b(data))
