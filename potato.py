class Category:
	def __init__(self, title, sum):
		self.title = title
		self.sum = sum

def get_active_categories(all_catetories, sum):
	return [x for x in all_catetories if x.sum <= sum]