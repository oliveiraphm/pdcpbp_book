from great_expectations.data_context import BaseDataContext
from great_expectations.core import ExpectationSuite
from great_expectations.validator.validator import Validator
import pandas as pd

# Load CSV manually
csv_path = r"C:\Users\PauloOliveira\py_studies\pdcpbp_book\chapter03\great_expectations\data\iris_data.csv"
df = pd.read_csv(csv_path)

# Create an in-memory Expectation Suite
suite = ExpectationSuite("iris_data_runtime_suite")

# Create a Validator from the DataFrame and suite
validator = Validator(
    execution_engine=None,  # PandasExecutionEngine will be auto-detected
    batches=[df],
    expectation_suite=suite
)

# Quick test: print first rows
print(df.head())

# Save suite to file
context = BaseDataContext()  # default GE context in memory
context.save_expectation_suite(validator.expectation_suite)
print("Expectation Suite saved successfully!")