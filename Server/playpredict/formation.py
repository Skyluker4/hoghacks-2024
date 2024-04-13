import os
import json


class Formation:
    def __init__(self, name, weight=1.0):
        self.name = name
        self.weight = weight
        # Check if formation has an image file, otherwise use placeholder
        if os.path.exists(f"./static/img/formation/{name}.svg"):
            self.image = f"/static/img/{name}.svg"
        else:
            self.image = "/static/img/placeholder.svg"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

offense_formations = [
    Formation("I Formation"),
    Formation("Singleback Formation"),
    Formation("Shotgun Formation"),
    Formation("Pistol Formation"),
    Formation("Empty Formation"),
    Formation("Wildcat Formation"),
]

defense_formations = [
    Formation("4-3 Formation"),
    Formation("3-4 Formation"),
    Formation("Nickel Formation"),
    Formation("Dime Formation"),
    Formation("Quarter Formation"),
    Formation("Goal Line Formation"),
]

def findFormation(name):
    for formation in offense_formations:
        if formation.name == name:
            return formation
    for formation in defense_formations:
        if formation.name == name:
            return formation
    return None