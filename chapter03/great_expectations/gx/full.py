from great_expectations.data_context import get_context
from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations.profile.user_configurable_profiler import UserConfigurableProfiler
import pandas as pd

# Load CSV
csv_path = r"C:\Users\PauloOliveira\py_studies\pdcpbp_book\chapter03\great_expectations\data\iris_data.csv"
df = pd.read_csv(csv_path)

# Load GE context
context = get_context()

# Add runtime datasource if it does not exist
datasource_config = {
    "name": "iris_data_runtime",
    "class_name": "Datasource",
    "execution_engine": {"class_name": "PandasExecutionEngine"},
    "data_connectors": {
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "batch_identifiers": ["default_identifier_name"]
        }
    },
}

if "iris_data_runtime" not in context.list_datasources():
    context.add_datasource(**datasource_config)

# Create RuntimeBatchRequest
batch_request = RuntimeBatchRequest(
    datasource_name="iris_data_runtime",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="iris_data_runtime_asset",
    runtime_parameters={"batch_data": df},
    batch_identifiers={"default_identifier_name": "default"},
)

# Get validator
validator = context.get_validator(batch_request=batch_request)

# Run automatic profiling
profiler = UserConfigurableProfiler(profile_dataset=validator)
suite = profiler.build_suite()
validator.expectation_suite = suite

# Preview data
print(validator.head())

# Save expectation suite correctly
validator.save_expectation_suite(discard_failed_expectations=False)
context.save_expectation_suite(
    expectation_suite=validator.expectation_suite,
    expectation_suite_name="iris_data_auto_suite"
)
print("Expectation Suite 'iris_data_auto_suite' created successfully!")