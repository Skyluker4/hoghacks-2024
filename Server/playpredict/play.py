import os
import json


class Play:
    def __init__(self, formation, name, weight=1.0):
        self.name = name
        self.weight = weight
        self.formation = formation
        # Check if formation has an image file, otherwise use placeholder
        if os.path.exists(f"./static/images/formations/plays/{formation}/{name}.png"):
            self.image = f"/static/images/formations/plays/{formation}/{name}.png"
        else:
            self.image = "/static/images/placeholder.png"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

offense_plays = [
    Play("I Formation", "Run"),
    Play("I Formation", "PA Pass"),
    Play("I Formation", "Screen Pass"),
    Play("Singleback Formation", "Run")
]

defense_plays = [
    Play("4-3 Formation", "Cover 2"),
    Play("4-3 Formation", "Cover 3"),
    Play("4-3 Formation", "Cover 1")
]
