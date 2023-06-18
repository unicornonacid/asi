import logging

from typing import Any
from kedro.framework.hooks import hook_impl
from kedro.io import DataCatalog
from kedro.pipeline.node import Node


class DataCatalogHooks:
    @property
    def _logger(self):
        return logging.getLogger(self.__class__.__name__)

    @hook_impl
    def after_catalog_created(self, catalog: DataCatalog) -> None:
        self._logger.info(catalog.list())

    @hook_impl
    def after_dataset_loaded(self, dataset_name: str, data: Any, node: Node) -> None:
        self._logger.info(f"Loaded {dataset_name} with {data} from {node}")

    @hook_impl
    def after_node_run(self, node: Node):
        self._logger.info(f"Ran ##### # # # # {node}")
