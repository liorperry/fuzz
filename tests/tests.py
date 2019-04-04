import json
import unittest

from service.ApiController import app


class StepApiControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # run sqlite fuzzing
    def test_fuzz_sqlite_run_command(self):
        pass

    # run sqlite fuzzing and stop
    def test_fuzz_sqlite_run_and_stop_command(self):
        pass

    # run sqlite fuzzing & check status
    def test_fuzz_sqlite_status_command(self):
        pass


    def test_book_detail_404(self):
        resp = self.app.get('/stam/1111')
        self.assertEqual(resp.status_code, 404)

    def test_swagger_api(self):
        resp = self.app.get('/fuzz/api/docs/')
        # todo check response content contians '<title>Fuzzer</title>'
        self.assertEqual(resp.status_code, 200)

