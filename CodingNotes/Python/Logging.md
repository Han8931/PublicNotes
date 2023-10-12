
# Introduction

```python
import logging

def main()->None:
    logging.basicConfig(level=logging.WARNING)

    logging.debug("This is a debug")
    logging.info("This is a info")
    logging.warning("This is a warning")
    logging.error("This is a error")
    logging.critical("This is a critical")

if __name__ == "__main__":
    main()
```

- If we set the basicConfig at `WARNING`, then it will only print `warning, error, and critical. `
- To change this, we can set it as `info` or `debug`

## Configuring Logging

```python
import logging

def main()->None:
    logging.basicConfig(
	    level=logging.DEBUG,
	    format="%(asctime)s %(levelname)s %(message)s",
	    datefmt="%Y-%m-%d %H:%M:%S",
		filename="basic.log",
	    )
	    

    logging.debug("This is a debug")
    logging.info("This is a info")
    logging.warning("This is a warning")
    logging.error("This is a error")
    logging.critical("This is a critical")

if __name__ == "__main__":
    main()
```

### getLogger

```python
mylogger = logging.getLogger("my")  
mylogger.setLevel(logging.INFO)
```

### Handler
Each logger has one or more handlers and the _handlers are responsible for sending the log information to a destination_. Also, each handler has one formatter that defines how the log will be displayed. 

```python
mylogger = logging.getLogger("my")  
mylogger.setLevel(logging.INFO)  

stream_handler = logging.StreamHandler()  
formatter = logging.Formatter("%(asctime)s %(levelname)s")
stream_handler.setFormatter(formatter)
mylogger.addHandler(stream_handler)  

file_handler = logging.FileHandler('my.log')  
mylogger.addHandler(file_handler)  

mylogger.info("server start!!!")
```

In the above example, I sent the log information to both the console and the file (my.log). 

## Exception

To log an exception in Python we can use **logging** module and through that we can log the error. Logging an exception in python with an error can be done in the **logging.exception()** method. This function logs a message with level ERROR on this logger. 

```python
import logging

try:
	printf("GeeksforGeeks")
except Exception as Argument:
	logging.exception("Error occurred while printing GeeksforGeeks")
```

Be aware that in Python 3 you must call the `logging.exception` method just inside the `except` part. If you call this method in an arbitrary place you may get a bizarre exception. 

