What follows is a take-home test that you should spend no more than 4 hours on. The purpose of this test is to evaluate your ability to:

deal with a vague brief
write python to consume, process, and analyse data
produce a report including visualisations
You will be evaluated on:

legibility of code
clarity of approach to analysis
quality of communication
You must produce a document around 500 words + visualisations that describes what you have discovered about the world and why it is interesting. You must also produce python code to describe how you made your discoveries.

How you approach the brief, within the context above, is up to you.

The data source for this test is a websocket containing wikipedia edits:

ws://wikimon.hatnote.com:9000

In python 3.7, this can be consumed using the websockets library, for example:

import asyncio
import websockets

async def hatnote():
    async with websockets.connect("ws://wikimon.hatnote.com:9000") as ws:
        while True:
            event = await ws.recv()
            print(event)

asyncio.get_event_loop().run_until_complete(hatnote())
We would like to know something interesting about the world, using this data stream as a proxy. Your task is to explore this data stream and its implications in the real world, and report back.
