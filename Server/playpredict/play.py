import os
import json
import pandas
import random


class Play:
    def __init__(self, formation, name, weight=1.0):
        self.name = name
        self.weight = weight
        self.formation = formation
        # Check if formation has an image file, otherwise use placeholder
        if os.path.exists(f"./static/img/formations/plays/{formation}/{name}.svg"):
            self.image = f"/static/img/formations/plays/{formation}/{name}.svg"
        else:
            # Randomly select /static/img/playplaceholder#.svg where # is 1-4
            self.image = f"/static/img/playplaceholder{random.randint(1, 4)}.jpg"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


data = pandas.read_csv("data/data.tsv", sep="\t")

offense_plays_str = []
defense_plays_str = []
for index, row in data.iterrows():
    offense_plays_str.append((str(row["Offensive Formation"]), str(row["Offensive Play"])))
    if str(row["Defensive Play"]) != "nan":
        defense_plays_str.append((str(row["Defensive Front"]), str(row["Defensive Play"])))
# Only keep unique plays
offense_plays_str = list(set(offense_plays_str))
defense_plays_str = list(set(defense_plays_str))
offense_plays = []
defense_plays = []
for f, p in offense_plays_str:
    offense_plays.append(Play(f, p))
for f, p in defense_plays_str:
    defense_plays.append(Play(f, p))
