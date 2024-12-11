import unittest

SERVER="server_b"
class AllAssertsTest(unittest.TestCase):


    @unittest.skip("Trabajo en progreso, será habilitada nuevamente")
    def test_skip_(self):
        self.assertEqual("hola","chao")

    @unittest.skipIf(SERVER == "server_b", "Saltado porque no estamos en el server")
    def test_skip_if(self):
        self.assertEqual(100,100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100,150)
