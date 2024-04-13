from . import situation as s, formation as f, play as p
import json
import os


class Game:
    def __init__(self, opp, location, home_team):
        self.opp = opp
        self.location = location
        self.home_team = home_team

        self.situation = s.Situation()

        # Current team formations
        self.other_formation = None
        self.current_formation = None

        # Array of predicted plays
        self.predictions = []

        # Array of plays that have been run
        self.plays = []

        # Array of formations that can be selected along with their suggested weights
        # Initalize to all formations with equal weight
        self.formations = []

        # Make initial prediction
        self.predict()

    # Call after a play is run
    def addPreviousPlay(self, play):
        self.plays.append((play, self.situation))
        self.predict()

    # Call after the other team gets in formation
    def updateOtherFormation(self, other_formation_name: str):
        self.other_formation = f.findFormation(other_formation_name)
        self.predict()

    # Call when your team selects a formation
    def updateCurrentFormation(self, formation_name: str):
        self.current_formation = f.findFormation(formation_name)
        self.predict(False)

    def updateScore(self, score):
        self.situation.home_score = score[0]
        self.situation.away_score = score[1]
        self.predict()

    def updatePossession(self, possession):
        self.situation.is_possessing_team = possession
        self.predict()

    def updatePosition(self, position):
        self.situation.position.distance = position[0]
        self.situation.position.down = position[1]
        self.situation.position.yard = position[2]
        self.predict()

    def predict(self, predict_suggested_formations=True):
        # TODO: Actually predict. Take in situation, current formation, other formation, and previous plays
        if self.situation.is_possessing_team:
            # Your team is possessing the ball
            # Suggest a list of offensive formations (based on situation, defense's formation, current offensive formation, and previous plays)
            self.predictions = p.offense_plays

            # Suggest a list of offensive formations (based on situation, defense's formation, and previous plays)
            if predict_suggested_formations:
                self.formations = f.offense_formations
        else:
            # Your team is not possessing the ball
            # Suggest a list of offensive plays that the other team is likely to run (based on situation, defense's formation, current offensive formation, and previous plays)
            self.predictions = p.offense_plays

            # Suggest a defensive formation (based on situation, offense's formation, and previous plays)
            if predict_suggested_formations:
                self.formations = f.defense_formations

        # Sort the arrays
        self.predictions.sort(key=lambda x: x.weight, reverse=True)
        if predict_suggested_formations:
            self.formations.sort(key=lambda x: x.weight, reverse=True)

    def jsonPredictions(self):
        return json.dumps(
            self.predictions, default=lambda o: o.__dict__, sort_keys=True, indent=4
        )

    def jsonFormations(self):
        return json.dumps(
            self.formations, default=lambda o: o.__dict__, sort_keys=True, indent=4
        )

    def getFootageForPlay(self, play: int):
        video_paths = ["/static/videos/placeholder.mp4"]
        if os.path.exists(f"./static/videos/2024/BadTeam/10-10-24-7-00/{play}/"):
            video_paths = os.listdir(f"/static/videos/2024/BadTeam/10-10-24-7-00/{play}/")
        return video_paths

def initGame():
    global game
    game = Game("BadTeam", "GoodTeam", True)
