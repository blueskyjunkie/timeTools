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
import unittest

import timeTools.synchronization.analysis.ituTG810 as sag810
import timeTools.synchronization.time as st
import timeTools.signalProcessing.tolerance as spt

import timeTools.synchronization.clock as tsc


class TestClock (unittest.TestCase):

    def testClock1 (self):
        timeStepSeconds = 1 / 16
        numberSamples = 10
        
        referenceTimeGenerator = st.referenceGenerator(timeStepSeconds)
        referenceTimeSeconds = referenceTimeGenerator.generate(numberSamples)
        
        clockModel = tsc.Model()
        
        localTimeSeconds, instantaneousLoFfoPpb = clockModel.calculateOffset(referenceTimeSeconds)
        
        self.assertTrue(numpy.all(localTimeSeconds == referenceTimeSeconds), 'Timebases not equivalent')
        self.assertTrue(numpy.all(instantaneousLoFfoPpb == 0), 'Instantaneous FFO not zero')


    def testClock2 (self):
        timeStepSeconds = 1 / 16
        numberSamples = 10
        
        referenceTimeGenerator = st.referenceGenerator(timeStepSeconds)
        referenceTimeSeconds = referenceTimeGenerator.generate(numberSamples)
        
        clockModel = tsc.Model()
        
        localTimeSeconds = numpy.array([])
        instantaneousLoFfoPpb = numpy.array([])
        for thisTime in referenceTimeSeconds:
            thisLocalTimeSeconds, thisInstantaneousLoFfoPpb = clockModel.calculateOffset(numpy.array([thisTime]))
            localTimeSeconds = numpy.concatenate( (localTimeSeconds, thisLocalTimeSeconds) )
            instantaneousLoFfoPpb = numpy.concatenate( (instantaneousLoFfoPpb, thisInstantaneousLoFfoPpb) )
        
        self.assertTrue(numpy.all(localTimeSeconds == referenceTimeSeconds), 'Timebases not equivalent')
        self.assertTrue(numpy.all(instantaneousLoFfoPpb == 0), 'Instantaneous FFO not zero')


    def testClock3 (self):
        timeStepSeconds = 1 / 16
        numberSamples = 10
        
        initialFfoPpb = 100e3
        
        expectedLocalTimeSeconds = numpy.array([ 0.0, 0.06250625, 0.1250125, 0.18751875, 0.250025, 0.31253125,
                                                0.3750375, 0.43754375, 0.50005, 0.56255625])
        referenceTimeGenerator = st.referenceGenerator(timeStepSeconds)
        referenceTimeSeconds = referenceTimeGenerator.generate(numberSamples)
        
        expectedTimeErrorSeconds = sag810.calculateTimeError(expectedLocalTimeSeconds, referenceTimeSeconds)
        
        clockModel = tsc.Model(initialFfoPpb = initialFfoPpb)
        
        actualLocalTimeSeconds, instantaneousLoFfoPpb = clockModel.calculateOffset(referenceTimeSeconds)
        actualTimeErrorSeconds = sag810.calculateTimeError(actualLocalTimeSeconds, referenceTimeSeconds)
        
        print(expectedTimeErrorSeconds)
        print(actualTimeErrorSeconds)
        
        self.assertTrue(numpy.all(instantaneousLoFfoPpb == initialFfoPpb), 'Instantaneous FFO not initialFfoPpb')
        thisTolerance = spt.ToleranceValue(expectedTimeErrorSeconds, 0.1, spt.ToleranceUnit['percent'])
        self.assertTrue(numpy.all(thisTolerance.isWithinTolerance(actualTimeErrorSeconds)), 'Timebases not equivalent')


if __name__ == "__main__":
    unittest.main()
    