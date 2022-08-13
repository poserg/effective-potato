import unittest

from potato import get_active_categories, Category

class TestGetActiveCategory(unittest.TestCase):


	def test_get_zero_active_categories(self):
		result = get_active_categories([
			Category('category 1', 1000),
			Category('category 2', 1500)
			],
			500)
		self.assertEqual(result, [])

	def test_get_some_active_categories(self):
		expected_category = Category('category 1', 1000)
		result = get_active_categories([
			expected_category,
			Category('category 2', 1500)
			],
			1200)
		self.assertEqual(result, [expected_category])
