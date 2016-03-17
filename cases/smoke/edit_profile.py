# -*- coding: utf-8 -*-

from base import *
import os, sys
import logging

class Edit_Profile(TestCase):
	
	@logged_in('twitter')
	@url('/en/profile/kris-test/edit/')
	def test_edit_profile(self):
		
		self.e_wait('.profile-img-wrapper img')
		
		self.assertEqual('Kris Test', self.e('.logged-username').text)
		self.e('.sports-container .icon-cross').click()							# remove my sport 1
		sleep(1)
		
		self.e('.sports-container .icon-cross').click()							# remove my sport 2
		sleep(1)
		
		self.e('.sports-container .icon-cross').click()							# remove my subscriptions
		sleep(1)
		
		self.e('[name="data[name][first_name]"]').send_keys('Changes')
		self.e('[name="data[name][last_name]"]').send_keys('Changes')
		self.e('[value="BG"]').click()
		self.e('[name="data[city]"]').clear()
		self.e('[name="data[city]"]').send_keys('Sofia')
		self.e('[name="data[address]"]').send_keys('`,./<>?;:|[]{}!@#$%^&*()-_+=')
		# self.e('[name="data[postcode]"]').send_keys('123')
		self.e('[value="1901"]').click()
		self.e('#months [value="01"]').click()
		self.e('#days [value="01"]').click()
		
		displayed(self, '[name="social_media[facebook][url]"]')
		displayed(self, '[name="social_media[twitter][url]"]')
		displayed(self, '[name="social_media[google_plus][url]"]')
		displayed(self, '[name="social_media[instagram][url]"]')
		displayed(self, '.links a:nth-of-type(3)')
		
		self.e('[value="Save"]').submit()
		
		sleep(3)
		
		self.edit_clear()
		
	@logged_in('twitter')
	@url('/en/profile/kris-test/')
	def edit_clear(self):
		
		self.e_wait('.user-image-wrapper img')
		
		self.e('.user-actions a').click()
		self.e_wait('.profile-img-wrapper img')
		
		self.assertEqual('KrisChanges', self.e('[name="data[name][first_name]"]').get_attribute('value'))
		
		self.e('[name="data[name][first_name]"]').clear()
		self.e('[name="data[name][first_name]"]').send_keys('Kris')
		self.e('[name="data[name][last_name]"]').clear()
		self.e('[name="data[name][last_name]"]').send_keys('Test')
		self.e('[value="SWE"]').click()
		self.e('[name="data[city]"]').clear()
		self.e('[name="data[city]"]').send_keys(u'Jukkasjärvi')
		self.e('[name="data[address]"]').clear()
		self.e('[name="data[address]"]').send_keys('IceHotel')
		# self.e('[name="data[postcode]"]').clear()
		# self.e('[name="data[postcode]"]').send_keys('98191')
		self.e('[value="2016"]').click()
		self.e('#months [value="12"]').click()
		self.e('#days [value="31"]').click()
		
		self.e('.profile-img .select2:nth-of-type(1) .select2-search__field').click()
		self.e('.select2-results__options li:nth-of-type(2)').click()					# add boxing
		self.e('.profile-img .select2:nth-of-type(1) .select2-search__field').click()
		self.e('.select2-results__options li:nth-of-type(10)').click()					# add calisthenics
		self.e('.profile-img .select2:nth-of-type(2) .select2-search__field').click()
		self.e('.select2-results__options li:nth-of-type(4)').click()					# add Kris Test Club
		self.e('[value="Save"]').submit()
		
		sleep(3)
		
		
		
		