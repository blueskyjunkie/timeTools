'''
    This file is part of timeTools.

    timeTools is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    timeTools is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with timeTools.  If not, see <http://www.gnu.org/licenses/>.
'''

import timeTools.synchronization.compliance.analysis as tsca


# ITU-T G.8262/Y.1362 (07/2010), pp 6

# Table 4
mtieConstantTemperatureNs = tsca.Mask([ ([0.1, 1], [20]), 
                                       ([1, 10], ([20], [0.48])), 
                                       ([10, 1000], [60]) ])

# Table 5
tdevConstantTemperatureNs = tsca.Mask([ ([0.1, 2.5], ([3.2], [-0.5])), 
                                       ([2.5, 40], [2]), 
                                       ([40, 1000], ([0.32], [0.5])), 
                                       ([1000, 10000], [10]) ])
