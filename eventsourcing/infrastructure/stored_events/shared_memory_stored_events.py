from eventsourcing.infrastructure.stored_events.base import StoredEventRepository
from eventsourcing.infrastructure.stored_events.transcoders import StoredEvent
from multiprocessing import Array

class SharedMemoryStoredEventRepository(StoredEventRepository):

    serialize_without_json = True

    def __init__(self):
        super(SharedMemoryStoredEventRepository, self).__init__()
        self._by_id = {}
        self._by_stored_entity_id = {}
        self._by_topic = {}

    def append(self, stored_event):
        assert isinstance(stored_event, StoredEvent)
        event_id = stored_event.event_id
        stored_entity_id = stored_event.stored_entity_id
        topic = stored_event.event_topic

        # Index by event ID.
        self._by_id[event_id] = stored_event

        # Index by entity ID.
        if stored_entity_id not in self._by_stored_entity_id:
            self._by_stored_entity_id[stored_entity_id] = []
        self._by_stored_entity_id[stored_entity_id].append(stored_event)

        # Index by event topic.
        if topic not in self._by_topic:
            self._by_topic[topic] = []
        self._by_topic[topic].append(stored_event)

    def __getitem__(self, event_id):
        return self._by_id[event_id]

    def __contains__(self, event_id):
        return event_id in self._by_id

    def get_entity_events(self, stored_entity_id):
        if stored_entity_id not in self._by_stored_entity_id:
            return []
        else:
            return self._by_stored_entity_id[stored_entity_id]

    def get_topic_events(self, event_topic):
        return self._by_topic[event_topic]