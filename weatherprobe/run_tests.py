import unittest

tests = unittest.TestLoader().discover('./tests', pattern='test_*.py')
result = unittest.TextTestRunner(verbosity=2).run(tests)