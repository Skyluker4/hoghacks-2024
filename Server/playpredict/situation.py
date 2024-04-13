import time as t
import json
from . import position


class Situation:

    def __init__(
        self,
        time=t.strptime("15:00", "%M:%S"),
        quarter=1,
        home_score=0,
        away_score=0,
        is_possessing_team=False,
    ):
        self.time = time
        self.quarter = quarter
        self.home_score = home_score
        self.away_score = away_score
        self.position = position.Position()
        self.is_possessing_team = is_possessing_team

    def toJSON(self):
        json_dat = json.dumps(
            self, default=lambda o: o.__dict__, sort_keys=True, indent=4
        )
        # Replace "time" with a formatted string in the form m:SS
        json_obj = json.loads(json_dat)
        json_obj["time"] = t.strftime("%M:%S", self.time)
        new_json_dat = json.dumps(
            json_obj, default=lambda o: o.__dict__, sort_keys=True, indent=4
        )
        return new_json_dat
