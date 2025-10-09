import time
import random

def generate_mock_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'id': random.randint(1, 1000),
            'value': random.random() * 100
        }
        data.append(record)
    return data

def process_in_batches(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

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
    num_records = 100
    batch_size = 10

    data = generate_mock_data(num_records)
    print("Original data:", data)

    for batch in process_in_batches(data, batch_size):
        transformed_batch = transform_data(batch)
        print("Batch before loading:")
        for record in transformed_batch:
            print(record)
        load_data(transformed_batch)
        time.sleep(1)

if __name__ == "__main__":
        main()