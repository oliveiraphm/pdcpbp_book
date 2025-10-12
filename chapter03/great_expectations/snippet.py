from great_expectations.data_context import get_context

context = get_context()
datasource = context.get_datasource("iris_data")
print(datasource.get_available_data_asset_names())