from base import *
import os, sys

class Club_Manage(VFTestCase):
	
	@url('/')
	def club_login(self):
		
		self.e('.login a:nth-of-type(2)').click()
		self.e_wait('[name="email"]')
		
		self.e('[name="email"]').send_keys('kris.versatest@mail.bg')
		self.e('[name="password"]').send_keys('KrisVersa')
		self.e('[type="submit"]').click()
		
		self.e_wait('.logged-user  a')
		
		LOGIN_COOKIES.append(self.browser.get_cookie('fwsess'))
		self.login_cookie_del()
		
	def test_applications(self):
		
		self.club_login()
		
		self.e('.sub-nav li:nth-of-type(3) a').click()
		self.e_wait('#filter_sports')
		
		