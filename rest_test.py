import unittest
import requests

class UserTest(unittest.TestCase):
    '''user search test'''

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/users'

    def test_user1(self):
        '''test user 1'''
        r = requests.get(self.base_url+'/1/',auth=('admin@mail.coom','1qa2ws,./'))
        result = r.json()
        self.assertEqual(result['username'],'admin@mail.com')
        self.assertEqual(result['email'],'admin@mail.com')

    def test_user2(self):
        '''test user 2'''
        r = requests.get(self.base_url+'/2/',auth=('admin@mail.coom','1qa2ws,./'))
        result = r.json()
        self.assertEqual(result['username'],'daisy')
        self.assertEqual(result['email'],'daisy@mail.com')

    def test_user3(self):
        '''test user 3'''
        r = requests.get(self.base_url+'/3/',auth=('admin@mail.coom','1qa2ws,./'))
        result = r.json()
        self.assertEqual(result['username'],'yuekui')
        self.assertEqual(result['email'],'yuekui@mail.com')

class GroupTest(unittest.TestCase):
    '''group search test'''

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/groups'

    def test_groups1(self):
        '''test groups 1'''
        r = requests.get(self.base_url+'/1/',auth=('admin@mail.coom','1qa2ws,./'))
        result = r.json()
        self.assertEqual(result['name'],'QA')

    def test_groups2(self):
        '''test groups 1'''
        r = requests.get(self.base_url + '/1/', auth=('admin@mail.coom', '1qa2ws,./'))
        result = r.json()
        self.assertEqual(result['name'], 'QA')

if __name__ == '__main__':
    unittest.main()