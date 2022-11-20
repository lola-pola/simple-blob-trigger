import logging

import azure.functions as func


def main(myblob):
    logging.info(f"f{myblob}")
