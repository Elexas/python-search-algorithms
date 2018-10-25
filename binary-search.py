import unittest
import unittest

def binary_search(item, x):
    index = None
    for i in range(len(x)):
        if item == x[i]:
            index = i
    return index


def binary_s(item, l, r, x):
    m = (int) ((r - l) / 2)

    if x[m] == item:
        return m
    elif item < x[m]:
        r = m
        return binary_s(item, l, r, x)
    else:
        l = m
        return binary_s(item, l, r, x)



class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        pass
    
    def testNone1(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(None, binary_search(0, x))
        
    def testNone2(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(None, binary_search(20, x))
 
    def test1(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(5, binary_search(6, x))
        
    def test2(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(14, binary_search(15, x))
    
    def test3(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(14, binary_search(15, x))

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    unittest.main()

