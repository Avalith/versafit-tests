from base import *
import os, sys

class Purchase(TestCase):
	
	@logged_in('user')
	@url('/en/buy/')
	def test_purchase(self):
		
		self.assertEqual('Please note that there are no clubs registered within your city', self.e('.errors').text)
		self.assertEqual('TOKEN BATCHES', self.e('.buy h3').text)
		self.assertEqual(u'\u201cTOKENS\u201d ARE THE VIRTUAL CURRENCY YOU USE TO PAY CLUBS. CURRENTLY, ONLY THE STANDARD TOKENS ARE AVAILABLE FOR PURCHASE.\nPLEASE, KEEP IN MIND VERSAFIT IS IN BETA AND PRICES MIGHT CHANGE IN THE FUTURE.', self.e('.buy h5').text)
		self.assertEqual('20', self.e('.purchase-type-coins h3').text)
		self.assertEqual('179 SEK', self.e('.price').text)
		self.assertEqual('PURCHASE', self.e('.purchase-copy').text)
		self.e('.card-inner').click()
		sleep(1)
		
		self.assertEqual('PURCHASE FORM', self.e('.buy-form h3').text)
		self.assertEqual('http://versafit.test.avalith.bg/en/purchase_conditions/', self.e('.radio-btn-styling a').get_attribute('href'))
		displayed(self, '[name="email"]')
		displayed(self, '[name="country"]')
		displayed(self, '[name="address"]')
		displayed(self, '[name="name"]')
		displayed(self, '[name="city"]')
		displayed(self, '[name="zip"]')
		displayed(self, '.radio-btn-circle')
		displayed(self, '.buy-form [type="Submit"]')