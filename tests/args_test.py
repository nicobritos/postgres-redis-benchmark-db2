import unittest
from utils import args as args_utils


class ArgsTest(unittest.TestCase):
    def test_postgres_config(self):
        args = args_utils.parse_args([
            '-g',
            '-ph', 'host',
            '-pp', '5432',
            '-pd', 'database',
            '-pU', 'username',
            '-pP', 'password'
        ])

        self.assertIsNotNone(args.ph)
        self.assertIsNotNone(args.pp)
        self.assertIsNotNone(args.pd)
        self.assertIsNotNone(args.pU)
        self.assertIsNotNone(args.pP)

        config = args_utils.get_postgres_config(args)

        self.assertEquals(config['host'], 'host')
        self.assertEquals(config['port'], '5432')
        self.assertEquals(config['database'], 'database')
        self.assertEquals(config['username'], 'username')
        self.assertEquals(config['password'], 'password')

    def test_redis_config(self):
        args = args_utils.parse_args([
            '-g',
            '-rh', 'host',
            '-rp', '6399',
            '-rd', '0'
        ])

        self.assertIsNotNone(args.rh)
        self.assertIsNotNone(args.rp)
        self.assertIsNotNone(args.rd)

        config = args_utils.get_redis_config(args)

        self.assertEquals(config['host'], 'host')
        self.assertEquals(config['port'], 6399)
        self.assertEquals(config['database'], 0)

    def test_generate(self):
        args = args_utils.parse_args(['-g'])

        self.assertIsNotNone(args.generate)

    def test_query(self):
        args = args_utils.parse_args(['-q', '1'])

        self.assertIsNotNone(args.query)
        self.assertEquals(args.query, 1)
