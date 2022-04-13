import json
import os
from pprint import pprint

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASEDIR, "json")

json_files = [file for file in os.listdir(DATA_DIR) if file.endswith('.json')]

areas_dict = {
    "JHR": "Johor",
    "KDH": "Kedah",
    "KTN": "Kelantan",
    "KUL": "Wilayah Persekutuan Kuala Lumpur",
    "LBN": "Wilayah Persekutuan Labuan",
    "MLK": "Melaka",
    "NSN": "Negeri Sembilan",
    "PHG": "Pahang",
    "PJY": "Wilayah Persekutuan Putra Jaya",
    "PLS": "Perlis",
    "PNG": "Pulau Pinang",
    "PRK": "Perak",
    "SBH": "Sabah",
    "SGR": "Selangor",
    "SRW": "Sarawak",
    "TRG": "Terengganu"
}

data_dict = {"state": []}

# print(json_files)

def compile_json():
    for file in json_files:
        with open(os.path.join(DATA_DIR, file), mode="r") as out:
            temp_list = json.load(out)
            # pprint(temp_dict, indent=2)
            data_dict["state"].append({"name": areas_dict[file.replace('.json', '').upper()], "city":temp_list})

def generate_json():
    json_object = json.dumps(data_dict, separators=(',', ':'))
    with open("generated.json", "w") as out:
        out.write(json_object)

# pprint(data_dict, indent=4)

if __name__ == '__main__':
    compile_json()
    generate_json()
    
