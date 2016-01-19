from base import *
import os, sys

class Club_Manage(TestCase):
	
	@logged_in('club') 
	@url('/en/club/manage/')
	def test_calendar_view(self):
		
		self.e('.sub-nav li:nth-of-type(1)').click()
		self.e_wait('.fc-center h2')
		
		displayed(self, '.site-nav a')
		displayed(self, '.fc-today-button')
		displayed(self, '.fc-prev-button')
		displayed(self, '.fc-next-button')
		displayed(self, '.fc-month-button')
		displayed(self, '.fc-agendaWeek-button')
		displayed(self, '.fc-agendaDay-button')
		
	@logged_in('club')
	@url('/en/club/manage/')
	def test_employees_view(self):
		
		self.e('.sub-nav li:nth-of-type(2)').click()
		self.e_wait('.sub-nav-title a')
		
		self.e('[type="search"]').send_keys('Asen Lazarov')
		sleep(1)
		
		self.e('.select2-results li').click()
		
		displayed(self, '.list-item img')
		self.assertEqual('ASEN LAZAROV', self.e('.list-item h5').text)
		displayed(self, '[name="role"]')
		displayed(self, '.select-style [name="sport_id"]')
		instance(self, '[value="coach"]')
		instance(self, '[value="supervisor"]')
		instance(self, '[value="12"]')
		instance(self, '[value="21"]')
		displayed(self, '[type="submit"]')
		
	@logged_in('club')
	@url('/en/club/manage/')
	def test_applications_view(self):
		
		self.e('.sub-nav li:nth-of-type(3)').click()
		self.e_wait('.accepted-status')
		
		self.e('.icon-plus').click()
		self.e_wait('#submit-button')
		
		displayed(self, '.select-style [name="sport_id"]')
		instance(self, '[name="sport_id"] [value="12"]')
		instance(self, '[name="sport_id"] [value="21"]')
		instance(self, '[name="sport_id"] [value="20"]')
		instance(self, '[name="sport_id"] [value="31"]')
		instance(self, '[name="sport_id"] [value="23"]')
		instance(self, '[name="sport_id"] [value="24"]')
		instance(self, '[name="sport_id"] [value="34"]')
		instance(self, '[name="sport_id"] [value="28"]')
		instance(self, '[name="sport_id"] [value="25"]')
		instance(self, '[name="sport_id"] [value="11"]')
		instance(self, '[name="sport_id"] [value="16"]')
		instance(self, '[name="sport_id"] [value="13"]')
		instance(self, '[name="sport_id"] [value="29"]')
		instance(self, '[name="sport_id"] [value="18"]')
		displayed(self, '[name="price"]')
		instance(self, '[name="price"] [value="1"]')
		instance(self, '[name="price"] [value="20"]')
		instance(self, '[name="price"] [value="50"]')
		instance(self, '[name="price"] [value="100"]')
		displayed(self, '#locality')
		displayed(self, '#map')
		displayed(self, '[name="requirements"]')
		displayed(self, '[name="description"]')
		displayed(self, '.button.bg-blue')
		self.e('[type="file"]').send_keys('/Users/kris/Downloads/index.jpg')
		displayed(self, '.MultiFile-label img')
		displayed(self, '.MultiFile-remove')
		
	@logged_in('club')
	@url('/en/club/manage/')
	def test_history_view(self):
		
		self.e('.sub-nav li:nth-of-type(4)').click()
		self.e_wait('.upcoming-event')
		
		displayed(self, '#filter_sports')
		instance(self, '#filter_sports [value=""]')
		instance(self, '#filter_sports [value="12"]')
		instance(self, '#filter_sports [value="21"]')
		displayed(self, '#filter_days')
		instance(self, '#filter_days [value="0"]')
		instance(self, '#filter_days [value="1"]')
		instance(self, '#filter_days [value="2"]')
		instance(self, '#filter_days [value="3"]')
		instance(self, '#filter_days [value="4"]')
		instance(self, '#filter_days [value="5"]')
		instance(self, '#filter_days [value="6"]')
		displayed(self, '.table tr td:nth-of-type(1)')
		displayed(self, '.table tr td:nth-of-type(2)')
		displayed(self, '.table tr td:nth-of-type(3)')
		
		
		