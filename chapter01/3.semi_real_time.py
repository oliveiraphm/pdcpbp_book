import time
import random
from collections import deque

def generate_mock_data():
    while True:
        record = {
            'id': random.randint(1, 1000),
            'value': random.random() * 100
        }
        yield record
        time.sleep(0.1)

def process_semi_real_time(batch_size, interval):
    buffer = deque()
    start_time = time.time()

    for record in generate_mock_data():
        buffer.append(record)

        if (time.time() - start_time) >= interval or len(buffer) >= batch_size:
            transformed_batch = transform_data(list(buffer))
            print(f"Batch of {len(transformed_batch)} records before loading:")
            for rec in transformed_batch:
                print(rec)
            load_data(transformed_batch)
            buffer.clear()
            start_time = time.time()

def transform_data(batch):
    transformed_batch = []
    for record in batch:
        transformed_record = {
            'id': record['id'],
            'value': record['value'],
            'transformed_value': record['value'] * 1.1
        }
        transformed_batch.append(transformed_record)
    return transformed_batch

def load_data(batch):
    for record in batch:
        print(f"Loading record into database: {record}")

def main():
    batch_size = 5
    interval = 3.0

    process_semi_real_time(batch_size, interval)

if __name__ == "__main__":
    main()