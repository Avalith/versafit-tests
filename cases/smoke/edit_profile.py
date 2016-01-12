from base import *
import os, sys

class Edit_Profile(VFTestCase):
	
	@logged_in
	@url('/en/profile/kris-test/edit/')
	def test_edit_profile(self):
		
		self.e_wait('.profile-img-wrapper img')
		
		self.assertEqual('Kris Test', self.e('.logged-username').text)
		self.e('.sport-wrapper-inner a').click()
		sleep(1)
		
		self.e('.sport-wrapper-inner a').click()
		sleep(1)
		
		self.e('.icon-close').click()
		sleep(1)
		
		self.e('[name="data[name]"]').send_keys(' Changes')
		self.e('[value="BG"]').click()
		self.e('[name="data[city]"]').clear()
		self.e('[name="data[city]"]').send_keys('Sofia')
		self.e('[name="data[address]"]').send_keys('`,./<>?;:|[]{}!@#$%^&*()-_+=')
		self.e('[name="data[postcode]"]').send_keys('123')
		self.e('[value="1901"]').click()
		self.e('#months [value="01"]').click()
		self.e('#days [value="01"]').click()
		
		displayed(self, '[name="social_media[facebook][url]"]')
		displayed(self, '[name="social_media[twitter][url]"]')
		displayed(self, '[name="social_media[google_plus][url]"]')
		displayed(self, '[name="social_media[instagram][url]"]')
		displayed(self, '.links a:nth-of-type(3)')
		self.e('[value="Save"]').click()
		
		sleep(3)
		
		self.edit_clear()
		
	@logged_in
	@url('/en/')
	def edit_clear(self):
		
		self.e_wait('.logged-user-img')
		self.e('.profile-subnav-wrapper a').click()
		self.e_wait('.user-image-wrapper img')
		
		self.e('.user-actions a').click()
		self.e_wait('.profile-img-wrapper img')
		
		self.assertEqual('Kris Test Changes', self.e('[name="data[name]"]').get_attribute('value'))
		
		self.e('[name="data[name]"]').clear()
		self.e('[name="data[name]"]').send_keys('Kris Test')
		self.e('[value="SWE"]').click()
		self.e('[name="data[city]"]').clear()
		self.e('[name="data[city]"]').send_keys('IceHotel')
		self.e('[name="data[address]"]').clear()
		self.e('[name="data[postcode]"]').clear()
		self.e('[name="data[postcode]"]').send_keys('98191')
		self.e('[value="2016"]').click()
		self.e('#months [value="12"]').click()
		self.e('#days [value="31"]').click()
		self.e('.select2:nth-of-type(1) .select2-search__field').click()
		self.e('#select2-user_sport-results li:nth-of-type(1)').click()
		self.e('.select2:nth-of-type(1) .select2-search__field').click()
		self.e('#select2-user_sport-results li:nth-of-type(2)').click()
		self.e('.select2:nth-of-type(2) .select2-search__field').click()
		self.e('#select2-club_subscriptions-results li:nth-of-type(1)').click()
		self.e('[value="Save"]').click()
		
		sleep(3)
		
		
		
		