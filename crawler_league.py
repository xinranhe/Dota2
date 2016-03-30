from dota2py import api
from dota2py import data
from time import sleep
import cPickle as pickle
import requests
import datetime
import sys
from pymongo import MongoClient
import json
from util import game_mode_dict
import logging

from config import API_KEY

class Dota2MatchCrawler(object):
    def __init__(self, league_id):
        api.set_api_key(API_KEY)

        # start and end sequence number
        self.league_id = league_id
        self.current_match_id = None

        # total games
        self.total_games = 0
        # total slected game
        self.total_selected_games = 0
        # total yasp games
        self.yasp_games = 0
        # logging
        self.logger = logging.getLogger('dota2')
        self.logger.setLevel(logging.INFO)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('log/league_%s.txt' % league_id)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        # init mongo client
        client = MongoClient()
        self.collection = client.Dota2.matches

    def get_game_mode_string(self, game_mode_id):
        try:
            return game_mode_dict[int(game_mode_id)]
        except :
            return 'Unknown mode %s' % game_mode_id

    def getSkillLevel(self, match_id):
        ''' we query dotabuff to obtain the skill level of the match
            3: very high, 2: high, 1: normal, -1: unknown
        '''
        query_url = 'http://dotamax.com/match/detail/%s' % (match_id)
        response = requests.get(query_url)
        if '>Very High</font>' in response.content:
            return 3
        elif '>High</font>' in response.content:
            return 2
        elif '>Normal</font>' in response.content:
            return 1
        else:
            # unknown skill level
            return -1

    def is_valid_match(self, gmd_result):
        '''Returns True if the given match details result should be considered,
        and False otherwise.'''
        try:
            for player in gmd_result['players']:
                if player['leaver_status'] is not 0:
                    return False
            # filer not 10 player game
            if gmd_result['human_players'] != 10:
                return False

            # filter by game mode, consider only All Pick
            #if gmd_result['game_mode'] not in [1]:
            #    return False

            # filter by game duration, at least 25 minutes
            #if gmd_result['duration'] < 1500:
            #    return False
        except:
            return False

        return True

    # current disabled by yasp
    def getMatchDetailFromYasp(self, match_id):
        query_url = 'http://yasp.co/matches/%d?json=1' % (match_id)
        response = requests.get(query_url)
        if response.status_code == 200:
            yasp_dict = json.loads(response.content)
            return (True, yasp_dict)
        else:
            return (False, None)

    def process_match_details(self, match, match_id):
        game_mode = self.get_game_mode_string(match['game_mode'])
        #skill_level = self.getSkillLevel(match_id)
        #match['skill_level'] = skill_level
        start_time = datetime.datetime.fromtimestamp(match['start_time']).strftime('%Y-%m-%d %H:%M:%S')

        #(has_yasp, yasp_dict) = self.getMatchDetailFromYasp(match_id)
        #match['has_yasp'] = has_yasp
        #if has_yasp:
        #    self.logger.info('Yasp game found: %s' % (match_id))
        #    match['yasp_result'] = yasp_dict
        #    self.yasp_games += 1
        match['league_id'] = self.league_id
        self.collection.insert(match)
        self.logger.info('Processed Match ID: %d' % match_id)
        #self.logger.info('Processed Match ID: %s - Game Mode: %s - Skill Level: %d' % (match_id, game_mode, skill_level))

    def getRecentMatches(self, start_match_id):
        try:
            gmh = api.get_match_history(start_at_match_id=start_match_id, league_id=self.league_id)['result']        
        except:
            sleep(5.0)
            return start_sequence_id

        error_code = gmh['status']
        matches = gmh['matches']

        self.logger.info('%d recent matches have been found' % (len(matches)))

        is_new_match_found = False

        for match in matches:
            match_id = match['match_id']
            if self.current_match_id is None:
                self.current_match_id = match_id
            else:
                self.current_match_id = min(self.current_match_id, match_id)

            #if self.collection.find_one({'match_id':match_id}) != None:
            #    self.logger.info('Same match %s found' % (match_id))
            #    continue
            self.total_games += 1
            is_new_match_found = True
            print match_id
            try:
                match = api.get_match_details(match_id)['result']
                if(not self.is_valid_match(match)):
                    continue
                self.total_selected_games += 1
                sleep(1.0)
                self.process_match_details(match, match_id)
            except Exception as e:
                self.logger.info("Failed in obtain match: %s, since %s" % (str(match_id), str(e)))

        self.logger.info('Total: %d, Selected: %d, Yasp: %d' % (self.total_games, self.total_selected_games, self.yasp_games))
        self.current_match_id -= 1
        return is_new_match_found

    def start_crawler(self):
        is_new_match_found = True
        while(is_new_match_found):
            is_new_match_found = self.getRecentMatches(self.current_match_id)
            self.logger.info('Finish till match_id %d' % self.current_match_id)

if __name__ == '__main__':
    league_id = int(sys.argv[1])
    crawler = Dota2MatchCrawler(league_id)
    crawler.start_crawler()