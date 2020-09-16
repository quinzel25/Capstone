import unittest

import camelCaseGitHub

from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        ##                answer   | .py file name . function_name | testing
        self.assertEqual('helloWorld', camelCaseGitHub.camelCase('Hello World'))
        ##This test will fail 
        #self.assertEqual('this will fail', camelCaseGitHub.camelCase('thisWillFail'))

        self.assertEqual('camelCaseRules', camelCaseGitHub.camelCase('Camel   cAsE RuLeS'))

        self.assertEqual('', camelCaseGitHub.camelCase(' '))


if __name__ == '__main__':
    unittest.main()
