class Formation:
	__init__(self, name):
		self.name = name
		# Check if formation has an image file, otherwise use placeholder
		if os.path.exists(f'./static/images/{name}.png'):
			self.image = f'images/{name}.png'
		else:
			self.image = 'images/placeholder.png'
