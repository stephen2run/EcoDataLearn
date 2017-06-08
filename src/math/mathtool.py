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

"""Builds the mathtool function
Implements the mathtool
"""
from approximation import *
from regression import *

# Approximation
approx_obj = MathApprox()
approx_obj.handle()
x = approx_obj.get_x()
y = approx_obj.get_y()

# Regression
deg = 1
regress_obj = MathRegress(x, y)
regress_obj.handle(deg)

deg = 7
regress_obj.handle(deg)