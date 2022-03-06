"""Module for analyser subscriber classes."""

from threading import Lock
import typing
from hatnote_websocket.schema import Message


class Subscriber(typing.Protocol):
    """Subscriber protocol."""

    async def consume(self, message: Message) -> None:
        """Consume a message from the publisher."""

    def result(self) -> dict[str, int]:
        """The result outputs the processed result of the messages consumed."""


class TitleSubscriber:
    """Subscriber class which consumes messages from the publisher."""

    def __init__(self):
        """Initialize the message subscriber."""
        self._titles: dict[str, int] = {}
        self.mutex = Lock()

    async def consume(self, message: Message) -> None:
        """Consume a message from the publisher."""
        if message.action == "edit":
            if self._titles.get(message.page_title) is None:
                with self.mutex:
                    self._titles[message.page_title] = 1
                return
            with self.mutex:
                self._titles[message.page_title] += 1

    def result(self) -> dict[str, int]:
        """Return the result of the analysis."""
        return self._titles


class HitSubscriber:
    """Subscriber class which consumes messages from the publisher."""

    def __init__(self):
        """Initialize the hit subscriber."""
        self._titles: dict[str, int] = {}
        self.mutex = Lock()

    async def consume(self, message: Message) -> None:
        """Consume a message from the publisher."""
        if message.action == "hit":
            with self.mutex:
                self._titles[f"{message.page_title}-{message.user}"] = 0

    def result(self) -> dict[str, int]:
        """Return the number of hits."""
        return self._titles


class ChangeSizeSubscriber:
    """Subscriber class which consumes messages from the publisher."""

    def __init__(self):
        """Initialize the change size subscriber."""
        self._titles: dict[str, int] = {}
        self.mutex = Lock()

    async def consume(self, message: Message) -> None:
        """Consume a message from the publisher."""
        if message.action == "edit":
            if self._titles.get(message.page_title) is None:
                with self.mutex:
                    self._titles[message.page_title] = abs(message.change_size)
                return
            with self.mutex:
                self._titles[message.page_title] += abs(message.change_size)

    def result(self) -> dict[str, int]:
        """Return the result of the analysis."""
        return self._titles
