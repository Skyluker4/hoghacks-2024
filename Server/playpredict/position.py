class Position:
    def __init__(
        self, yard=0, down=1, distance=10, own_side=True
    ):
        self.yard = yard
        self.down = down
        self.distance = distance

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
