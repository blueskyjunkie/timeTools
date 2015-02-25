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

import timeTools.synchronization.compliance.ituTG8262.eecOption1.wanderGeneration as tscg8262eec1wg
import timeTools.synchronization.compliance.ituTG8262.eecOption1.wanderTolerance as tscg8262eec1wt


class TestItuTG8262 (unittest.TestCase): 

    def testMtieConstantTemperatureG8262WanderGenerationMask (self):
        thisMask = tscg8262eec1wg.mtieConstantTemperatureNs
          
        figureHandle = mpp.figure()
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.01, 1000) )
        mpp.ylim( (1, 1000) )
        thisMask.addToPlot(figureHandle.number)
          
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        mpp.title('testMtieConstantTemperatureG8262WanderGenerationMask')
         
 
    def testMtieVariableTemperatureG8262WanderGenerationMask (self):
        constantTempMask = tscg8262eec1wg.mtieConstantTemperatureNs
        thisMask = tscg8262eec1wg.mtieTemperatureNs
         
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
        mpp.title('testMtieVariableTemperatureG8262WanderGenerationMask')
        

    def testTdevConstantTemperatureG8262WanderGenerationMask (self):
        thisMask = tscg8262eec1wg.tdevConstantTemperatureNs
        
        figureHandle = mpp.figure()
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (0.1, 100) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        mpp.title('testTdevConstantTemperatureG8262WanderGenerationMask')
        

    def testMtieConstantTemperatureG8262WanderToleranceMask (self):
        thisMask = tscg8262eec1wt.mtieMicroseconds
        
        figureHandle = mpp.figure()
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (0.1, 10) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        mpp.title('testMtieConstantTemperatureG8262WanderToleranceMask')
        

    def testTdevConstantTemperatureG8262WanderToleranceMask (self):
        thisMask = tscg8262eec1wt.tdevNs
        
        figureHandle = mpp.figure()
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (1, 1000) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        mpp.title('testTdevConstantTemperatureG8262WanderToleranceMask')


    def tearDown (self):
        if __name__ == "__main__":
            mpp.show()


if __name__ == "__main__":
    unittest.main()
    