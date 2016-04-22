# -*- coding: utf-8 -*-


from base import *
import os, sys
import logging

class Pages_View(TestCase):
	
	@logged_in('twitter')
	@url('/')
	def test_homepage(self):
		
		self.assertEqual('http://versafit.test.avalith.bg/se/', 									self.e('.header-logo a').get_attribute('href'))
		
		displayed(self, 																			'.icon-whistle')
		displayed(self, 																			'.icon-bubbles4')													# message notifications
		displayed(self, 																			'.profile-subnav-wrapper img')										# user image
		
		self.assertEqual('http://versafit.test.avalith.bg/se/', 									self.e('.site-nav li:nth-of-type(1) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/buy/', 								self.e('.site-nav li:nth-of-type(2) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/profile/kris-test/my_events/', 		self.e('.site-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/', 								self.e('.site-nav li:nth-of-type(4) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/clubs/', 								self.e('.site-nav li:nth-of-type(5) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/aboutus/', 							self.e('.site-nav li:nth-of-type(6) a').get_attribute('href'))
		
		displayed(self, 																			'#language-switcher')
		
		displayed(self, 																			'.social a')
		
		# displayed(self, 																			'.upcoming-event')
		# displayed(self, 																			'.news-item h2')
		
		
		# CONTACT US
		self.assertEqual('http://versafit.test.avalith.bg/se/terms/', 								self.e('.site-footer .links a:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/club_terms/', 							self.e('.site-footer .links a:nth-of-type(3)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/privacy/', 							self.e('.site-footer .links a:nth-of-type(4)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/faq/', 								self.e('.site-footer .links a:nth-of-type(5)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/aboutus/', 							self.e('.site-footer .links a:nth-of-type(6)').get_attribute('href'))
		
		self.assertEqual('http://www.facebook.com/versafitnetwork', 								self.e('.social a:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://www.twitter.com/versafitnetwork', 									self.e('.social a:nth-of-type(2)').get_attribute('href'))
		
		# self.assertEqual('', self.e('.social a:nth-of-type(3)').get_attribute('href'))
		# TO DO site footer google+ link

	@logged_in('twitter')
	@url('/se/sports')
	def test_sports(self):
		
		# self.e_wait('.site-nav a')
		
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/body-weight/',					self.e('.page a:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/boxing/',						self.e('.page a:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/floorball/', 					self.e('.page a:nth-of-type(3)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/futsal/', 						self.e('.page a:nth-of-type(4)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/grappling/', 					self.e('.page a:nth-of-type(5)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/submission-grappling/', 		self.e('.page a:nth-of-type(6)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/crossfit/', 					self.e('.page a:nth-of-type(7)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/football/', 					self.e('.page a:nth-of-type(8)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/gym/', 							self.e('.page a:nth-of-type(9)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/handball/', 					self.e('.page a:nth-of-type(10)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/hockey/', 						self.e('.page a:nth-of-type(11)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/kettlebells/', 					self.e('.page a:nth-of-type(12)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/kickboxing/', 					self.e('.page a:nth-of-type(13)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/volleyball/', 					self.e('.page a:nth-of-type(14)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/se/sports/wrestling/', 					self.e('.page a:nth-of-type(15)').get_attribute('href'))
		
		displayed(self, '.icon-fitness')
		
		self.e('.icon-wrestling').click()
		sleep(1)
		
		self.assertEqual(u'Sporten finns inte tillgänglig nära dig', self.e('.field-wrapper p:nth-of-type(1)').text)
		self.assertEqual(u'Om du skulle vilja att vi lägger till den här sporten, låt oss veta genom att trycka på "Visa intresse" nedan.', self.e('.field-wrapper p:nth-of-type(2)').text)
		displayed(self, '[value="Visa intresse"]')
		
	@url('/en/clubs/')
	def test_clubs(self):
			
		self.e('[href="/en/club/kris-test-club/"]').click()
		self.e_wait('.club-info')
		
		displayed(self, '.club-logo img')
		displayed(self, '.club-info-wrapper p')
		displayed(self, '.news-title-container h2')
		displayed(self, '.news-item p')
		self.e('[href="/en/club/kris-test-club/boxing/"]').click()
		# displayed(self, '.icon-boxing')
		# displayed(self, '.icon-body-weight')
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
		
		self.assertEqual(u'Kris Test Club\nStockholm', 							self.e('.club-title').text)

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
		displayed(self, 																'[value="Lägg till vän"]')
		displayed(self, 																'.user-info p a')													# social links
		# displayed(self, 																'.carousel a')
		displayed(self, 																'.td-inner')														# user activity 
		displayed(self, 																'.friends-list h5')													# friends number
		displayed(self, 																'.friends-list a')
		displayed(self, 																'.button-centered-wrapper a')										# view all friends
		
		self.e('.user-actions a').click()																													# send a message
		sleep(2)
		
		displayed(self, 																'[name="text"]')
		displayed(self, 																'[value="Skicka"]')
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
		
		instance(self, 																	'[value="2000"]')
		instance(self, 																	'[value="1931"]')
		
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
		
	@logged_in('twitter')
	@url('/en/profile/kris-test/promo_code/')
	def test_promo_code(self):
		
		self.assertEqual('ENTER THE PROMOTIONAL CODE BELOW', self.e('form h3').text)
		self.e('#promo_code').send_keys('<script>alert("OMG");</script>')
		self.e('[value="Submit"]').submit()
		sleep(1)
		
		self.assertEqual('Invalid promo code', self.e('.errors').text)
		
	@logged_in('twitter')
	@url('/se/profile/kris-test/refer_a_friend/')
	def test_refer_friend(self):
		
		self.assertEqual(u'Vårt värvingsprogram är ganska enkelt. Varje användare börjar sin testperiod med 18 standardmynt. Däremot om du istället värvar en vän härigenom så blir deras testperiod 25 mynt istället för 18. Utöver detta så kommer du att få 10 standardmynt när den vän du värvat genomför sitt första köp. Du kan börja värva vänner så fort du genomför ditt första köp.', self.e('.container h5').text)
		self.assertEqual(u'Din väns email:', self.e('[for="email"]').text)
		displayed(self, '#email')
		displayed(self, '[value="Skicka inbjudan"]')
		
	@logged_in('twitter')
	@url('/en/profile/kris-test/transaction_history/')
	def test_transaction_history(self):
		
		self.assertEqual('TRANSACTION HISTORY', self.e('.container h3').text)
		self.assertEqual('Product', 			self.e('.table th:nth-of-type(1)').text)
		self.assertEqual('Token Amount', 		self.e('.table th:nth-of-type(2)').text)
		self.assertEqual('Order ID', 			self.e('.table th:nth-of-type(3)').text)
		self.assertEqual('Transaction ID', 		self.e('.table th:nth-of-type(4)').text)
		self.assertEqual('Total Price', 		self.e('.table th:nth-of-type(5)').text)
		self.assertEqual('Status', 				self.e('.table th:nth-of-type(6)').text)
		self.assertEqual('Date', 				self.e('.table th:nth-of-type(7)').text)
		
		displayed(self, '.table td:nth-of-type(1) div')
		displayed(self, '.table td:nth-of-type(2) div')
		displayed(self, '.table td:nth-of-type(3) div')
		# displayed(self, '.table td:nth-of-type(4) div')
		displayed(self, '.table td:nth-of-type(5) div')
		displayed(self, '.table td:nth-of-type(6) div')
		displayed(self, '.table td:nth-of-type(7) div')
		
		self.e('.button.view-order').click()
		sleep(1)
		
		displayed(self, '#order_dialog .button')
		
		self.assertEqual('Order receipt', self.e('.ui-dialog-title').text)
		
		
		