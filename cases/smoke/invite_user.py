from base import *
import os, sys
import logging

class Invite_User(TestCase):
	
	@logged_in('twitter')
	@url('/')
	def test_invite_user(self):
		
		self.e('.search-menu a').click()
		self.e('.select2-selection').click()
		self.e('.select2-search__field').send_keys('Kris Versa')
		sleep(1)
		
		self.e('.select2-results__option img').click()
		self.e_wait('.user-name')
		
		self.assertEqual('Kris Versa', self.e('.user-name').text)
		
		self.e('[value="Add friend"').click()
		sleep(1)
		
		self.del_cookie('fwsess')
		
		self.accept_delete_invite()
		
	@logged_in('facebook')
	@url('/')
	def accept_delete_invite(self):
		
		self.e('.icon-whistle').click()
		sleep(1)
		
		self.e('.accept').click()
		self.e('.logged-username').click()
		self.e_wait('.button-centered-wrapper')								# all friends
		
		self.assertEqual('Kris Test', self.e('.friend-name').text)
		
		self.e('.button-centered-wrapper').click()							# all friends
		sleep(1)
		
		self.e('.friend-actions .button').click()							# delete friend
		sleep(1)
		
		self.accept_alert()
		self.e_wait('.friends-list h5')
		
		self.assertEqual('FRIENDS / 0 /', self.e('.friends-list h5').text)
		
