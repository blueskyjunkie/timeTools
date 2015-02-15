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


class Model:
    '''
    A simple clock model with initial static offset and optional Gaussian frequency 
    jitter. The initial time offset is assumed to be zero.
    
    The frequency offset and resulting time offset are returned by 
    calculateOffset. calculateOffset is iterative so that subsequent calls to 
    calculateOffset calculate the offset relative to the last call.
    '''
    
    def __init__ (self, rmsJitterPpb = 0, initialFfoPpb = 0, initialTimeOffsetSeconds = 0, initialReferenceTimeSeconds = 0):
        self._initialFfoPpb = initialFfoPpb
        self._rmsJitterPpb = rmsJitterPpb
        
        # Support iterative use of the model by retaining relevant data from the previous iteration.
        self._lastReferenceTimeSeconds = numpy.array([initialReferenceTimeSeconds])
        self._lastTimeOffsetSeconds = initialTimeOffsetSeconds
        self._lastFfoPpb = initialFfoPpb
        
        
    def calculateOffset (self, referenceTimeSeconds):
        # If there is any time delta between self._lastReferenceTimeSeconds and referenceTimeSeconds[0]
        # then this must be accounted for in the skew and subsequent time integration calculation.
        timeDelta = numpy.diff(numpy.concatenate( (self._lastReferenceTimeSeconds, referenceTimeSeconds) ))
        numberDeltaSamples = len(timeDelta)
        
        jitterPpb = 0
        if self._rmsJitterPpb != 0:
            jitterPpb = numpy.random.normal(scale = self._rmsJitterPpb, size = numberDeltaSamples)
            
        instantaneousLoFfoPpb = (self._initialFfoPpb * numpy.ones(numberDeltaSamples)) + jitterPpb
        # Make sure that the FFO from the previous iteration is accurately accounted for.
        instantaneousLoFfoPpb[0] = self._lastFfoPpb
        
        timeChange = (timeDelta * instantaneousLoFfoPpb * 1e-9) + timeDelta
        
        localTimeSeconds = self._lastTimeOffsetSeconds + numpy.cumsum(timeChange)
        
        self._lastTimeOffsetSeconds = localTimeSeconds[-1]
        self._lastFfoPpb = instantaneousLoFfoPpb[-1]
        self._lastReferenceTimeSeconds = numpy.array([referenceTimeSeconds[-1] ])
        
        return localTimeSeconds, instantaneousLoFfoPpb
    