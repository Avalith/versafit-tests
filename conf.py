
PATH_CRHOME_DRIVER	= 'chromedriver'
GO_TIMEOUT = 1

# VERSION = 'v75-beta-2'

# LINK_BASE = 'historypin.org'
# LINK_BASE = '{0}.historypin-hrd.appspot.com'.format(VERSION)

URL_BASE = 'http://versafit.test.avalith.bg'
# URL_BLOB = 'http://{0}'.format(LINK_BASE)
# PROTOCOL = URL_BASE.split('://')[0]


# IS_ON_SDK	= not (LINK_BASE.endswith('.appspot.com') or LINK_BASE.endswith('historypin.com'))
# IS_LIVE		= LINK_BASE.endswith('http://www.versafit.com')

ID_USER			= 65536


LOGIN_DETAILS = {
	'club'			: { 'type': 'standard'		, 'user': 'kris.versatest@mail.bg'		, 'pass': 'KrisVersa', },
	'user'			: { 'type': 'standard'		, 'user': ''							, 'pass': '', },
	'coach'			: { 'type': 'standard'		, 'user': ''							, 'pass': '', },
	'supervisor'	: { 'type': 'standard'		, 'user': ''							, 'pass': '', },
	'facebook'		: { 'type': 'facebook'		, 'user': ''							, 'pass': '', },
	'twitter'		: { 'type': 'twitter'		, 'user': 'kris.yanachkov@gmail.com'	, 'pass': 'bind7ultimate', },
	'googleplus'	: { 'type': 'googleplus'	, 'user': ''							, 'pass': '', },
	'wronguser'		: { 'type': 'standart'		, 'user': 'wronguser'					, 'pass': 'highsecurity', },
}