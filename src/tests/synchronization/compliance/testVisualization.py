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

import timeTools.synchronization.compliance.analysis as complianceAnalysis
import timeTools.synchronization.compliance.visualization as complianceVisualization


class TestVisualization(unittest.TestCase):
    
    def testVisualization1 (self):
        numberSamples = 100
        
        signalBaseline = numpy.linspace(0.0, 20.0, numberSamples)
        signalValues = numpy.random.normal(0.0, 10.0, numberSamples)
        thisSignal = (signalBaseline, signalValues)
        
        thisMask = complianceAnalysis.Mask([( [10.0], [-5.0], [0.0, 10.0] ), ( [0.0, 1.0], [5.0, -1.0], [10, 20] )])
        
        thisPlot = complianceVisualization.plot()
        
        thisPlot.addMask(thisMask, linewidth=4, color='r', linestyle='--')
        thisPlot.addSignal(thisSignal)
        
        thisPlot.go()
        
        maskResult = thisMask.evaluate(thisSignal)
        
        self.assertFalse(maskResult, 'testVisualization (1) failed mask evaluation')
        
        
    def testVisualization2 (self):
        numberSamples = 100
        
        signalBaseline = numpy.linspace(0.0, 20.0, numberSamples)
        signalValues = numpy.random.normal(0.0, 10.0, numberSamples)
        thisSignal = (signalBaseline, signalValues)
        
        # Test that this mask is plotted correctly (a horizontal line for any length of signal).
        thisMask = complianceAnalysis.Mask([( [10.0], [0.0] )])
        
        thisPlot = complianceVisualization.plot()
        
        thisPlot.addMask(thisMask, linewidth=4, color='r', linestyle='--')
        thisPlot.addSignal(thisSignal)
        
        thisPlot.go()
    

if __name__ == "__main__":
    unittest.main()
    