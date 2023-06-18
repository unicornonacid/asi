from kedro.pipeline import Pipeline, node, pipeline
from .nodes import generate_data, clean_data, register_base_data, data_drift_check


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=generate_data,
                inputs=["params:data_generation_options"],
                outputs="generated_data",
                name="generate_data_node",
                tags=["generate", "all", "data_processing"],
            ),
            node(
                func=clean_data,
                inputs="generated_data",
                outputs="clean_data",
                name="clean_data_node",
                tags=["clean", "all", "data_processing"],
            ),
            node(
                func=register_base_data,
                inputs="clean_data",
                outputs="base_data",
                name="register_base_data_node",
                tags=["register_base_data", "all", "data_processing"],
            ),
            node(
                func=data_drift_check,
                inputs=["base_data", "clean_data"],
                outputs=None,
                name="data_drift_check",
                tags=["data_drift_check", "all", "data_processing"],
            ),
        ]
    )
