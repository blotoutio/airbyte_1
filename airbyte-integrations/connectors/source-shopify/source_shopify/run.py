#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys
import logging

from airbyte_cdk.entrypoint import launch
from source_shopify.config_migrations import MigrateConfig

from .source import SourceShopify

# Set up logging
logging.basicConfig(level=logging.INFO)


def run() -> None:
    source = SourceShopify()
    # migrate config at runtime
    MigrateConfig.migrate(sys.argv[1:], source)
    # run the connector
    logging.info("Running shopify connector")
    launch(source, sys.argv[1:])
