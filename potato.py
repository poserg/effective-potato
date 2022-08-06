class Category:
	def __init__(self, title, sum, account_guid):
		self.title = title
		self.sum = sum
		self.account_guid = account_guid

def get_active_categories(all_catetories, sum):
	return [x for x in all_catetories if x.sum <= sum]