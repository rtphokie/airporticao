import unittest
from airporticao import AirNavAirports
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def test_RDU(self):
        uut = AirNavAirports()
        data = uut.lookup_airport("KRDU")
        self.assertEqual(data['desc'], 'Raleigh/Durham, North Carolina, USA')
        self.assertAlmostEqual(data['lat'], 35.877, 2)
        self.assertTrue(data['from_cache'])

    def test_KGEV(self):
        uut = AirNavAirports()
        data = uut.lookup_airport("KGEV")
        self.assertEqual(data['desc'], 'Jefferson, North Carolina, USA')
        self.assertEqual(data['country'], 'USA')
        self.assertEqual(data['city'], 'Jefferson')
        self.assertEqual(data['state'], 'North Carolina')
        self.assertAlmostEqual(data['lat'], 36.4324796, 2)
        self.assertTrue(data['from_cache'])

    def test_LAX(self):
        uut = AirNavAirports()
        data = uut.lookup_airport("KLAX")
        self.assertEqual(data['desc'], 'Los Angeles, California, USA')
        self.assertEqual(data['country'], 'USA')
        self.assertEqual(data['city'], 'Los Angeles')
        self.assertEqual(data['state'], 'California')
        self.assertAlmostEqual(data['lat'], 33.942496, 2)
        self.assertTrue(data['from_cache'])


if __name__ == '__main__':
    unittest.main()
