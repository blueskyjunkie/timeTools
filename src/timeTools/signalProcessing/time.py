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

import math


def printTime (elapsedTimeSeconds):
    timeText = ''
    if elapsedTimeSeconds >= 3600:
        hrs = math.floor(elapsedTimeSeconds / 3600)
        timeText += (repr(hrs) + ' hrs, ')
        
        remainder = elapsedTimeSeconds - (hrs * 3600)
        
        timeText += printTime(remainder)
    elif elapsedTimeSeconds >= 60:
        mins = math.floor(elapsedTimeSeconds / 60)
        timeText += (repr(mins) + ' min, ')
        
        remainder = elapsedTimeSeconds - (mins * 60)
        
        timeText += printTime(remainder)
    else:
        timeText = repr(elapsedTimeSeconds) + ' s'
        
    return timeText
