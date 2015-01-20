import unittest

import capi_classes

class TestCapiClient(unittest.TestCase):
    # CAPI has two endpoints: /search and /content_id
    # Each endpoint takes common parameters: page-size, api-key
    # Using test-driven development;
    # create a class hierarchy that creates appropriate url strings for each endpoint
    # but whose parameter handling is shared
    pass
