import unittest
from unittest.mock import MagicMock

from slack_backup import client
from slack_backup import objects

PROFILES = [{'always_active': False,
             'api_app_id': '',
             'avatar_hash': '167c4585f3b5',
             'bot_id': 'B34RR91SQ',
             'image_1024': 'https://bla.com/2016-11-19/12345_72.png',
             'image_192': 'https://bla.com/2016-11-19/12345_72.png',
             'image_24': 'https://bla.com/2016-11-19/12345_24.png',
             'image_32': 'https://bla.com/2016-11-19/12345_32.png',
             'image_48': 'https://bla.com/2016-11-19/12345_48.png',
             'image_512': 'https://bla.com/2016-11-19/12345_72.png',
             'image_72': 'https://bla.com/2016-11-19/12345_72.png',
             'image_original': 'https://bla.com/2016-11-19/12345_original.png',
             'real_name': '',
             'real_name_normalized': '',
             'title': 'all your base are belongs to us'},
            {'avatar_hash': 'bab01f158419',
             'email': 'name1@some.mail.com',
             'first_name': 'name',
             'image_1024': 'https://bla.com/2016-11-19/23456_512.png',
             'image_192': 'https://bla.com/2016-11-19/23456_192.png',
             'image_24': 'https://bla.com/2016-11-19/23456_24.png',
             'image_32': 'https://bla.com/2016-11-19/23456_32.png',
             'image_48': 'https://bla.com/2016-11-19/23456_48.png',
             'image_512': 'https://bla.com/2016-11-19/23456_512.png',
             'image_72': 'https://bla.com/2016-11-19/23456_72.png',
             'image_original': 'https://bla.com/2016-11-19/23456_original.png',
             'last_name': 'lastname',
             'real_name': 'name lastname',
             'real_name_normalized': 'name lastname'},
            {'avatar_hash': '398907b00c64',
             'email': 'name2@@foobar.mail.net',
             'first_name': 'othername',
             'image_1024': 'https://bla.com/2016-11-19/34567_72.gif',
             'image_192': 'https://bla.com/2016-11-19/34567_72.gif',
             'image_24': 'https://bla.com/2016-11-19/34567_24.gif',
             'image_32': 'https://bla.com/2016-11-19/34567_32.gif',
             'image_48': 'https://bla.com/2016-11-19/34567_48.gif',
             'image_512': 'https://bla.com/2016-11-19/34567_72.gif',
             'image_72': 'https://bla.com/2016-11-19/34567_72.gif',
             'image_original': 'https://bla.com/2016-11-19/34567_original.gif',
             'last_name': 'totallylast',
             'phone': '',
             'real_name': 'othername totallylast',
             'real_name_normalized': 'othername totallylast',
             'skype': '',
             'title': 'blah & blah'},
            {'avatar_hash': 'sv1454671952',
             'fields': None,
             'first_name': 'slackbot',
             'image_192': 'https://bla.com/65f9/img/slackbot_192.png',
             'image_24': 'https://bla.com/181c/img/slackbot_24.png',
             'image_32': 'https://bla.com/0fac/slackbot/assets/service_32.png',
             'image_48': 'https://bla.com/4fac/slackbot/assets/service_48.png',
             'image_512': 'https://bla.com/1803/img/slackbot_512.png',
             'image_72': 'https://bla.com/1780/img/slackbot_72.png',
             'last_name': '',
             'real_name': 'slackbot',
             'real_name_normalized': 'slackbot'}]

USERS = {'cache_ts': 1479577519,
         'ok': True,
         'members': [{'color': 'd58247',
                      'deleted': False,
                      'id': 'UAAAAAAAA',
                      'is_admin': False,
                      'is_bot': True,
                      'is_owner': False,
                      'is_primary_owner': False,
                      'is_restricted': False,
                      'is_ultra_restricted': False,
                      'name': 'borg',
                      'profile': PROFILES[0],
                      'real_name': '',
                      'status': None,
                      'team_id': 'T0000TEST',
                      'tz': None,
                      'tz_label': 'Pacific Standard Time',
                      'tz_offset': -28800},
                     {'color': '4bbe2e',
                      'deleted': False,
                      'has_2fa': False,
                      'id': 'UBBBBBBBB',
                      'is_admin': True,
                      'is_bot': False,
                      'is_owner': True,
                      'is_primary_owner': False,
                      'is_restricted': False,
                      'is_ultra_restricted': False,
                      'name': 'name1',
                      'profile': PROFILES[1],
                      'real_name': 'name lastname',
                      'status': None,
                      'team_id': 'T0000TEST',
                      'tz': 'America/Los_Angeles',
                      'tz_label': 'Pacific Standard Time',
                      'tz_offset': -28800},
                     {'color': 'e96699',
                      'deleted': False,
                      'has_2fa': False,
                      'id': 'UCCCCCCCC',
                      'is_admin': False,
                      'is_bot': False,
                      'is_owner': False,
                      'is_primary_owner': False,
                      'is_restricted': False,
                      'is_ultra_restricted': False,
                      'name': 'name2',
                      'profile': PROFILES[2],
                      'real_name': 'othername totallylast',
                      'status': None,
                      'team_id': 'T0000TEST',
                      'tz': 'America/Los_Angeles',
                      'tz_label': 'Pacific Standard Time',
                      'tz_offset': -28800},
                     {'color': '757575',
                      'deleted': False,
                      'id': 'USLACKBOT',
                      'is_admin': False,
                      'is_bot': False,
                      'is_owner': False,
                      'is_primary_owner': False,
                      'is_restricted': False,
                      'is_ultra_restricted': False,
                      'name': 'slackbot',
                      'profile': PROFILES[3],
                      'real_name': 'slackbot',
                      'status': None,
                      'team_id': 'T0000TEST',
                      'tz': None,
                      'tz_label': 'Pacific Standard Time',
                      'tz_offset': -28800}]}


class TestClient(unittest.TestCase):

    def test_update_users(self):
        cl = client.Client("token string")
        cl.slack.api_call = MagicMock(return_value=USERS)
        cl._update_users()
        users = cl.session.query(objects.User).all()
        self.assertEqual(len(users), 4)
        self.assertEqual(users[0].id, 1)

        cl._update_users()
        users = cl.session.query(objects.User).all()
        self.assertEqual(len(users), 4)
        self.assertEqual(users[0].id, 1)
        self.assertEqual(users[0].slackid, 'UAAAAAAAA')
