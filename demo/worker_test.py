#!/usr/bin/env python3.8

import asyncio
import json
import logging

import ezpy


async def test_handler(frames):
    logging.info("handling...")
    await asyncio.sleep(2)
    return [b"OK", json.dumps("HEY!").encode("utf-8")]


async def main():
    logging.basicConfig(level=logging.INFO)
    async with ezpy.WorkerConnection(
        con_s="tcp://localhost:9998",
        service_name=b"TEST",
            livelieness=2000,
            q_length=5
    ) as conn:
        await conn.serve(test_handler)
    logging.info("OK")
    return


if __name__ == '__main__':
    asyncio.run(main())
