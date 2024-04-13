from . import situation, formation, prediction, play
import json


class Game:
    def __init__(self, opp, location, home_team):
        self.opp = opp
        self.location = location
        self.home_team = home_team

        self.situation = situation.Situation()
        self.other_formation = formation.Formation("Test Formation")
        # Array of predicted plays
        self.predictions = []

        # Array of plays that have been run
        self.plays = []

        self.formations = []

        # Make initial prediction
        self.predict()

    def addPlay(self):
        pass

    def addCurrentFormation(self):
        pass

    def predict(self):
        # Make the predictions array have 3 predictions
        self.predictions = [
            play.Play(self.other_formation, "Test Play 1", 0.5),
            play.Play(self.other_formation, "Test Play 2", 0.4),
            play.Play(self.other_formation, "Test Play 3", 0.3),
        ]

        # Then sort the predictions by weight, descending
        self.predictions.sort(key=lambda x: x.weight, reverse=True)

    def jsonPredictions(self):
        return json.dumps(
            self.predictions, default=lambda o: o.__dict__, sort_keys=True, indent=4
        )
