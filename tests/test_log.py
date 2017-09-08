import unittest, os
from log import *
from body import Body
from physics.vector2 import Vector2


class TestLog(unittest.TestCase):
    def test_get_minimal_str_of_vector2(self):
        vector = Vector2(3, 4)
        expected_result = '3,4'
        result = get_minimal_str_of_vector2(vector)
        self.assertEqual(result, expected_result)

    def test_init_file(self):
        file_path = 'temp.txt'
        bodies = [
                Body(Vector2(0, 0), Vector2(0, 0), 10),
                Body(Vector2(1, 0), Vector2(0, 0), 20),
                Body(Vector2(0, 1), Vector2(0, 0), 30)
        ]
        init_file(file_path, bodies)
        expected_result = [
            '3\n',
            '10\n',
            '20\n',
            '30\n'
        ]
        with open(file_path) as file:
            result = file.readlines()
        os.remove(file_path)
        self.assertEqual(result, expected_result)

    def test_log_body_positions(self):
        file_path = 'temp.txt'
        bodies = [
            Body(Vector2(0, 0), Vector2(0, 0), 10),
            Body(Vector2(1, 0), Vector2(0, 0), 20),
            Body(Vector2(0, 1), Vector2(0, 0), 30)
        ]
        log_body_positions(file_path, bodies)
        expected_result = [
            '0,0\n',
            '1,0\n',
            '0,1\n'
        ]
        with open(file_path) as file:
            result = file.readlines()
        os.remove(file_path)
        self.assertEqual(result, expected_result)

    def test_all(self):
        dt = 1
        file_path = 'temp.txt'
        bodies = [
            Body(Vector2(0, 0), Vector2(1, 0), 10),
            Body(Vector2(1, 0), Vector2(1, 0), 20),
            Body(Vector2(0, 1), Vector2(1, 0), 30)
        ]
        init_file(file_path, bodies)
        log_body_positions(file_path, bodies)
        for body in bodies:
            body.update_position(dt)
        log_body_positions(file_path, bodies)
        expected_result = [
            '3\n',
            '10\n',
            '20\n',
            '30\n',
            '0,0\n',
            '1,0\n',
            '0,1\n',
            '1,0\n',
            '2,0\n',
            '1,1\n'
        ]
        with open(file_path) as file:
            result = file.readlines()
        os.remove(file_path)
        self.assertEqual(result, expected_result)