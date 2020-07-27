# Imports
import unittest
from timer import Timer
from timer import TimerError

# Timer test class definition
class TimerTest(unittest.TestCase):
    # Timer will start
    def test_timer_will_start(self):
        timer = Timer()
        timer.start()
        elapsed = timer.stop()
        assert(elapsed != None)
    
    # Timer will not start if it is running
    def test_timer_will_not_start_again(self):
        timer = Timer()
        timer.start()
        try:
            timer.start()
        except TimerError as e:
            error = e.args[0]
            assert(error == "Timer is running use .stop() to stop it and .reset() to reset it.")

    # Timer will not stop if it has not been started
    def test_timer_will_not_stop_if_not_started(self):
        timer = Timer()
        try:
            timer.stop()
        except TimerError as e:
            error = e.args[0]
            assert(error == "Timer is not running use .start() to start it.")
    
    # Timer will not get elapsed time if not started
    def test_timer_will_not_get_elapsed_time_if_not_running(self):
        timer = Timer()
        try:
            timer.get_elapsed_time()
        except TimerError as e:
            error = e.args[0]
            assert(error == "Timer has not been started use .start() to start it.")

    # Timer will not get elapsed time if not stopped
    def test_timer_will_not_get_elapsed_time_if_running(self):
        timer = Timer()
        try:
            timer.start()
            timer.get_elapsed_time()
        except TimerError as e:
            error = e.args[0]
            assert(error == "Timer is running and has no end time use .stop() to stop it.")

# If runner name is main equal to main method start main method
if __name__ == '__main__':
    unittest.main()
