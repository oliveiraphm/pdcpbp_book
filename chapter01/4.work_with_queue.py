from queue import Queue

def read_message_queue():
    q = Queue()
    
    for i in range(10):
        q.put(f"message {i}")
    
    while not q.empty():
        message = q.get()
        process_message(message)
        q.task_done()

def process_message(message):
    print(f"Processing message: {message}")

read_message_queue()