# -*- coding: utf-8 -*-
from go_library.datamodel.gocam import *

from linkml_runtime.loaders import yaml_loader, json_loader, rdf_loader
from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdf_dumper

import os
from tests import JSONLD_DIR, RESOURCE_DIR

"""Test the module can be imported."""

import unittest

json_in = os.path.join(RESOURCE_DIR, 'sample.json')
a1json = os.path.join(RESOURCE_DIR, 'activity1.json')

class TestLoad(unittest.TestCase):
    """A test case for loading."""

    def test_load(self):
        a1 = json_loader.load(a1json, MolecularActivity)
        print(a1)
        #with open(json_in) as stream:
        m = json_loader.load(json_in, Model)
