from base import *
import os, sys

class Employees(TestCase):
	
	@logged_in('club')
	@url('/en/club/manage/employees/')
	def test_add_employee(self):
		self.e('.sidebar-col-right [type="search"]').send_keys('kris versa')
		sleep(1)
		
		self.e('.search-result img').click()
		sleep(1)
		
		self.assertEqual('KRIS VERSA', self.e('.person-item h5').text)
		self.e('[value="Send invitation"]').submit()
		sleep(1)
		
		displayed(self, '.image img')
		self.assertEqual('Kris Versa', 	self.e('tr:nth-of-type(2) td:nth-of-type(2) div').text)
		self.assertEqual('coach', 		self.e('tr:nth-of-type(2) td:nth-of-type(3) div').text)
		self.assertEqual('Boxing', 		self.e('tr:nth-of-type(2) td:nth-of-type(4) div').text)
		self.assertEqual('Remove', 		self.e('tr:nth-of-type(2) td:nth-of-type(6) a').text)
		self.assertEqual('new', 		self.e('tr:nth-of-type(2) .new-status').text)
		
		self.del_cookie('fwsess')
		self.accept_request()
		
	@logged_in('facebook')
	@url('/')
	def accept_request(self):
		
		self.assertEqual('http://versafit.test.avalith.bg/en/club/kris-test-club/',self.e('.request-pending a').get_attribute('href'))
		self.e('.icon-whistle').click()
		sleep(1)
		
		displayed(self, '.request-pending p')
		displayed(self, '.request-pending .delete')
		icon = self.e('.icon-whistle')
		self.hover(icon)
		self.e('.buttons .accept').click()
		sleep(1)
		
		helement = self.e('.logged-username')
		self.hover(helement)
		self.e('[href="/en/profile/kris-versa/coach/"]').click()
		self.e_wait('.container h5')
		
		displayed(self, '.datepicker')
		self.assertEqual('Start Time', 	self.e('.table tr th:nth-of-type(1)').text)
		self.assertEqual('Event Title', self.e('.table tr th:nth-of-type(2)').text)
		self.assertEqual('Club', 		self.e('.table tr th:nth-of-type(3)').text)
		self.assertEqual('Sport', 		self.e('.table tr th:nth-of-type(4)').text)
		self.assertEqual('Slots', 		self.e('.table tr th:nth-of-type(5)').text)
		
		self.del_cookie('fwsess')
		self.delete_coach()
		
	@logged_in('club')
	@url('/en/club/manage/employees/')
	def delete_coach(self):
		
		self.e_wait('.main-cnt-col-left h5')
		
		self.assertEqual('accepted', self.e('.accepted-status').text)
		self.e('tr:nth-of-type(2) td:nth-of-type(6) a').click()
		sleep(1)
		
		self.accept_alert()
		
		
		