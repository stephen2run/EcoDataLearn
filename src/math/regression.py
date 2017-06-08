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

"""Builds the regression function
Implements the regression
"""

from __init__ import *

class MathRegress:
    def __init__(self, x, y):
        print("Test Math Regression")
        self.x = x
        self.y = y

    def regression(self):
        reg = np.polyfit(self.x, self.y, self.deg)
        self.ry = np.polyval(reg, self.x)

    def plot2d(self):
        plt.plot(self.x, self.y, 'b', label='f(x)')
        plt.plot(self.x, self.ry, 'r.', label='regression')
        plt.title('Regression with degree' + str(self.deg))
        plt.legend(loc=0)
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.show()

    def handle(self, deg):
        self.deg = deg
        self.regression()
        self.plot2d()