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
import numpy
import unittest

import timeTools.synchronization.compliance.analysis as sca


class TestAnalysis(unittest.TestCase):
    
    def testMask1 (self):
        thisMask = sca.Mask([( [10.0], [0.0] )])
        
        # The signal exceeds the mask bound so the evaluation should fail
        signal = (numpy.arange(0.0, 12.0), numpy.arange(0.0, 12.0))
        
        self.assertFalse(thisMask.evaluate(signal), 'Mask (1) bound test failed')
        
        
    def testMask2 (self):
        thisMask = sca.Mask([( [12.0], [0.0] )])
        
        # The signal is equal to the mask bounds so the evaluation should pass
        signal = (numpy.arange(0.0, 12.0), numpy.arange(0.0, 12.0))
        
        self.assertTrue(thisMask.evaluate(signal), 'Mask (2) bound test failed')


    def testMask3 (self):
        thisMask = sca.Mask([( [10.0], [0.0, 10.0] )])
        
        # The signal is <= the mask bound for the specified interval so the evaluation should pass
        signal = (numpy.arange(0.0, 12.0), numpy.arange(0.0, 12.0))
        
        self.assertTrue(thisMask.evaluate(signal), 'Mask (3) bound test failed')


    def testMask4 (self):
        thisMask = sca.Mask([( [10.0], [-1.0], [0.0, 10.0] )])
        
        # The signal >= the mask bound on the lower bound side and <= the mask bound on the 
        # upper bound side over the mask interval so the evaluation should pass
        signal = (numpy.arange(0.0, 12.0), numpy.arange(0.0, 12.0))
        
        self.assertTrue(thisMask.evaluate(signal), 'Mask (3) bound test failed')


    def testPlotMask1 (self):
        thisMask = sca.Mask([( [10.0], [0.0, 10.0] ), ( [0.0, 1.0], [10, 20] ), ( [20.0], [20.0, 30.0] ), ( [170, -8.0, 0.1], [30.0, 40.0])])
        
        figureHandle = mpp.figure()
        thisMask.addToPlot(figureHandle.number)
        
        axisHandle = mpp.gca()
        
        axisHandle.set_ylim([0, 30])


    def testPlotMask2 (self):
        thisMask = sca.Mask([( [10.0], [0.0, 10.0] ), ( [0.0, 1.0], [10, 20] ), ( [20.0], [20.0, 30.0] ), ( [170, -8.0, 0.1], [30.0, 40.0])])
        
        figureHandle = mpp.figure()
        # Test adding line properties
        thisMask.addToPlot(figureHandle.number, linewidth=3, linestyle='-', color='r')
        
        axisHandle = mpp.gca()
        
        axisHandle.set_ylim([0, 30])


    def testPlotMask3 (self):
        thisMask = sca.Mask([( [10.0], [-5.0], [0.0, 10.0] ), ( [0.0, 1.0], [5.0, -1.0], [10, 20] )])
        
        figureHandle = mpp.figure()
        thisMask.addToPlot(figureHandle.number)
        
        axisHandle = mpp.gca()
        
        axisHandle.set_ylim([-20, 30])


    def testPlotMask4 (self):
        thisMask = sca.Mask([( [10.0], [0.0] )])
        
        figureHandle = mpp.figure()
        thisMask.addToPlot(figureHandle.number)
        
        axisHandle = mpp.gca()
        
        axisHandle.set_ylim([0, 30])
        

if __name__ == "__main__":
    unittest.main()
    