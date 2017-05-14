import asyncio
import os
import signal
import tomodachi
from tomodachi.discovery.dummy_registry import DummyRegistry
from tomodachi.protocol.json_base import JsonBase


@tomodachi.service
class AutoClosingService(object):
    name = 'test_auto_closing'
    discovery = [DummyRegistry]
    message_protocol = JsonBase

    start = False
    started = False
    stop = False

    async def _start_service(self):
        self.start = True

    async def _started_service(self):
        self.started = True
        await asyncio.sleep(0.1)
        os.kill(os.getpid(), signal.SIGTERM)

    async def _stop_service(self):
        self.stop = True