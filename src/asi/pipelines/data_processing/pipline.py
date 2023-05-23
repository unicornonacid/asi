from kedro.pipeline import Pipeline, node, pipeline
from .nodes import generate_data, clean_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=generate_data,
                inputs=["params:data_generation_options"],
                outputs="generated_data",
                name="generate_data_node",
            ),
            node(
                func=clean_data,
                inputs="generated_data",
                outputs="clean_data",
                name="clean_data_node",
            )
        ]
    )
