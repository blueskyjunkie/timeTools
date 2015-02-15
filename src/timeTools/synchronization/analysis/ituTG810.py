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
import numpy

import timeTools.synchronization.analysis.mtieKernels as samk
import timeTools.synchronization.analysis.tdevKernels as satk
import timeTools.synchronization.intervals as si


def calculateTimeError (localTime, referenceTime):
    '''
    Calculate Time Error (TE) of two timebases assuming they are identically, uniformly sampled.
    
    Assume localTime and referenceTime are numpy arrays.
    
    "Definitions and terminology for synchronization networks", ITU-T G.810 (08/96), Section 4.5.13, pp7
    '''
    assert(localTime.size == referenceTime.size)
    
    return(localTime - referenceTime)


def calculateTimeIntervalError (localTime, referenceTime, intervalSamples):
    '''
    Calculate Time Interval Error (TIE) of two timebases assuming they are identically, uniformly sampled.
    
    Assume localTime and referenceTime are numpy arrays.
    
    "Definitions and terminology for synchronization networks", ITU-T G.810 (08/96), Section 4.5.14, pp7
    '''
    assert(localTime.size == referenceTime.size)
    timeError = calculateTimeError(localTime, referenceTime)
    
    return(timeError[intervalSamples:timeError.size:1] - timeError[0:(timeError.size - intervalSamples):1])


def calculateMtie (localTime, referenceTime, samplingInterval, desiredNumberObservations):
    '''
    Calculate Maximum Time Interval Error (MTIE) of two timebases using the 
    direct method, assuming they are identically, uniformly sampled.
    
    "Definitions and terminology for synchronization networks", ITU-T G.810 (08/96), Section 4.5.15, pp7
    
    The ITU definition does a direct calculation on all windows sizes, but here a logarithmic scale is used 
    to improve computational efficiency slightly.
    
    Assume localTime and referenceTime are numpy arrays.
    '''
    assert(len(localTime) > 1)
    assert(len(referenceTime) > 1)
    assert(localTime.size == referenceTime.size)
    
    timeError = calculateTimeError(localTime, referenceTime)

    maxIntervalIndex = len(localTime) - 1
    
    intervalIndex = si.generateMonotonicLogScale(numpy.floor(si.generateLogIntervalScale(1, maxIntervalIndex, desiredNumberObservations)))
    mtie = numpy.zeros(intervalIndex.size)
    
    for k in numpy.arange(0, len(intervalIndex)):
        thisInterval = intervalIndex[k]
        
        mtie[k] = samk.slidingWindow(timeError, thisInterval)
    
    observationIntervals = samplingInterval * intervalIndex

    return (mtie, observationIntervals)


def calculateTdev (localTime, referenceTime, samplingInterval, desiredNumberObservations, kernel = satk.mean):
    assert(len(localTime) > 1)
    assert(len(referenceTime) > 1)
    assert(referenceTime.size == localTime.size)

    # Assume the signal is uniformly sampled.
    timeError = calculateTimeError(localTime, referenceTime)

    numberErrorPoints = len(timeError)
    rawTdevSize = math.floor(numberErrorPoints / 3)
    maxIntervalIndex = rawTdevSize

    intervalIndex = si.generateMonotonicLogScale(numpy.floor(si.generateLogIntervalScale(1, maxIntervalIndex, desiredNumberObservations)))
    
    # ITU-T Rec. G.810 (08/96) pp 17
    rawTdev = numpy.zeros(rawTdevSize)
    for n in (numpy.arange(0, rawTdevSize) + 1):
        iterationSize = numberErrorPoints - (3 * n) + 1
        tdevFactor = 1 / (6 * iterationSize)
        
        tdevSum = 0
        for j in (numpy.arange(0, iterationSize) + 1):
            tdevSum += numpy.power(kernel(timeError, n, j), 2)
        
        rawTdev[n - 1] = math.sqrt(tdevFactor * tdevSum)
    
    # Reduce the resolution to that specified
    # In the case of the direct TDEV method, this doesn't improve computation time, but it does improve memory usage
    tdev = rawTdev[intervalIndex - 1]
    
    observationIntervals = samplingInterval * intervalIndex
    
    return (tdev, observationIntervals)
