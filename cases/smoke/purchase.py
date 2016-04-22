# -*- coding: utf-8 -*-


from base import *
import os, sys

class Purchase(TestCase):
	
	@logged_in('user')
	@url('/se/buy/')
	def test_purchase(self):
		
		self.assertEqual(u'Vänligen notera att det inte finns några registrerade idrottsföreningar i din stad', self.e('.errors').text)
		self.assertEqual(u'MYNTPAKET', self.e('.buy h3').text)
		self.assertEqual(u'"Mynten" är den virtuella valuta som du använder för att betala till föreningarna. För tillfället är det bara möjligt att köpa standardmynt. Tänk även på att VersaFit är i beta just nu och att priser kan komma att ändras i framtiden.', self.e('.buy h5').text)
		self.assertEqual('20', self.e('.purchase-type-coins h3').text)
		self.assertEqual('179 SEK', self.e('.price').text)
		self.assertEqual(u'K\xd6P', self.e('.purchase-copy').text)
		self.e('.card-inner').click()
		sleep(1)
		
		self.assertEqual(u'BETALNINGSFORMULÄR', self.e('.buy-form h3').text)
		self.assertEqual('http://versafit.test.avalith.bg/se/purchase_conditions/', self.e('.radio-btn-styling a').get_attribute('href'))
		displayed(self, '[name="email"]')
		displayed(self, '[name="country"]')
		displayed(self, '[name="address"]')
		displayed(self, '[name="name"]')
		displayed(self, '[name="city"]')
		displayed(self, '[name="zip"]')
		displayed(self, '.radio-btn-circle')
		displayed(self, '.buy-form [value="Fortsätt"]')
		
		
		
		# test pay card 	q = document.querySelectorAll('#aspnetForm input[type=text], #aspnetForm select'); q[1].value = '4581090329655682'; q[2].value = 'Karamfil'; q[3].value = 2; q[4].value = 2018; q[5].value = 210;