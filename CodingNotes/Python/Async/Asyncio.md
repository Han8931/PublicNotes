[Reference 1](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-1.html)
[Reference 2](https://medium.com/dev-bits/a-minimalistic-guide-for-understanding-asyncio-in-python-52c436c244ea)

# What is asyncio?

Python's asyncio is a co-routine-based concurrency model that provides elegant constructs to write concurrent python code without using threads. The mindset of designing concurrent solutions is different from traditional thread-based approaches. We know that threading is mainly used for I/O bound processing, whereas multiprocessing is advantageous for CPU-bound tasks in Python.

Python asyncio standard library package allows developers to use async/await syntax while developing concurrent programs.


# Introduction

Traditionally computers have been machines that do one thing at a time. Modern computers (as of 2020) can often do multiple things at once, because they are equipped with a multitude of CPU cores, and whilst I cannot predict the future I expect that to continue to be true for at least the immediate future. And there are many books and many articles out there about how to make use of any number of libraries and frameworks designed to do multiple things at once by utilizing multiple execution threads.

**Asyncio is not one of these**

Using asyncio in your Python code will not make your code multi-threaded. It will not cause multiple Python instructions to be executed at once, and it will not in any way allow you to sidestep the so-called ["global interpreter lock"](https://wiki.Python.org/moin/GlobalInterpreterLock).

When a program is running IO-bound code it’s pretty common for the CPU to spend a lot of time doing nothing at all because the one thing that’s currently being done is waiting for something elsewhere.

It’s also pretty common to find that your program has a variety of other work it could be getting on with whilst this waiting is occurring, work which doesn’t depend upon the thing being waited for. So asyncio is designed to allow you to structure your code so that when one piece of linear single-threaded code (called a _"coroutine"_) is waiting for something to happen another can take over and use the CPU.

**It’s not about using multiple cores, it’s about using a single core more efficiently**