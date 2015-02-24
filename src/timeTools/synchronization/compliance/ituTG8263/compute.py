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

import timeTools.synchronization.analysis.fastMtie as tsam
import timeTools.synchronization.compliance.ituTG8263.wanderGeneration as tscg8263wg


def analyzeItuTG8263Mask (localTimeSeconds, referenceTimeSeconds, samplingIntervalSeconds, desiredNumberObservations):
    mtieSeconds, observationIntervalsSeconds = tsam.calculateMtie(localTimeSeconds, 
                                                                  referenceTimeSeconds, 
                                                                  samplingIntervalSeconds, 
                                                                  desiredNumberObservations)
    
    mtieNanoseconds = mtieSeconds / 1e-9
    
    analysisResult = tscg8263wg.constantTemperatureNs.evaluate( (observationIntervalsSeconds, mtieNanoseconds) )
    
    return analysisResult, tscg8263wg.constantTemperatureNs, (observationIntervalsSeconds, mtieNanoseconds)
