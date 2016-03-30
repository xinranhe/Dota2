import requests
import re
import urllib

from util import item_dict

for item_id in item_dict.keys():
	item_name = item_dict[item_id]
	url = 'http://media.steampowered.com/apps/dota2/images/items/%s_lg.png' % item_name
	file_path = 'result/items/%s.png' % item_name
	try:
		urllib.urlretrieve(url, file_path)
		print 'succeeded in downloading %s' % item_name
	except:
		print 'failed in downloading %s' % item_name