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


# ITU-T G.8262/Y.1362 (07/2010), pp 11

# Table 11
jitterAmplitude1G = tsca.Mask([ ([10, 12.1], [312.5]), 
                               ([12.1, 2500], ([3750], [-1])), 
                               ([2500, 50000], [1.5]) ])

jitterAmplitude10G = tsca.Mask([ ([10, 12.1], [2488]), 
                                ([12.1, 20000], ([30000], [-1])), 
                                ([20000, 40000], [1.5]) ])
