# -*- coding: utf-8 -*-
from go_library.datamodel.gocam import *

import go_library.sqla.gocam as sqla_gocam
from linkml_runtime.loaders import yaml_loader, json_loader, rdf_loader

import os
from tests import JSONLD_DIR, RESOURCE_DIR

"""Test the module can be imported."""

import unittest

json_in = os.path.join(RESOURCE_DIR, 'sample.json')
a1json = os.path.join(RESOURCE_DIR, 'activity1.json')

class TestLoad(unittest.TestCase):

    def test_load(self):
        a1 = json_loader.load(a1json, MolecularActivity)
        print(a1)
        with open(json_in) as stream:
            m = json_loader.load(json_in, Model)
        a2 = sqla_gocam.MolecularActivity(id=a1.id)
