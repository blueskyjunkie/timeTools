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

import unittest

import timeTools.synchronization.analysis.ituTG810 as sag810
import timeTools.synchronization.clock as sc
import timeTools.synchronization.time as st

import timeTools.synchronization.compliance.time as tsct


class TestComplianceTime (unittest.TestCase):

    def testComplianceTime1 (self):
        timeStepSeconds = 1 / 16
        numberSamples = 2000
        
        clockFfoPpb = 0
        clockRmsJitterPpb = 3.0
        
        referenceTimeGenerator = st.referenceGenerator(timeStepSeconds)
        referenceTimeSeconds = referenceTimeGenerator.generate(numberSamples)
        
        clockModel = sc.Model(initialFfoPpb = clockFfoPpb, rmsJitterPpb = clockRmsJitterPpb)
        localTimeSeconds, instantaneousLoFfoPpb = clockModel.calculateOffset(referenceTimeSeconds)
        
        timeErrorMicroseconds = sag810.calculateTimeError(localTimeSeconds, referenceTimeSeconds) / 1e-6
        
        analysisResult = tsct.time1usMask.evaluate( (referenceTimeSeconds, timeErrorMicroseconds))
        
        self.assertTrue(analysisResult, '1us mask failed when it should not have')
        

    def testComplianceTime2 (self):
        timeStepSeconds = 1 / 16
        numberSamples = 2000
        
        clockFfoPpb = 10
        clockRmsJitterPpb = 3.0
        
        referenceTimeGenerator = st.referenceGenerator(timeStepSeconds)
        referenceTimeSeconds = referenceTimeGenerator.generate(numberSamples)
        
        clockModel = sc.Model(initialFfoPpb = clockFfoPpb, rmsJitterPpb = clockRmsJitterPpb)
        localTimeSeconds, instantaneousLoFfoPpb = clockModel.calculateOffset(referenceTimeSeconds)
        
        timeErrorMicroseconds = sag810.calculateTimeError(localTimeSeconds, referenceTimeSeconds) / 1e-6
        
        analysisResult = tsct.time1usMask.evaluate( (referenceTimeSeconds, timeErrorMicroseconds))
        
        self.assertFalse(analysisResult, '1us mask passed when it should not have')


if __name__ == "__main__":
    unittest.main()
    