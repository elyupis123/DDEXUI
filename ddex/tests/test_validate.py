from DDEXUI.ddex.validate import Validate
import unittest

class ValidateTests(unittest.TestCase):
	def test_upcs_must_only_contain_numbers(self):
		result = Validate().upc("abc123456789")
		self.assertEqual(result["error"], "upc must only contain numbers")

	def test_upcs_cannot_contain_less_than_12_digits(self):
		result = Validate().upc("12345")
		self.assertEqual(result["error"], "upc must be 12 - 13 digits long")

	def test_upcs_cannot_contain_more_than_13_digits(self):
		result = Validate().upc("12345678910235")
		self.assertEqual(result["error"], "upc must be 12 - 13 digits long")

	def test_valid_upcs_do_not_return_errors(self):
		result = Validate().upc("123456789012")
		self.assertEqual(result["value"], "123456789012")
		self.assertFalse("error" in result)

	def test_year_must_be_a_number(self):
		result = Validate().year("a")
		self.assertEqual(result["error"], "year must be a number")

	def test_a_valid_year_doesn_not_return_any_errors(self):
		result = Validate().year("2012")
		self.assertEqual(result["value"], 2012)
		self.assertFalse("error" in result)
		