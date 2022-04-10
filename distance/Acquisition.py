import sys
import time


def flush_then_wait():
    sys.stdout.flush()
    sys.stderr.flush()
    time.sleep(0.5)


sys.stdout.write("Script stdout 1\n")
sys.stdout.write("Script stdout 2\n")
sys.stdout.write("Script stdout 3\n")
flush_then_wait()