from uuid import UUID

from eventsourcing.domain.model.events import (
    EventWithOriginatorID,
    EventWithOriginatorVersion,
    EventWithTimestamp,
)
from eventsourcing.types import AbstractSnapshop


class Snapshot(
    EventWithTimestamp,
    EventWithOriginatorVersion,
    EventWithOriginatorID,
    AbstractSnapshop,
):
    def __init__(
        self, originator_id: UUID, originator_version: int, topic: str, state: str
    ):
        super(Snapshot, self).__init__(
            originator_id=originator_id,
            originator_version=originator_version,
            topic=topic,
            state=state,
        )

    @property
    def topic(self) -> str:
        """
        Path to the class of the snapshotted entity.
        """
        return self.__dict__["topic"]

    @property
    def state(self) -> str:
        """
        State of the snapshotted entity.
        """
        return self.__dict__["state"]
