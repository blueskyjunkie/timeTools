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


# Wander generation, Section 6.1, Rec. ITU-T G.8263/Y.1363 (02/2012), pp5
constantTemperatureMtieNs = tsca.Mask([([0.1, 1000], [1000]), ([1000], [0, 1])])

variableTemperatureMtieNs = tsca.Mask([([0.1, 100], [1000]), ([100], [0, 10])])
