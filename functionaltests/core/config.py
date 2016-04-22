"""
   production url list of sites

"""
SANOMA_URL = "http://sanoma.nl"
MARGRIET_URL = "http://www.margriet.nl/"
LIBELLE_URL = "http://www.libelle.nl/"

# delay for wait until function
UI_MAX_RESPONSE_TIME = 25.0

# Browserstack credentials:
# USERNAME = 'xxxx', BROWSERSTACK_KEY = 'xxxxx'
USERNAME = 'den377'
BROWSERSTACK_KEY = '6XpuCRXaQtKHWNQfSzz4'

# Browserstack parameters:

# BROWSER = 'IE', 'Edge', 'Firefox', 'Chrome'
BROWSER = 'Edge'

# 'IE': '11.0'
# 'Edge': '12.0'
# 'Firefox': '44.0, '43.0', '42.0', '41.0', '40.0', '39.0', '38.0', '37.0', '36.0', '35.0', '34.0', '33.0', '32.0'
# 'Chrome': '48.0, '47.0', '46.0', '45.0', '44.0', '43.0', '42.0', '41.0', '40.0', '39.0', '38.0', '37.0'
BROWSER_VERSION = '12.0'

# OS = 'Windows', 'OS X'
OS = 'Windows'

# 'Windows' = '10', '8.1', '8', '7', 'XP'
# 'OS X' = 'El Capitan', 'Yosemite', 'Mavericks', 'Mountain Lion'
OS_VERSION = '8'

# '1024x768', '1280x960', '1280x1024', '1600x1200', '1920x1080'
RESOLUTION = '1024x768'

DESIRED_CAP = {'browser': BROWSER,
               'browser_version': BROWSER_VERSION,
               'os': OS,
               'os_version': OS_VERSION,
               'resolution': RESOLUTION
               }

DESIRED_CAP_MOBILE = {'browserName': 'android',
                      'platform': 'ANDROID',
                      'device': 'Samsung Galaxy S5'}

# URL
#BROWSERSTACK_URL = "http://%s:%s@hub.browserstack.com:80/wd/hub" % (USERNAME, BROWSERSTACK_KEY)

