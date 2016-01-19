import unittest

from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.alert import Alert
import logging


from conf import *

def web_element_exists(self, selector):
	try:
		self.e(selector)
		return True
	except NoSuchElementException:
		return False


WebElement.e 			= WebElement.find_element_by_css_selector
WebElement.es 			= WebElement.find_elements_by_css_selector
WebElement.css 			= WebElement.value_of_css_property
WebElement.exists 		= web_element_exists
WebElement.parent_node 	= lambda self: self.find_element_by_xpath('./parent::node()')


def displayed(self, selector):
	self.assertTrue(self.e(selector).is_displayed())

def instance(self, selector):
	self.assertIsInstance(self.e(selector), WebElement)

def url(url):
	def wrapper(fn):
		def wrapped(*args, **kwargs):
			args[0].go(url)
			
			sleep(1)
			
			fn(*args, **kwargs)
		return wrapped
	return wrapper


# def logged_in(fn):
# 	def wrapped(*args, **kwargs):
# 		args[0].login_cookie_set()
# 		fn(*args, **kwargs)
# 		args[0].login_cookie_del()
# 	return wrapped



LOGIN_COOKIES = {}

def logged_in(login_type):
	def wrapper(fn):
		def wrapped(*args, **kwargs):
			opts = LOGIN_DETAILS[login_type]
			
			cls = args[0]
			cls.login_cookie_set(login_type, opts)
			
			fn(*args, **kwargs)
			
			cls.login_cookie_del()
		return wrapped
	return wrapper

class Logins:
	# def logout(self):
	# 	self.go(URL_BASE + '/user/logout/')
	# 	self.pageload_wait()
	
	@classmethod
	def login_cookie_set(cls, login_type, opts):
		cookie = LOGIN_COOKIES.get(login_type)
		
		if cookie:
			cls.login_cookie_del()
			cls.browser.add_cookie(cookie)
		else:
			getattr(cls, 'login_method_' + opts['type'])(opts)
			
			LOGIN_COOKIES[login_type] = cls.browser.get_cookie('fwsess')
			
			sleep(.5)
	
	@classmethod
	def login_cookie_del(cls):
		cls.browser.delete_cookie('fwsess')
	
	@classmethod
	def login_method_standard(cls, opts):
		cls.go('/en/login/')
		
		cls.e('input[name=email]').send_keys(opts['user'])
		cls.e('input[name=password]').send_keys(opts['pass'])
		
		cls.e('input[type=submit]').click()
	
	# fb
	
	@classmethod
	def login_method_twitter(cls, opts):
		cls.e('.login a:nth-of-type(2)').click()
		cls.e('.alternative-login a:nth-of-type(2)').click()
		sleep(2)
		
		cls.e('#username_or_email')
		cls.e('#password').send_keys(opts['pass'])
		cls.e('.submit').click()
		
		# sleep(12)
		cls.e_wait('.logged-username')
	
	# gp


# class Browser(webdriver.Firefox):
class Browser(webdriver.Chrome):
	def go(self, url):
		self.get(('' if url.startswith('http') else URL_BASE) + url)
		self.pageload_wait()
		# sleep(1)
	
	def es(self, selector):
		return self.find_elements_by_css_selector(selector)
	
	exists = web_element_exists
	
	def e(self, selector):
		return self.find_element_by_css_selector(selector)
	
	def e_wait(self, selector, timeout = 30):
		try:
			w = WebDriverWait(self, timeout)
			return w.until(lambda driver: driver.e(selector))
		except:
			raise NoSuchElementException('The element could not be found')
	
	def pageload_wait(self, timeout = 30):
		sleep(1)
		# TODO Fix this to work with something else than dummy sleep
		# self.e_wait('body')
		# try:
		# 	w = WebDriverWait(self, timeout)
		# 	return w.until(lambda driver: driver.execute_script("return document.readyState;") == "complete")
		# except:
		# 	raise Exception('Page could not load')
	
	def hover(self, elem):
		ActionChains(self).move_to_element(elem).perform()
		sleep(.5)
	
	def double_click(self, elem):
		ActionChains(self).double_click(elem).perform()
		sleep(.5)  # TODO is this necessary
	
	def click_xy(self, elem, x, y):
		ActionChains(self).move_to_element_with_offset(elem, x, y).click().perform()
		sleep(.5)  # TODO is this necessary
		
	def accept_alert(self):
		alert = self.switch_to_alert()
		alert.accept()



def run(*tests):
	import cases
	
	suite = unittest.TestSuite()
	
	if tests:
		for i in tests:
			i = i.split('.')
			
			test_case = getattr(cases, i[0])
			if len(i) > 1:
				suite.addTest(test_case(i[1]))
			else:
				suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_case))
	else:
		suite.addTests(unittest.TestLoader().loadTestsFromModule(cases))
	
	# TestCase.browser_start(Browser())

	from selenium.webdriver.chrome.options import Options
	opts = Options()
	# opts.add_argument("--start-fullscreen")
	opts.add_argument("--maximize")

	TestCase.browser_start(Browser(PATH_CRHOME_DRIVER, chrome_options = opts))
	
	unittest.TextTestRunner(verbosity = 1).run(suite)
	TestCase.browser_close()


class TestCase(unittest.TestCase, Logins):
	@classmethod
	def browser_start(cls, browser):
		cls.browser = browser
		# cls.browser.maximize_window()
		
		cls.go				= cls.browser.go
		cls.refresh			= cls.browser.refresh
		cls.es				= cls.browser.es
		cls.e				= cls.browser.e
		cls.e_wait			= cls.browser.e_wait
		cls.exists			= cls.browser.exists
		# cls.pageload_wait	= cls.browser.pageload_wait
		cls.hover			= cls.browser.hover
		cls.double_click	= cls.browser.double_click
		cls.accept_alert	= cls.browser.accept_alert
	
	@classmethod
	def browser_close(cls):
		cls.browser.quit()
	
	def assertTitle(self, title):
		self.assertIn(title, self.browser.title)


# from base import playground; self = playground()
def playground():
	self = TestCase
	self.browser_start(Browser(PATH_CRHOME_DRIVER))
	self.go('/')
	
	return self


# def side_buttons(self):
# 	s_buttons = [
# 		'.site-toolbar .icon-info', 
# 		'.site-toolbar .icon-share', 
# 		'.site-toolbar .icon-discussion', 
# 		'.site-toolbar .icon-add-collection'
# 	]

# 	for n in range(len(s_buttons)):
# 		i = s_buttons[n]
# 		# logging.critical(i)
# 		self.assertTrue(self.e(i).is_displayed())
# 		# self.assertIsInstance(self.e(i), WebElement)
		
# def side_buttons_profile(self):
# 	sp_buttons = [
# 		'.site-toolbar .icon-edit', 
# 		'.site-toolbar .icon-share', 
# 		'.site-toolbar .icon-discussion', 
# 		'.site-toolbar .icon-add-pin', 
# 		'.site-toolbar .icon-add-collection', 
# 		'.site-toolbar .icon-add-tour'
# 	]
	
# 	for n in range(len(sp_buttons)):
# 		i = sp_buttons[n]
# 		# logging.critical(i)
# 		self.assertTrue(self.e(i).is_displayed())



