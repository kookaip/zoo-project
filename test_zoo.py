import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    
    def test_invalid_age(self): 

        self.assertEqual(self.zoo.get_ticket_price(-5), "Error: invalid age") 

    def test_class_1(self): 

        self.assertEqual(self.zoo.get_ticket_price(6), 50) 

    def test_class_2(self): 

        self.assertEqual(self.zoo.get_ticket_price(17), 100) 

    def test_class_3(self): 

        self.assertEqual(self.zoo.get_ticket_price(35), 150) 

    def test_class_4(self): 

        self.assertEqual(self.zoo.get_ticket_price(99), 100) 

    def test_bva_invalid(self): 

        self.assertEqual(self.zoo.get_ticket_price(0), "Error: invalid age") 

    def test_bva_1(self): 

        self.assertEqual(self.zoo.get_ticket_price(12), 50) 

    def test_bva_2(self): 

        self.assertEqual(self.zoo.get_ticket_price(13), 100) 

        self.assertEqual(self.zoo.get_ticket_price(20), 100) 

    def test_bva_3(self): 

        self.assertEqual(self.zoo.get_ticket_price(21), 150) 

        self.assertEqual(self.zoo.get_ticket_price(60), 150) 

    def test_bva_4(self): 

        self.assertEqual(self.zoo.get_ticket_price(61), 100) 

if __name__ == '__main__':
    unittest.main()