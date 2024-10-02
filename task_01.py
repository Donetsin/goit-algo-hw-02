# Завдання 1
import queue
import time
import random

request_queue = queue.Queue()

def generate_request():
    """Generate a random request id, put it in the queue and print it."""
    request_id = random.randint(1000, 9999)
    request_queue.put(request_id)
    print("Generated request: ", request_id)

def process_request():
    """Process the given request id, or if none given, the top of the queue."""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Request {request_id} processed.")
    else:
        print("All requests processed.")

def main():
    """
    Generates and processes requests in an infinite loop, with a 2 second delay
    between each request.
    """
    while True:
        # Generate and process a request
        if random.randint(1, 100) % 2 == 0:
            generate_request()
            time.sleep(2)
        else:
            process_request()
            time.sleep(3)

if __name__ == "__main__":
    main()
