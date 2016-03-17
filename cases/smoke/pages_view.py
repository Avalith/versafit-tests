from base import *
import os, sys
import logging

class Pages_View(TestCase):
	
	@logged_in('twitter')
	@url('/')
	def test_homepage(self):
		
		self.assertEqual('http://versafit.test.avalith.bg/en/', 									self.e('.header-logo a').get_attribute('href'))
		
		displayed(self, 																			'.icon-whistle')
		
		displayed(self, 																			'.icon-bubbles4')													# message notifications
		
		# TO DO "class social-link"
		
		displayed(self, 																			'.profile-subnav-wrapper img')										# user image
		
		self.assertEqual('http://versafit.test.avalith.bg/en/', 									self.e('.site-nav li:nth-of-type(1) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/buy/', 								self.e('.site-nav li:nth-of-type(2) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/profile/kris-test/my_events/', 		self.e('.site-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/', 								self.e('.site-nav li:nth-of-type(4) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/clubs/', 								self.e('.site-nav li:nth-of-type(5) a').get_attribute('href'))
		# self.assertEqual('http://versafit.test.avalith.bg/en/faq/', 								self.e('.site-nav li:nth-of-type(6) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/aboutus/', 							self.e('.site-nav li:nth-of-type(6) a').get_attribute('href'))
		
		displayed(self, 																			'#language-switcher')
		
		displayed(self, 																			'.social a')
		
		# displayed(self, 																			'.upcoming-event')
		# displayed(self, 																			'.news-item h2')
		
		self.assertEqual('http://versafit.test.avalith.bg/en/terms/', 								self.e('.site-footer .links a:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/club_terms/', 							self.e('.site-footer .links a:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/privacy/', 							self.e('.site-footer .links a:nth-of-type(3)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/faq/', 								self.e('.site-footer .links a:nth-of-type(4)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/aboutus/', 							self.e('.site-footer .links a:nth-of-type(5)').get_attribute('href'))
		
		# TO DO site footer social-link

	@url('/en/sports')
	def test_sports(self):
		
		# self.e_wait('.site-nav a')
		
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/body-weight/',					self.e('.page a:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/boxing/',						self.e('.page a:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/crossfit/', 					self.e('.page a:nth-of-type(3)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/floorball/', 					self.e('.page a:nth-of-type(4)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/football/', 					self.e('.page a:nth-of-type(5)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/futsal/', 						self.e('.page a:nth-of-type(6)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/grappling/', 					self.e('.page a:nth-of-type(7)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/handball/', 					self.e('.page a:nth-of-type(8)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/hockey/', 						self.e('.page a:nth-of-type(9)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/kickboxing/', 					self.e('.page a:nth-of-type(10)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/volleyball/', 					self.e('.page a:nth-of-type(11)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/wrestling/', 					self.e('.page a:nth-of-type(12)').get_attribute('href'))
		
		displayed(self, 																			'.links a')

	@url('/en/clubs/')
	def test_clubs(self):
			
		self.e('[href="/en/club/kris-test-club/"]').click()
		self.e_wait('.club-info')
		
		displayed(self, '.club-logo img')
		displayed(self, '.news-item p')
		self.e('[href="/en/club/kris-test-club/kickboxing/"]').click()
		displayed(self, '.icon-boxing')
		displayed(self, '.icon-body-weight')
		displayed(self, '.people-list a')
		displayed(self, '.page-description p')
		displayed(self, '#calendar.container')
		
		self.e_wait('.flex-active-slide img')

	# @url('/')
	def test_search_club(self):
		
		self.e('.search-menu a').click()
		self.e('.select2-selection').click()
		self.e('.select2-search__field').send_keys('kris test club')
		sleep(1)
		
		self.e('.select2-results__option').click()
		sleep(1)
		
		displayed(self, 																'[action="/en/club/kris-test-club/"]')
		# self.assertEqual('Kris Test Club\nJukkasj\xe4rvi', 								self.e('.club-title').text)

	@logged_in('twitter')
	# @url('/')
	def test_search_user(self):
		# sleep(1)
		
		self.e('.search-menu a').click()
		self.e('.select2-selection').click()
		self.e('.select2-search__field').send_keys('Kris Versa')
		sleep(2)
		
		self.e('.select2-results__option img').click()
		self.e_wait('.user-name')
		
		self.assertEqual('Kris Versa', 													self.e('.user-name').text)
		
		displayed(self, 																'.user-image-wrapper img')
		displayed(self, 																'[value="Add friend"]')
		displayed(self, 																'.user-info p a')													# social links
		displayed(self, 																'.carousel a')
		displayed(self, 																'.Xtd-inner')														# user activity 
		displayed(self, 																'.friends-list h5')													# friends number
		displayed(self, 																'.friends-list a')
		displayed(self, 																'.button-centered-wrapper a')										# view all friends
		
		self.e('.user-actions a').click()																													# send a message
		sleep(2)
		
		displayed(self, 																'[name="text"]')
		displayed(self, 																'[value="Send"]')
		displayed(self, 																'.send-message h5')													# previous messages

	@url('/')
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
		
		# displayed(self, 																'#personal_number')
		displayed(self, 																'#password')
		displayed(self, 																'#password-confirmation')
	
	@logged_in('wronguser')
	def test_wrong_user(self):
		
		self.assertEqual('Wrong username/email or password', self.e('.errors').text)
		
		
		
		