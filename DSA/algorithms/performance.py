import time
from contextlib import contextmanager

@contextmanager
def timer(label: str):
    start: float = time.perf_counter()
    try:    
        yield
    finally:
        end: float = time.perf_counter()
        print(f"{label}: {end - start:.6f} secs")