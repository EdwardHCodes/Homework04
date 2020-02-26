# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:25:32 2020

@author: Edward
Script to test GitHubApi script.
"""


from unittest import mock

from Homework04a import gitHub_API

class TestgitHub_API(mock.TestCase):
    def testGithub(self):
        self.assertEqual(gitHub_API('FastCashHash'), True)

if __name__ == "__main__":
    print('Running unit tests')
    mock.main() 
