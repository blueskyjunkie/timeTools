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


# Rec. ITU-T G.8262/Y.1362 (07/2010), Section 8.3.1, Table 6, pp 8
amplitude1G = tsca.Mask([ ([2.5e3, 10e6], [0.5]) ])

amplitude10G = tsca.Mask([ ([20e3, 80e6], [0.5]) ])
