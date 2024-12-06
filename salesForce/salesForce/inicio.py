import unittest

from PO.POLogin import SF
import os

# class TestSalesforce(unittest.TestCase):
#
#     def setUp(self):
#         self.sf = SF()
#
#     def test_login(self):
#         self.sf.login()
#
#     def test_pospago(self):
#         self.sf.login()
#         self.sf.pospago()
#
#     def tearDown(self):
#         self.sf.close_driver()
#
#
# if __name__ == '__main__':
#     unittest.main()

sf = SF("Pospago")
sf.login()
sf.pospago()

