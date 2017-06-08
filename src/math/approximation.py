# Copyright 2017 The EcoDataLearn. All Rights Reserved.
# Author Stephen (Yu) Shao
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Builds the approximation function
Implements the approximation
"""

from __init__ import *

class MathApprox:
    def __init__(self):
        print("Test Math Approximation")

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def f(self, x):
        return np.sin(x) + 0.5 * x

    def plot2d(self):
        plt.plot(self.x, self.y, 'b')
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.show()

    def handle(self):
        self.x = np.linspace(-2 * np.pi, 2 * np.pi, 50)
        self.y = self.f(self.x)
        self.plot2d()