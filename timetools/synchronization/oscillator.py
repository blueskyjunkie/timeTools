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

import logging
import numpy


class NoiseModel:

    def __init__( self, seed = None ):
        self.randomState = numpy.random.RandomState( seed = seed )


class GaussianNoise( NoiseModel ):

    def __init__( self, standardDeviationPpb = 1, seed = None ):
        super().__init__( seed )
        self._standardDeviationPpb = standardDeviationPpb


    def generate( self, referenceTimeSeconds ):
        thisNoise = self.randomState.normal( scale = self._standardDeviationPpb, size = referenceTimeSeconds.shape )

        return thisNoise


class LinearAging:

    def __init__( self, agingRatePpbPerDay, initialAgePpb = 0, initialAgeTimeSeconds = 0 ):
        self._agingRatePpbPerDay = agingRatePpbPerDay
        self._agingRatePpbPerSecond = self._agingRatePpbPerDay / ( 3600 * 24 )
        self._initialAgePpb = initialAgePpb
        self._initialAgeTimeSeconds = initialAgeTimeSeconds


    def generate( self, referenceTimeSeconds ):
        offsetTimeSeconds = referenceTimeSeconds - self._initialAgeTimeSeconds

        ffoPpb = ( offsetTimeSeconds * self._agingRatePpbPerSecond ) + self._initialAgePpb

        return ffoPpb


class LinearTemperatureSensitivity:

    def __init__( self, temperatureSensitivityPpbPerKelvin, referenceTemperatureKelvin = 293.15 ):
        self._referenceTemperatureKelvin = referenceTemperatureKelvin
        self._sensitivityPpbPerKelvin = temperatureSensitivityPpbPerKelvin


    def generate( self, referenceTemperatureKelvin ):
        # Assume zero ppb offset at the reference temperature
        ffoPpb = ( referenceTemperatureKelvin - self._referenceTemperatureKelvin ) \
                 * self._sensitivityPpbPerKelvin

        return ffoPpb


class OscillatorModel:

    def __init__( self, initialFfoPpb = 0, agingModel = None, temperatureSensitivityModel = None, noiseModel = None ):
        self._initialFfoPpb = initialFfoPpb
        self._agingModel = agingModel
        self._temperatureSensitivityModel = temperatureSensitivityModel
        self._noiseModel = noiseModel


    def generate( self, referenceTimeSeconds, referenceTemperatureKelvin = None ):

        ffoPpb = numpy.ones( referenceTimeSeconds.shape ) * self._initialFfoPpb

        if self._agingModel is not None:
            ffoPpb += self._agingModel.generate( referenceTimeSeconds )

        if self._noiseModel is not None:
            ffoPpb += self._noiseModel.generate( referenceTimeSeconds )

        if self._temperatureSensitivityModel is not None and referenceTemperatureKelvin is not None:
            assert( numpy.all( referenceTemperatureKelvin.shape == referenceTemperatureKelvin.shape ) )
            ffoPpb += self._temperatureSensitivityModel.generate( referenceTemperatureKelvin )

        elif referenceTemperatureKelvin is None and self._temperatureSensitivityModel is not None:
            logging.warning( 'Temperature sensitivity model was specified but reference temperature not specified for FFO calculations.' )

        elif referenceTemperatureKelvin is not None and self._temperatureSensitivityModel is None:
            logging.warning( 'Temperature sensitivity model was not specified but reference temperature was specified for FFO calculations.' )

        return ffoPpb
