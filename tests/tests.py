import json
import unittest

from service.ApiController import app


class StepApiControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_fuzz_run_command(self):
        # /fuzz/do/<string:command>
        resp = self.app.get('/fuzz/do/run')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

        content = json.loads(resp.get_data(as_text=True))
        self.assertEqual(len(content), 1)
        self.assertEqual(content, {'command': 'run'})

    def test_fuzz_pause_command(self):
        # /fuzz/do/<string:command>
        resp = self.app.get('/fuzz/do/pause')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

        content = json.loads(resp.get_data(as_text=True))
        self.assertEqual(len(content), 1)
        self.assertEqual(content, {'command': 'pause'})

    def test_fuzz_stop_command(self):
        # /fuzz/do/<string:command>
        resp = self.app.get('/fuzz/do/stop')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')

        content = json.loads(resp.get_data(as_text=True))
        self.assertEqual(len(content), 1)
        self.assertEqual(content, {'command': 'stop'})

    def test_book_detail_404(self):
        resp = self.app.get('/stam/1111')
        self.assertEqual(resp.status_code, 404)

    def test_swagger_api(self):
        resp = self.app.get('/fuzz/api/docs/')
        # todo check response content contians '<title>Fuzzer</title>'
        self.assertEqual(resp.status_code, 200)

