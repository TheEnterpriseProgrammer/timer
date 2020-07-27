
# Imports
import time
from timer_error import TimerError


# Timer class definition
class Timer:
    # Constructor
    def __init__(self):
        # Private variables
        self._start_time = None
        self._end_time = None

    # Start the timer 
    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is running use .stop() to stop it and .reset() to reset it.")

        self._start_time = time.perf_counter()
    
    # Stop the timer
    def stop(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running use .start() to start it.")

        self._end_time = time.perf_counter()

        return self._end_time - self._start_time
    
    # Get elapsed time
    def get_elapsed_time(self):
        if self._start_time is not None and self._end_time is None:
            raise TimerError(f"Timer is running and has no end time use .stop() to stop it.")
        if self._start_time is None and self._end_time is None:
            raise TimerError(f"Timer has not been started use .start() to start it.")

        elapsed_time = self._end_time - self._start_time
        return f"Elapsed time: {elapsed_time:0.4f} seconds"


    # Reset
    def reset(self):
        self._start_time = None
        self._end_time = None
    

