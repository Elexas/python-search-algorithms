import unittest

def linear_search(item, l):
    index = None
    for i in range(len(l)):
        if item == l[i]:
            index = i
    return index


class TestLinearSearch(unittest.TestCase):

    def setUp(self):
        pass
    
    def testNone1(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(None, linear_search(0, l))
        
    def testNone2(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(None, linear_search(20, l))
 
    def test1(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(5, linear_search(6, l))
        
    def test2(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(14, linear_search(15, l))
    
    def test3(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(14, linear_search(15, l))
    
    def test4(self):
        l = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(6, linear_search(9, l))

if __name__ == "__main__":
    unittest.main()

