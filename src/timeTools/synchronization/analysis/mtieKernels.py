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

import numpy


def slidingWindow (timeError, thisInterval):
    thisMtie = 0
    for m in numpy.arange(0, timeError.size, 1):
        thisWindow = timeError[m : (m + thisInterval + 1) : 1]
        maxError = numpy.max(thisWindow)
        minError = numpy.min(thisWindow)
        
        peakToPeakError = maxError - minError;
        
        if peakToPeakError > thisMtie:
            thisMtie = peakToPeakError
            
    return thisMtie


def smartWindow (timeError, thisInterval):
    
    def findMaximumPosition (thisWindow, m):
        maxWindowPosition = numpy.argmax(thisWindow)
        
        maxSignalPosition = maxWindowPosition + m
        
        return maxSignalPosition
    
    
    def findMinimumPosition (thisWindow, m):
        minWindowPosition = numpy.argmin(thisWindow)
        
        minSignalPosition = minWindowPosition + m
        
        return minSignalPosition
    
    thisMtie = 0
    
    m = 0
    completed = False
    lastIteration = False
    while not completed:
        thisWindow = timeError[m : (m + thisInterval + 1) : 1]
        maxError = numpy.max(thisWindow)
        minError = numpy.min(thisWindow)
        
        peakToPeakError = maxError - minError;
        
        if peakToPeakError > thisMtie:
            thisMtie = peakToPeakError
        
        maxSignalPosition = findMaximumPosition(thisWindow, m)
        minSignalPosition = findMinimumPosition(thisWindow, m)
        
        nextWindowPosition = numpy.min([maxSignalPosition, minSignalPosition])
            
        if lastIteration:
            completed = True
        
        if nextWindowPosition == m:
            nextWindowPosition = numpy.max([maxSignalPosition, minSignalPosition])
        
        if (nextWindowPosition + thisInterval) >= timeError.size:
            nextWindowPosition = timeError.size - thisInterval
            lastIteration = True
            
        m = nextWindowPosition
        
    return thisMtie
