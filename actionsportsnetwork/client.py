import requests
from requests.auth import HTTPBasicAuth
from .exceptions import *


class ActionNetwork(object):

    def __init__(self, username, password):
        """

        :param username:
        :param password:
        """
        self.host = 'https://api-prod.sprtactn.co'
        self.username = username
        self.password = password
        self.headers = {'User-Agent': 'Action-AppStore/13877 CFNetwork/894 Darwin/17.4.0'}
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self._auth()
        self.userid = None
        self.pro = False

    def _auth(self):
        """

        :return: Sets auth token in session header
        """
        res = self.session.post(self.host + '/mobile/v1/user/login', auth=HTTPBasicAuth(self.username,
                                                                                        self.password), json={})
        if 'token' in res.json().keys():
            self.session.headers.update({'authorization': res.json()['token']})
            res = self.myprofile().json()
            self.userid = res['id']
            if res['is_pro']:
                self.pro = True
        else:
            raise InvalidCredentials

    def _get(self, url, params=None):
        """

        :param url:
        :param params:
        :return:
        """
        try:
            return self.session.get(self.host + url, params=params)
        except Exception:
            raise NotFoundError

    def _post(self, url, params=None, data=None):
        """

        :param url:
        :param params:
        :param data:
        :return:
        """
        try:
            return self.session.post(self.host + url, params=params, json=data)
        except Exception:
            raise NotFoundError

    def myprofile(self):
        """

        :return:
        Overview of profile

        """
        return self._get('/mobile/v1/me')

    def inbox(self):
        """
        Inbox mostly for picks from other people

        :return:
        """
        return self._get('/mobile/v1/me/inbox')

    def picks(self, date=None, future=False, league=None):
        """

        :param date:
        :param future:
        :return:
        """

        params = {}
        if date is not None:
            params['date'] = date
        if future:
            params['future'] = True
        if league is not None:
            params['league'] = league

        return self._get('/mobile/v1/me/picks', params=params)

    def stats(self):
        """
        Pick stats
        :return:
        """
        return self._get('/mobile/v1/me/picks/stats')

    def analysis(self, analysis_id=None):
        """

        :return:
        """
        if analysis_id is None:
            return self._get('/mobile/v1/me/picks/analysis')
        else:
            return self._get('/mobile/v1/me/picks/analysis/' + analysis_id)

    def scoreboard(self, league, bookids=None, seasontype=None, week=None, date=None, division=None):
        """

        :param league:
        valid choices: today, all, nfl, mlb, nhl, mine, pga, soccer, ncaaf, ncaab, epl, bundesliga, champions,
        laliga, ligue1, seriea, mls
        :param bookids:
        :param seasonType:
        :param week:
        :param date:
        :param division: choices from TOP25, D1, AAC, WCC, WAC, SWAC, SUNBELT, SUMMIT, SOUTHLAND, AMERICANEAST, SEC, etc
        :return:
        """
        params = {}
        if bookids is not None:
            params['bookIds'] = bookids

        if seasontype is not None:
            params['seasonType'] = seasontype

        if week is not None:
            params['week'] = week

        if date is not None:
            params['date'] = date

        if division is not None:
            params['division'] = division

        return self._get('/mobile/v1/scoreboard/' + league, params={'bookIds': bookids, 'seasonType': seasontype,
                                                                    'week': week})

    def oddshistory(self, gameid, bookids=None):
        """

        :param gameid:
        :param bookids:
        :return:
        """
        params = {}
        if bookids is not None:
            params['bookIds'] = bookids
        return self._get('/mobile/v1/game/' + gameid + '/oddshistory', params=params)

    def game(self, gameid, bookids=None):
        """

        :param gameid:
        :param bookids:
        :return:
        gets info on games
        """
        params = {}
        if bookids is not None:
            params['bookIds'] = bookids

        return self._get('/mobile/v1/game/' + gameid, params=params)

    def add_pick(self, league_id, game_id, side_id, type, value, odds, units, units_type="money", period=game):
        """

        :param league_id:
        :param game_id:
        :param side_id:
        :param type:
        :param value:
        :param odds:
        :param units:
        :param units_type:
        :param period:
        :return:
        """

        pickdict = {"league_id": league_id, "game_id": game_id, "side_id": side_id, "meta": {"is_synced": False,
                                                                                             "tease": 0},
                    "type": type, "value": value, "odds": odds, "units": units, "units_type": units_type, "period": period}
        return self._post('/mobile/v1/me/picks', data=pickdict)












