from . import situation, position, formation, prediction

class Game:
	def __init__(self, opp, location, home_team):
		self.opp = opp
		self.location = location
		self.home_team = home_team

		self.situation = situation.Situation()
		self.position = position.Position()
		self.other_formation = formation.Formation("Test Formation")
		self.predictions = []

		self.plays = []

		# [(Formation, Weight)]
		self.formations = []

		# Make initial prediction
		self.predict()

	def addPlay(self):
		pass

	def predict(self):
		pass
