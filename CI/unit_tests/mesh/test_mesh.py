"""
ZnVis: A Zincwarecode package.
License
-------
This program and the accompanying materials are made available under the terms
of the Eclipse Public License v2.0 which accompanies this distribution, and is
available at https://www.eclipse.org/legal/epl-v20.html
SPDX-License-Identifier: EPL-2.0
Copyright Contributors to the Zincwarecode Project.
Contact Information
-------------------
email: zincwarecode@gmail.com
github: https://github.com/zincware
web: https://zincwarecode.com/
Citation
--------
If you use this module please cite us with:

Summary
-------
Test the mesh module.
"""
import unittest

import numpy as np

from znvis import Material
from znvis.mesh.mesh import Mesh


class TestMesh(unittest.TestCase):
    """
    A test class for the Particle class.
    """

    def test_instantiation(self):
        """
        Test the instantiation of a Mesh

        Returns
        -------
        Check that parameters are set correctly.
        """
        material = Material(colour=np.array([30, 144, 255]) / 255, alpha=0.9)
        mesh = Mesh(material=material)
        np.testing.assert_array_equal(mesh.material, material)
