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


# Rec. ITU-T G.8261/Y.1361 (08/2013), Section 9.2.1.1, Table 4, pp 20

mtieNs = tsca.Mask([ ([0.1, 2.5], [250]), 
                    ([2.5, 20], [0, 100]), 
                    ([20, 2000], [2000]), 
                    ([2000], ([0.01, 433], [1, 0.2])) ])
