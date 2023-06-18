from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data, train_model, evaluate_model, register_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["clean_data", "params:model_options"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data_node",
                tags=["split", "all", "data_science"],
            ),
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="regressor",
                name="train_model_node",
                tags=["train", "all", "data_science"],
            ),
            node(
                func=evaluate_model,
                inputs=["regressor", "X_test", "y_test"],
                outputs=None,
                name="evaluate_model_node",
                tags=["evaluate", "all", "data_science"],
            ),
            node(
                func=register_model,
                inputs=["regressor"],
                outputs="prod_model",
                name="register_model",
                tags=["register", "all", "data_science"],
            ),
        ]
    )
