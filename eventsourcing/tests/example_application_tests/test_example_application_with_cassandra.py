from eventsourcing.tests.example_application_tests.base import ExampleApplicationTestCase
from eventsourcing.tests.sequenced_item_tests.test_cassandra_active_record_strategy import \
    WithCassandraRecordStrategies


class TestExampleApplicationWithCassandra(WithCassandraRecordStrategies, ExampleApplicationTestCase):
    pass
