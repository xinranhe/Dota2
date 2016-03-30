from pymongo import MongoClient
import numpy as np 
import scipy as sp 
import cPickle as pickle




client = MongoClient()
collection = client.Dota2.matches

leagueIds = ['3706','3990','3781','3798','3502','3534','3552','2392'];
tierList = [2,1,1,1,1,2,2,1]
allmatches = dict()

for id in leagueIds:
	allmatches[id] = dict();
	allmatches[id]['tier'] = tierList[ leagueIds.index(id) ]
	leaguedata = list()

	visited = set()
	matches = collection.find( {'league_id': int(id) }  )
	for match in matches:
		match_id = match['match_id']
		if match_id in visited:
			pass	# nothing
		else:
			visited.add(match_id)
			try:
				print "processing: ", match_id
				banpick = match['picks_bans']
				matchdata = dict()
				matchdata['match_id'] = match_id				
				matchdata['duration'] = match['duration']		
				matchdata['banpicks'] = np.zeros((20,1))

				for bp in banpick:
					matchdata['banpicks'][ bp['order']   ] = bp['hero_id'] 
				# first ban win = 1
				# first ban lose  = -1
				if (match['radiant_win']) :
					if (banpick[0]['team'] == 0):
						
						matchdata['label'] = 1
					else:
						matchdata['label'] = -1
				else:
					if (banpick[0]['team'] == 0):
						## first pick win = 1
						## first pick lose  = -1
						matchdata['label'] = -1
					else:
						matchdata['label'] = 1
				leaguedata.append(matchdata)
				#print "processed match: ", len(leaguedata)


			except:
				pass 
	
	print "processed match: ", len(leaguedata)
	allmatches[id]['data'] = leaguedata



pickle.dump(allmatches, open('data/allbanpick1105.pkl', 'wb'))













