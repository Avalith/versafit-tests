from base import *
import os, sys

class Send_Message(TestCase):
	
	@logged_in('user')
	@url('/en/profile/krisemailuser/friend_list/')
	def test_send_message(self):
		global time
		
		self.e('.friend-actions a:nth-of-type(2)').click()
		self.e_wait('.send-message h5')
		
		self.e('[name="text"]').send_keys('Test MEssage! 1234567890-_=+[]{}|;:~`<>,./?')
		self.e('[value="Send"]').submit()
		sleep(2)
		
		time = self.e('.previews-message .meta').text
		
		# self.del_cookie('fwsess')
		
		# self.view_message()
		
	@logged_in('twitter')
	@url('/en/profile/kris-test/messages')
	def test_z_view_message(self):
		
		self.assertEqual('1', self.e('.messages .counter').text)
		self.assertEqual('krisemailuser', self.e('.main-cnt-col-left .message-copy h4').text)
		
		self.e('.main-cnt-col-left .message-copy').click()
		self.e_wait('[name="text"]')
		
		self.assertTrue(time == self.e('.previews-message .meta').text)
		self.assertEqual('Test MEssage! 1234567890-_=+[]{}|;:~`<>,./?', self.e('.previews-message-copy').text)