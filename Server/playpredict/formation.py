import os
import json
import pandas
import random

class Formation:
    def __init__(self, name, weight=1.0):
        self.name = name
        self.weight = weight
        # Check if formation has an image file, otherwise use placeholder
        if os.path.exists(f"./static/img/formation/{name}.svg"):
            self.image = f"/static/img/{name}.svg"
        else:
            # Randomly select /static/img/formplaceholder#.svg where # is 1-3
            self.image = f"/static/img/formplaceholder{random.randint(1, 3)}.jpg"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

data = pandas.read_csv("data/data.tsv", sep="\t")

offense_formations_str = []
defense_formations_str = []
for index, row in data.iterrows():
    offense_formations_str.append(str(row["Offensive Formation"]))
    if str(row["Defensive Front"]) != "nan":
        defense_formations_str.append(str(row["Defensive Front"]))
# Only keep unique formations
offense_formations_str = list(set(offense_formations_str))
defense_formations_str = list(set(defense_formations_str))
offense_formations = []
defense_formations = []
for formation in offense_formations_str:
    offense_formations.append(Formation(formation))
for formation in defense_formations_str:
    defense_formations.append(Formation(formation))

def findFormation(name):
    for formation in offense_formations:
        if formation.name == name:
            return formation
    for formation in defense_formations:
        if formation.name == name:
            return formation
    return None
