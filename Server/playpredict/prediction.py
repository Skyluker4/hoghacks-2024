import json


class Prediction:
    def __init__(self, formation, play, confidence):
        self.formation = formation
        self.play = play
        self.confidence = confidence

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
