import time

def task1():
    time.sleep(2)
    print("Task 1 completed")

def task2():
    time.sleep(1)
    print("Task 2 completed")

task1()
task2()

                Synchronous
--------------------------------------------------
                Asynchronous

import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

