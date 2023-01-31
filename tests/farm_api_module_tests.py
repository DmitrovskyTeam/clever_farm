import unittest

from farm_api_module import FarmApiModule


class BasicModuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.api_module = FarmApiModule()

    def tearDown(self) -> None:
        self.api_module.close()

    def test_temperature1(self):
        self.assertEqual(None, self.api_module.get_air_temp_hum(5))

    def test_temperature2(self):
        self.assertEqual(None, self.api_module.get_air_temp_hum(-1))

    def test_temperature3(self):
        self.assertEqual(None, self.api_module.get_air_temp_hum(0))

    def test_temperature4(self):
        self.assertIn('id', str(self.api_module.get_air_temp_hum(1)))
        self.assertIn('temperature', str(self.api_module.get_air_temp_hum(1)))
        self.assertIn('humidity', str(self.api_module.get_air_temp_hum(1)))

    def test_temperature5(self):
        self.assertNotEqual(None, self.api_module.get_air_temp_hum(1))

    def test_temperature6(self):
        self.assertNotEqual(None, self.api_module.get_air_temp_hum(4))
    def test_ground_sensor1(self):
        self.assertEqual(None, self.api_module.get_ground_hum(-1))

    def test_ground_sensor2(self):
        self.assertEqual(None, self.api_module.get_ground_hum(0))

    def test_ground_sensor3(self):
        self.assertEqual(None, self.api_module.get_ground_hum(7))

    def test_ground_sensor4(self):
        self.assertNotEqual(None, self.api_module.get_ground_hum(1))

    def test_ground_sensor5(self):
        self.assertNotEqual(None, self.api_module.get_ground_hum(6))


if __name__ == "__main__":
    unittest.main()
