import unittest

import hamcrest
from confluent_kafka.admin import AdminClient
from confluent_kafka.cimpl import NewTopic
from hamcrest import assert_that, equal_to, contains_string


class Topic:
    def __init__(self, topic):
        self.topic = topic


class TestImport(unittest.TestCase):
    def setUp(self):
        pass

    def test_000_it(self):
        import py_elastic_int_testing
        assert_that(py_elastic_int_testing, hamcrest.not_none())

    def test_001_list_topics(self):
        # wait 90 seconds until broker is up

        broker = "kafka:9092"
        admin_client = AdminClient({'bootstrap.servers': broker})
        result = admin_client.list_topics(timeout=90)

        assert_that(result.orig_broker_name, equal_to("kafka:9092/1"))

    def test_002_test_create_topic(self):
        broker = "kafka:9092"
        admin_client = AdminClient({'bootstrap.servers': broker})

        new_topics = [NewTopic("testrun", 1, 1)]

        result_futures = admin_client.create_topics(new_topics,
                                                    request_timeout=15.0)

        for topic, f in result_futures.items():
            try:
                f.result()  # The result itself is None
                self.assertTrue(True)
            except Exception as e:
                assert_that(str(e), contains_string("already exists."))
