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
        self.broker = "kafka:9092"
        self.admin_client = AdminClient({'bootstrap.servers': self.broker})

    def test_000_it(self):
        import py_elastic_int_testing
        assert_that(py_elastic_int_testing, hamcrest.not_none())

    def test_001_list_topics(self):
        # wait 90 seconds until broker is up

        result = self.admin_client.list_topics(timeout=90)

        assert_that(result.orig_broker_name, equal_to("kafka:9092/1"))

    def test_002_test_create_topic(self):

        new_topics = [NewTopic("testrun", 1, 1)]

        result_futures = self.admin_client.create_topics(new_topics,
                                                         request_timeout=15.0)

        for topic, f in result_futures.items():
            try:
                f.result()  # The result itself is None
                self.assertTrue(True)
            except Exception as e:
                assert_that(str(e), contains_string("already exists."))

    def test_003_create_topic_with_config(self):
        config = {
            "delete.retention.ms": 3600,
            "retention.bytes": 10000,
            "retention.ms": 3600,
        }
        new_topics = [NewTopic("testrun2", 1, 1, config=config)]

        result_futures = self.admin_client.create_topics(new_topics=new_topics)

        for topic, f in result_futures.items():
            try:
                f.result()  # The result itself is None
                self.assertTrue(True)
            except Exception as e:
                assert_that(str(e), contains_string("already exists."))
