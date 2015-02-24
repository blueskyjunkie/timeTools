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

import timeTools.synchronization.compliance.ituTG8262.eecOption1.wanderGeneration as tscg8262eec1


class TestItuTG8262 (unittest.TestCase): 

    def testMtieConstantTemperatureG8262Mask (self):
        thisMask = tscg8262eec1.mtieConstantTemperatureNs
          
        figureHandle = mpp.figure()
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.01, 1000) )
        mpp.ylim( (1, 1000) )
        thisMask.addToPlot(figureHandle.number)
          
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        mpp.title('testMtieConstantTemperatureG8262Mask')
         
 
    def testMtieVariableTemperatureG8262Mask (self):
        constantTempMask = tscg8262eec1.mtieConstantTemperatureNs
        thisMask = tscg8262eec1.mtieTemperatureNs
         
        figureHandle = mpp.figure()
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (1, 1000) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        constantTempMask.addToPlot(figureHandle.number, color='b')
         
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        mpp.title('testMtieVariableTemperatureG8262Mask')
        

    def testTdevConstantTemperatureG8262Mask (self):
        thisMask = tscg8262eec1.tdevConstantTemperatureNs
        
        figureHandle = mpp.figure()
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (0.1, 100) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        mpp.title('testTdevConstantTemperatureG8262Mask')


    def tearDown (self):
        if __name__ == "__main__":
            mpp.show()


if __name__ == "__main__":
    unittest.main()
    