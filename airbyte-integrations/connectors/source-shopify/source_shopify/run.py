#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys
import logging

from airbyte_cdk.entrypoint import launch
from source_shopify.config_migrations import MigrateConfig

from .source import SourceShopify


# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)  # You can adjust the level as needed (DEBUG, WARNING, ERROR)
logger = logging.getLogger(__name__)


def run() -> None:
    logger.info("Starting the Shopify connector...")
    source = SourceShopify()
    logger.info("SourceShopify instance created.")
    # migrate config at runtime
    MigrateConfig.migrate(sys.argv[1:], source)
    # run the connector
    launch(source, sys.argv[1:])
