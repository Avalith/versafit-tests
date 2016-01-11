from base import *
import os, sys

class Edit_Profile(VFTestCase):
	
	@logged_in
	@url('/en/profile/kris-test/edit/')
	def test_edit_profile(self):
		
		self.e_wait('.profile-img-wrapper img')
		
		self.assertEqual('Kris Test', self.e('.logged-username').text)
		self.e('[name="data[name]"]').send_keys(' Changes')
		self.e('[name="data[auth][email]"]').send_keys('versa.test@mail.bg')
		self.e('[value="BG"]').click()
		self.e('[name="data[city]"]').send_keys('Sofia')
		self.e('[name="data[address]"]').send_keys('`,./<>?;:|[]{}!@#$%^&*()-_+=')
		self.e('[name="data[postcode]"]').send_keys('123')
		self.e('[value="1901"]').click()
		self.e('#months [value="01"]').click()
		self.e('#days [value="01"]').click()
		
		self.e('[value="Save"]').click()
		
		sleep(3)