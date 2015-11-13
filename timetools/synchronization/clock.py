'''
    This file is part of timetools.

    timetools is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    timetools is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with timetools.  If not, see <http://www.gnu.org/licenses/>.
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
    
    def __init__( self, oscillatorModel, initialTimeOffsetSeconds = 0, initialReferenceTimeSeconds = 0, initialReferenceTemperatureKelvin = 0 ):
        # Support iterative use of the model by retaining relevant data from the previous iteration.
        self._lastReferenceTimeSeconds = numpy.array( [ initialReferenceTimeSeconds ] )
        self._lastReferenceTemperatureKelvin = numpy.array( [ initialReferenceTemperatureKelvin ] )
        self._lastTimeOffsetSeconds = initialTimeOffsetSeconds
        self._lastInstantaneousFfoPpb = numpy.array( [ oscillatorModel._initialFfoPpb ] )

        self._oscillatorModel = oscillatorModel
        

    def calculateOffset( self, referenceTimeSeconds, referenceTemperatureKelvin = None ):
        # If there is any time delta between self._lastReferenceTimeSeconds and referenceTimeSeconds[0]
        # then this must be accounted for in the skew and subsequent time integration calculation.
        timeDelta = numpy.diff( numpy.concatenate( ( self._lastReferenceTimeSeconds, referenceTimeSeconds ) ) )

        thisIterationReferenceTime = referenceTimeSeconds[ : ( len( referenceTimeSeconds ) - 1 ) ]
        thisIterationReferenceTemperature = None
        if referenceTemperatureKelvin is not None:
            thisIterationReferenceTemperature = referenceTemperatureKelvin[ : ( len( referenceTemperatureKelvin ) - 1 ) ]
            
        loFfoPpb = \
            self._oscillatorModel.generate(
                thisIterationReferenceTime,
                thisIterationReferenceTemperature )
        # Make sure that the FFO from the previous iteration is accurately accounted for.
        instantaneousLoFfoPpb = self._lastInstantaneousFfoPpb
        if loFfoPpb != []:
            instantaneousLoFfoPpb = numpy.concatenate( ( self._lastInstantaneousFfoPpb, loFfoPpb ) )

        assert ( instantaneousLoFfoPpb.shape == timeDelta.shape )

        timeChange = ( timeDelta * instantaneousLoFfoPpb * 1e-9 ) + timeDelta
        localTimeSeconds = self._lastTimeOffsetSeconds + numpy.cumsum( timeChange )

        assert ( localTimeSeconds.shape == referenceTimeSeconds.shape )
        
        self._lastTimeOffsetSeconds = localTimeSeconds[-1]
        self._lastInstantaneousFfoPpb = numpy.array( [ instantaneousLoFfoPpb[-1] ] )
        # Make this a numpy array even though it is only a single scalar so that numpy concatenation works for
        # timeDelta calculation.
        self._lastReferenceTimeSeconds = numpy.array( [ referenceTimeSeconds[-1] ] )
        if referenceTemperatureKelvin is not None:
            self._lastReferenceTemperatureKelvin = numpy.array( [ referenceTemperatureKelvin[-1] ] )
        
        return localTimeSeconds, instantaneousLoFfoPpb
    