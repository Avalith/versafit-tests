from base import *
import os, sys

class Add_Event(TestCase):
	
	# @url('/')
	# def club_login(self):
		
	# 	self.e('.login a:nth-of-type(2)').click()
	# 	self.e_wait('[name="email"]')
		
	# 	self.e('[name="email"]').send_keys('kris.versatest@mail.bg')
	# 	self.e('[name="password"]').send_keys('KrisVersa')
	# 	self.e('[type="submit"]').click()
		
	# 	self.e_wait('.logged-user  a')
		
	# 	LOGIN_COOKIES.append(self.browser.get_cookie('fwsess'))
	# 	self.login_cookie_del()
	
	@logged_in('club')
	def test_add_event(self):
		
		# self.e('.sub-nav li:nth-of-type(1) a').click()
		self.e_wait('.fc-left')
		
		self.e('.fc-left button').click()
		sleep(1)
		
		self.e('#title').send_keys("HeavyWeight Beer Cup")
		self.e('#event_sports [value="12"]').click()
		self.e('[name="slots"]').send_keys('10')
		self.e('.filed-wrapper-col #dp-start').click()
		self.e('.ui-datepicker-buttonpane button').click()
		self.e('.ui_tpicker_hour').click()
		self.e('[value="23"]').click()
		self.e('.ui_tpicker_minute_slider').click()
		self.e('.ui_tpicker_minute_slider [value="0"]').click()
		self.e('[data-handler="hide"]').click()
		# self.e('.filed-wrapper-col #dp-end').click()
		# self.e('.ui-datepicker-calendar tr:nth-of-type(5) td').click()
		self.e('#locality').send_keys('stockholm')
		# self.e('[name="repeat"]').click()
		# self.e('[value="weekly"]').click()
		# sleep(1)
		# self.e('[name="repeat_count"]').click()
		# self.e('[value="6"]').click()
		self.e('[value="Create Event"]').click()
		
		sleep(3)
		
		self.delete_event()
	
	@logged_in('club')
	def delete_event(self):
		
		self.e_wait('.fc-view-container')
		
		self.e('[data-full="11:00 PM - 12:00 AM"]').click()
		sleep(1)
		
		self.e('.button.remove').click()
		sleep(1)
		
		self.accept_alert()
		sleep(2)
		
		self.go('/')
		self.e_wait('.upcoming-event tr')
		
		self.assertFalse('HeavyWeight Beer Cup' == self.e('.upcoming-event:first-of-type tr:nth-child(2) td span').text)
		
		
		