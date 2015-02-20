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

import timeTools.synchronization.compliance.general as generalCompliance

time1usMask = generalCompliance.createSimpleThresholdMask(1.0, 0, lowerThreshold=-1.0)
time500nsMask = generalCompliance.createSimpleThresholdMask(0.5, 0, lowerThreshold=-0.5)

time1msMask = generalCompliance.createSimpleThresholdMask(1000, 0, lowerThreshold=-1000)
time500usMask = generalCompliance.createSimpleThresholdMask(500, 0, lowerThreshold=-500)
