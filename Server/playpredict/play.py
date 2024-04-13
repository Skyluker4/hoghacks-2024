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
            self.image = "/images/placeholder.png"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
