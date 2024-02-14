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
Test the visualizer module.
"""

import time
import unittest

import numpy as np
import open3d as o3d

from znvis.mesh.sphere import Sphere
from znvis.particle.particle import Particle
from znvis.testing.znvis_process import Process
from znvis.visualizer.visualizer import Visualizer


class TestVisualizer(unittest.TestCase):
    """
    A test class for the Particle class.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up the class for testing.
        """
        name = "my_particle"
        position = np.random.uniform(-5, 5, (10, 2, 3))
        particle = Particle(name=name, position=position, mesh=Sphere())
        cls.visualizer = Visualizer([particle])

    def test_instantiation(self):
        """
        Test the class instantiation.

        Returns
        -------
        Check the class was built correctly.
        """
        self.assertEqual(self.visualizer.number_of_steps, 10)
        self.assertEqual(self.visualizer.counter, 0)

    def test_initialize_app(self):
        """
        test instantiation of the app.

        Returns
        -------
        Test that the app initializes properly.
        """
        process = Process(target=self.initialize_app)
        process.start()
        time.sleep(1)
        process.terminate()
        if process.exception:
            error, traceback = process.exception
            print(traceback)
        self.assertEqual(process.exception, None)

    def initialize_app(self):
        """
        Test initializing the app.

        Returns
        -------

        """
        self.visualizer._initialize_app()
        self.assertEqual(type(self.visualizer.vis), o3d.visualization.O3DVisualizer)
