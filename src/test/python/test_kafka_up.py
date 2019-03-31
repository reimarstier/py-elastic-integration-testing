import unittest

import hamcrest
from confluent_kafka.admin import AdminClient, ConfigResource, ConfigSource
from confluent_kafka.cimpl import NewTopic, RESOURCE_TOPIC, KafkaException
from hamcrest import assert_that, equal_to, contains_string


class Topic:
    def __init__(self, topic):
        self.topic = topic


class TestImport(unittest.TestCase):
    def setUp(self):
        self.broker = "kafka:9092"
        # self.broker = "localhost:9093"
        self.admin_client = AdminClient({'bootstrap.servers': self.broker})

    def test_000_it(self):
        import py_elastic_int_testing
        assert_that(py_elastic_int_testing, hamcrest.not_none())

    def test_001_list_topics(self):
        # wait 90 seconds until broker is up

        result = self.admin_client.list_topics(timeout=90)

        assert_that(result.orig_broker_name, equal_to("%s/1" % self.broker))

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
        new_topics = [NewTopic("test_config", 1, 1, config=config)]

        result_futures = self.admin_client.create_topics(new_topics=new_topics)

        for topic, f in result_futures.items():
            try:
                f.result()  # The result itself is None
                self.assertTrue(True)
            except Exception as e:
                assert_that(str(e), contains_string("already exists."))

    def test_get_config(self):
        config_resource = [ConfigResource(RESOURCE_TOPIC, "test_config")]
        futures = self.admin_client.describe_configs(config_resource)
        for res, f in futures.items():
            try:
                configs = f.result()

                assert_that(configs["retention.ms"].value, equal_to("3600"))
                assert_that(configs["retention.bytes"].value, equal_to("10000"))
                assert_that(configs["delete.retention.ms"].value,
                            equal_to("3600"))

            except KafkaException as e:
                raise
            except Exception:
                raise

    def test_delete_topics(self):
        topics = ["testrun", "testrun2"]
        futures = self.admin_client.delete_topics(topics, operation_timeout=30)

        for topic, f in futures.items():
            result = f.result()
            self.assertIsNone(result)
