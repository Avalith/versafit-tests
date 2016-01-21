from base import *
import os, sys
import logging

class Pages_View(TestCase):
	
	@logged_in('twitter')
	@url('/')
	def test_homepage(self):
		
		# self.e_wait('.what-is-versafit')
		
		self.assertEqual('http://versafit.test.avalith.bg/', 							self.e('.header-logo a').get_attribute('href'))
		
		displayed(self, 																'.icon-whistle')
		
		# displayed(self, '.icon-???')			# TO DO after new icon finished
		# TO DO "class social-link"
		
		displayed(self, 																'.profile-subnav-wrapper img')										# user image
		
		self.assertEqual('http://versafit.test.avalith.bg/en/', 						self.e('.site-nav li:nth-of-type(1) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/', 					self.e('.site-nav li:nth-of-type(2) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/clubs/', 					self.e('.site-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/buy/', 					self.e('.site-nav li:nth-of-type(4) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/faq/', 					self.e('.site-nav li:nth-of-type(5) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/aboutus/', 				self.e('.site-nav li:nth-of-type(6) a').get_attribute('href'))
		
		displayed(self, 																'.polyglot-language-switcher')
		
		# displayed(self, '.at4-share-outer #at4-share') WAIT FOR REPAIR SOCIAL PANEL
		# displayed(self, '.events-table tr')
		# displayed(self, '.attending-table tr')
		
		displayed(self, 																'.upcoming-event')
		displayed(self, 																'.news-item h2')
		
		self.assertEqual('http://versafit.test.avalith.bg/terms', 						self.e('.site-footer .links a:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/privacy', 					self.e('.site-footer .links a:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/faq', 						self.e('.site-footer .links a:nth-of-type(3)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/aboutus', 					self.e('.site-footer .links a:nth-of-type(4)').get_attribute('href'))
		
		# TO DO site footer social-link

	@url('/en/sports')
	def test_sports(self):
		
		# self.e_wait('.site-nav a')
		
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/boxing/',		 	self.e('.page a:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/calisthenics/', 	self.e('.page a:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/crossfit/', 		self.e('.page a:nth-of-type(3)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/fitness/', 			self.e('.page a:nth-of-type(4)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/floorball/', 		self.e('.page a:nth-of-type(5)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/football/', 		self.e('.page a:nth-of-type(6)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/futsal/', 			self.e('.page a:nth-of-type(7)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/handball/', 		self.e('.page a:nth-of-type(8)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/hockey/', 			self.e('.page a:nth-of-type(9)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/ju-jutsu/', 		self.e('.page a:nth-of-type(10)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/kettlebells/', 		self.e('.page a:nth-of-type(11)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/kickboxing/', 		self.e('.page a:nth-of-type(12)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/volleyball/', 		self.e('.page a:nth-of-type(13)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/wrestling/', 		self.e('.page a:nth-of-type(14)').get_attribute('href'))
		
		displayed(self, 																'.links a')

	# @url('/')
	def test_search_club(self):
		
		self.e('.search-menu a').click()
		self.e('.select2-selection').click()
		self.e('.select2-search__field').send_keys('kristestclub')
		sleep(1)
		
		self.e('.select2-results__option').click()
		sleep(1)
		
		self.assertEqual('KrisTestClub', 												self.e('.club-title').text)

	@logged_in('twitter')
	# @url('/')
	def test_search_user(self):
		# sleep(1)
		
		self.e('.search-menu a').click()
		self.e('.select2-selection').click()
		self.e('.select2-search__field').send_keys('Nikolay Furnadzhiev')
		sleep(1)
		
		self.e('.select2-results__option img').click()
		self.e_wait('.user-name')
		
		self.assertEqual('Nikolay Furnadzhiev', 										self.e('.user-name').text)
		
		displayed(self, 																'.user-image-wrapper img')
		displayed(self, 																'[value="Invite"]')
		displayed(self, 																'.user-info p a')													# social links
		displayed(self, 																'.user-sports a')
		displayed(self, 																'.Xtd-inner')														# user activity 
		displayed(self, 																'.friends-list h5')													# friends number
		displayed(self, 																'.friends-list a')
		displayed(self, 																'.button-centered-wrapper a')										# view all friends
		
		self.e('.user-actions a').click()																													# send a message
		sleep(2)
		
		displayed(self, 																'[name="text"]')
		displayed(self, 																'[value="Send"]')
		displayed(self, 																'.send-message h5')													# previous messages

	@url('/en/register')
	def test_reg_acount(self):
		
		self.e('.login a').click()
		self.e_wait('#name')
		
		displayed(self, 																'#username')
		displayed(self, 																'#email')
		displayed(self, 																'#country')
		
		instance(self, 																	'[value="AF"]')
		instance(self, 																	'[value="ZW"]')
		
		self.e('[value="BG"]').click()
		
		displayed(self, 																'#city')
		displayed(self, 																'#locality')
		displayed(self, 																'#years')
		
		instance(self, 																	'[value="2016"]')
		instance(self, 																	'[value="1901"]')
		
		displayed(self, 																'#months')
		
		instance(self, 																	'#months [value="01"]')
		instance(self, 																	'#months [value="12"]')
		
		displayed(self, 																'#days')
		
		instance(self, 																	'#days [value="01"]')
		instance(self, 																	'#days [value="31"]')
		
		displayed(self, 																'#personal_number')
		displayed(self, 																'#password')
		displayed(self, 																'#password-confirmation')

	# @logged_in('wronguser')
	# def test_wrong_user(self): #TO DO
		
		
		
		