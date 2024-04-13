import os
import json

class Formation:
	def __init__(self, name):
		self.name = name
		# Check if formation has an image file, otherwise use placeholder
		if os.path.exists(f'./static/images/{name}.png'):
			self.image = f'images/{name}.png'
		else:
			self.image = 'images/placeholder.png'

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
