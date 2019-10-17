import unittest
import app

file_value = [[-7.2277942e+02,7.0652344e+01,3.3089404e+00,1.2586458e+01,
   5.6169076e+00,1.4102925e+01, -3.0458407e+00,3.1913407e+00,
  -3.3704033e+00, -1.5528569e+00, -8.1244192e+00, -2.1913698e+00,
   2.9435401e+00, -2.7643819e+00,9.8888969e-01,1.7122957e+00,
  -2.8129392e+00,2.5758761e-01,2.7482674e+00,-1.8028446e+00]]

class Test_all(unittest.TestCase):
    def test_calc(self):
        result = app.calc("03-01-01-01-01-01-01.wav")
        self.assertEqual(result.shape,(1,20))
        self.assertIsNotNone(result)
        self.assertListEqual(result,file_value)

    def test_convert_emo(self):
        result = app.convert_emo(2)
        self.assertIsNotNone(result)
        self.assertEqual(result,'fearful')



if  __name__ == '__main__':
    unittest.main()