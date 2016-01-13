from base import *
import os, sys

class Pages_View_Versa(VFTestCase):
	
	@logged_in('user')
	@url('/')
	def test_homepage(self):
		
		self.e_wait('.what-is-versafit')
		
		self.assertEqual('http://versafit.test.avalith.bg/', self.e('.header-logo a').get_attribute('href'))
		displayed(self, '.icon-whistle')
		# displayed(self, '.icon-???')			# TO DO after new icon finished
		# TO DO "class social-link"
		displayed(self, '.profile-subnav-wrapper img')
		self.assertEqual('http://versafit.test.avalith.bg/en/', self.e('.site-nav li:nth-of-type(1) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/', self.e('.site-nav li:nth-of-type(2) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/clubs/', self.e('.site-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/buy/', self.e('.site-nav li:nth-of-type(4) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/faq/', self.e('.site-nav li:nth-of-type(5) a').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/aboutus/', self.e('.site-nav li:nth-of-type(6) a').get_attribute('href'))
		displayed(self, '.polyglot-language-switcher')
		displayed(self, '.at4-share-outer #at4-share')
		# displayed(self, '.events-table tr')
		# displayed(self, '.attending-table tr')
		displayed(self, '.news-item h2')
		self.assertEqual('http://versafit.test.avalith.bg/terms', self.e('.site-footer .links a:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/privacy', self.e('.site-footer .links a:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/faq', self.e('.site-footer .links a:nth-of-type(3)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/aboutus', self.e('.site-footer .links a:nth-of-type(4)').get_attribute('href'))
		
		# TO DO site footer social-link
		# self.e('.search-menu').click()
		
	@url('/en/sports')
	def test_sports(self):
		
		self.e_wait('.site-nav a')
		
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/boxing/', self.e('.page a:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/calisthenics/', self.e('.page a:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/crossfit/', self.e('.page a:nth-of-type(3)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/fitness/', self.e('.page a:nth-of-type(4)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/floorball/', self.e('.page a:nth-of-type(5)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/football/', self.e('.page a:nth-of-type(6)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/futsal/', self.e('.page a:nth-of-type(7)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/handball/', self.e('.page a:nth-of-type(8)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/hockey/', self.e('.page a:nth-of-type(9)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/ju-jutsu/', self.e('.page a:nth-of-type(10)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/kettlebells/', self.e('.page a:nth-of-type(11)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/kickboxing/', self.e('.page a:nth-of-type(12)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/volleyball/', self.e('.page a:nth-of-type(13)').get_attribute('href'))
		self.assertEqual('http://versafit.test.avalith.bg/en/sports/wrestling/', self.e('.page a:nth-of-type(14)').get_attribute('href'))
		displayed(self, '.links a')
		
		
		