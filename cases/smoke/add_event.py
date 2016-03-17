from base import *
import os, sys
import logging

class Add_Event(TestCase):
	
	@logged_in('club')
	@url('/en/club/manage/calendar')
	def test_add_event(self):
		
		self.e_wait('.fc-left')											# add event
		
		self.e('.fc-add-button').click()								# add event
		sleep(1)
		
		self.e('#title').send_keys("HeavyWeight Beer Cup")
		self.e('#event_sports [value="12"]').click()
		self.e('[name="slots"]').send_keys('10')
		self.e('.filed-wrapper-col #dp-start').click()
		self.e('.ui-datepicker-buttonpane button').click()				# now button
		self.e('.ui_tpicker_hour').click()
		self.e('[value="23"]').click()
		self.e('.ui_tpicker_minute_slider').click()
		self.e('.ui_tpicker_minute_slider [value="0"]').click()
		self.e('[data-handler="hide"]').click()							# done button
		self.e('#locality').send_keys('stockholm')
		
		displayed(self, 		'[name="repeat"]')
		instance(self, 			'[value="weekly"]')
		instance(self, 			'[name="repeat_count"]')
		instance(self, 			'[name="repeat_count"] [value="1"]')
		instance(self, 			'[name="repeat_count"] [value="18"]')
		
		# self.e('[name="repeat"]').click()
		# self.e('[value="weekly"]').click()
		# sleep(1)
		# self.e('[name="repeat_count"]').click()
		# self.e('[value="6"]').click()
		
		self.e('.button.create-event').submit()
		
		sleep(3)
		
		self.delete_event()
	
	@logged_in('club')
	def delete_event(self):
		# sleep(1)
		cookie_alert = self.e('.cc_btn')
		
		if cookie_alert:
			self.e('.cc_btn').click()
		
		self.e('[data-full="11:00 PM - 12:00 AM"]').click()
		sleep(1)
		
		self.e('.button.remove').click()
		sleep(1)
		
		self.accept_alert()
		sleep(2)
		
		self.go('/')
		# self.e_wait('.upcoming-event tr')
		
		# self.assertFalse('HeavyWeight Beer Cup' == self.e('.upcoming-event:first-of-type tr:nth-child(2) td span').text)
		
		
		