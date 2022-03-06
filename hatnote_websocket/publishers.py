"""Module for Publisher class."""

import asyncio
import websockets
from hatnote_websocket.schema import Message
from hatnote_websocket.subscribers import Subscriber


class Publisher:
    """Class which consumes a message from the websocket and broadcasts to subscribers."""

    def __init__(self, url: str, analysers: list[Subscriber], count: int):
        """Initialize the websocket publisher."""
        self._analysers = analysers
        self._url = url
        self.counter = count

    async def publish(self):
        async with websockets.connect(self._url) as ws:
            for _ in range(self.counter):
                event = await ws.recv()
                message = Message.parse_raw(event)
                await asyncio.gather(
                    *[analyser.consume(message) for analyser in self._analysers]
                )
