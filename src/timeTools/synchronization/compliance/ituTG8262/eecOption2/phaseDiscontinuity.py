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


# Rec. ITU-T G.8262/Y.1362 (07/2010), Section 11.4.2, Table 15, pp 18

mtieNs = tsca.Mask([ ([0.014, 0.5], [7.6, 885]), 
                    ([0.5, 2.33], [300, 300]), 
                    ([2.33], [1000])])
