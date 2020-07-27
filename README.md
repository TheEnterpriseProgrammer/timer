# Timer
This project is to be used for determining the elapsed time of execution of a python application.    
This package can be used in conjunction with a logger to log elapsed time.

> #### Table of Contents  
> [1.Installation](#installation)  
> [2.Initialization](#initialization)  
> [3.Starting The Timer](#starting-the-timer)  
> [4.Stopping The Timer](#stopping-the-timer)  
> [5.Getting The Elapsed Time](#getting-the-elapsed-time)  
> [6.Resetting the Timer](#resetting-the-timer)  

## Installation
Installation instructions here

## Initialization
To initialize the timer create a new instance of the timer.

```python
timer = Timer()
```

## Starting The Timer
To start the timer invoke the start method on the timer.

```python
timer.start()
```

## Stopping The Timer
To stop the timer invoke the stop method on the timer.

```python
timer.stop()
```

## Getting The Elapsed Time
There are two ways of getting the elapsed time from the timer.    
Also the elapsed time will be available from the timer until it is reset.    

1. The elapsed time is returned when invoking the .stop() method.
```python
timer.stop()
```

2. The elapsed time can be retrieved by invoking the .get_elapsed_time() method.
```python
timer.get_elapsed_time()
```

## Resetting The Timer
To restart the timer invoke the reset method on the timer.
```python
timer.reset()
```
