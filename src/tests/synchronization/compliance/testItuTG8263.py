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

import matplotlib.pyplot as mpp
import unittest

import timeTools.synchronization.clock as sc
import timeTools.synchronization.time as st

import timeTools.synchronization.compliance.visualization as tscv

import timeTools.synchronization.compliance.ituTG8263.compute as tscg8263


class TestItuTG8263 (unittest.TestCase):

    def testWanderGenerationConstantTemperatureNs1 (self):
        timeStepSeconds = 1
        numberSamples = 10000
        
        desiredNumberObservations = 15
        
        clockFfoPpb = 0.5
        clockRmsJitterPpb = 2
        
        referenceTimeGenerator = st.referenceGenerator(timeStepSeconds)
        referenceTimeSeconds = referenceTimeGenerator.generate(numberSamples)
        
        clockModel = sc.Model(initialFfoPpb = clockFfoPpb, rmsJitterPpb = clockRmsJitterPpb)
        localTimeSeconds, instantaneousLoFfoPpb = clockModel.calculateOffset(referenceTimeSeconds)
        
        analysisResult, thisMask, mtieData = tscg8263.analyzeItuTG8263Mask(localTimeSeconds, referenceTimeSeconds, timeStepSeconds, desiredNumberObservations)
        
        thisPlot = tscv.plot()
        
        thisPlot.addMask(thisMask, linewidth=4, color='r', linestyle='--', marker='o')
        thisPlot.addSignal(mtieData)
        
        thisPlot.go()
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        
        self.assertTrue(analysisResult, 'Failed 16 ppb mask when should not have')


    def testWanderGenerationConstantTemperatureNs2 (self):
        timeStepSeconds = 1
        numberSamples = 10000
        
        desiredNumberObservations = 15
        
        clockFfoPpb = 5
        clockRmsJitterPpb = 2
        
        referenceTimeGenerator = st.referenceGenerator(timeStepSeconds)
        referenceTimeSeconds = referenceTimeGenerator.generate(numberSamples)
        
        clockModel = sc.Model(initialFfoPpb = clockFfoPpb, rmsJitterPpb = clockRmsJitterPpb)
        localTimeSeconds, instantaneousLoFfoPpb = clockModel.calculateOffset(referenceTimeSeconds)
        
        analysisResult, thisMask, mtieData = tscg8263.analyzeItuTG8263Mask(localTimeSeconds, referenceTimeSeconds, timeStepSeconds, desiredNumberObservations)
        
        thisPlot = tscv.plot()
        
        thisPlot.addMask(thisMask, linewidth=4, color='r', linestyle='--')
        thisPlot.addSignal(mtieData, linestyle='--', marker='o')
        
        thisPlot.go()
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        
        self.assertFalse(analysisResult, 'Passed 16 ppb mask when should not have')


if __name__ == "__main__":
    unittest.main()
    