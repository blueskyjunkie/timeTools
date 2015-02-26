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
import timeTools.synchronization.compliance.ituTG8262.eecOption2.wanderGeneration as tscg8262eec2wg
import timeTools.synchronization.compliance.ituTG8262.eecOption2.wanderTolerance as tscg8262eec2wt
import timeTools.synchronization.compliance.ituTG8262.jitterTolerance as tscg8262jt
import timeTools.synchronization.compliance.ituTG8262.eecOption2.wanderTransfer as tscg8262eec2wtf
import timeTools.synchronization.compliance.ituTG8262.eecOption2.transient as tscg8262eec2t


class TestItuTG8262 (unittest.TestCase):

    def testEec1MtieConstantTemperatureG8262WanderGenerationMask (self):
        thisMask = tscg8262eec1wg.mtieConstantTemperatureNs
          
        figureHandle = mpp.figure()
        mpp.title('testEec1MtieConstantTemperatureG8262WanderGenerationMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.01, 1000) )
        mpp.ylim( (1, 1000) )
        thisMask.addToPlot(figureHandle.number)
          
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
         
 
    def testEec1MtieVariableTemperatureG8262WanderGenerationMask (self):
        constantTempMask = tscg8262eec1wg.mtieConstantTemperatureNs
        thisMask = tscg8262eec1wg.mtieTemperatureNs
         
        figureHandle = mpp.figure()
        mpp.title('testEec1MtieVariableTemperatureG8262WanderGenerationMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (1, 1000) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        constantTempMask.addToPlot(figureHandle.number, color='b')
         
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def testEec1TdevConstantTemperatureG8262WanderGenerationMask (self):
        thisMask = tscg8262eec1wg.tdevConstantTemperatureNs
        
        figureHandle = mpp.figure()
        mpp.title('testEec1TdevConstantTemperatureG8262WanderGenerationMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (0.1, 100) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def testEec1MtieConstantTemperatureG8262WanderToleranceMask (self):
        thisMask = tscg8262eec1wt.mtieMicroseconds
        
        figureHandle = mpp.figure()
        mpp.title('testEec1MtieConstantTemperatureG8262WanderToleranceMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (0.1, 10) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def testEec1TdevConstantTemperatureG8262WanderToleranceMask (self):
        thisMask = tscg8262eec1wt.tdevNs
        
        figureHandle = mpp.figure()
        mpp.title('testEec1TdevConstantTemperatureG8262WanderToleranceMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (1, 1000) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def testEec2MtieConstantTemperatureG8262WanderGenerationMask (self):
        thisMask = tscg8262eec2wg.mtieConstantTemperatureNs
          
        figureHandle = mpp.figure()
        mpp.title('testEec2MtieConstantTemperatureG8262WanderGenerationMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.01, 1000) )
        mpp.ylim( (1, 1000) )
        thisMask.addToPlot(figureHandle.number)
          
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def testEec2TdevConstantTemperatureG8262WanderGenerationMask (self):
        thisMask = tscg8262eec2wg.tdevConstantTemperatureNs
        
        figureHandle = mpp.figure()
        mpp.title('testEec2TdevConstantTemperatureG8262WanderGenerationMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (0.1, 100) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def testEec2TdevG8262WanderToleranceMask (self):
        thisMask = tscg8262eec2wt.tdevNs
        
        figureHandle = mpp.figure()
        mpp.title('testEec2TdevG8262WanderToleranceMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (1, 1000) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def testG8262JitterTolerance1GMask (self):
        thisMask = tscg8262jt.jitterAmplitude1G
        
        figureHandle = mpp.figure()
        mpp.title('testG8262JitterTolerance1GMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (10, 1000000) )
        mpp.ylim( (0.1, 1000) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def testG8262JitterTolerance10GMask (self):
        thisMask = tscg8262jt.jitterAmplitude10G
        
        figureHandle = mpp.figure()
        mpp.title('testG8262JitterTolerance10GMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (10, 1000000) )
        mpp.ylim( (0.1, 10000) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def testEec2TdevG8262WanderTransferMask (self):
        thisMask = tscg8262eec2wtf.tdevNs
        
        figureHandle = mpp.figure()
        mpp.title('testEec2TdevG8262WanderTransferMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 1000) )
        mpp.ylim( (1, 1000) )
        thisMask.addToPlot(figureHandle.number, linewidth=3, color='r')
        
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def testEec2MtieTransientMask (self):
        thisMask = tscg8262eec2t.transientMtieNs
          
        figureHandle = mpp.figure()
        mpp.title('testEec2MtieTransientMask')
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.014, 10) )
        mpp.ylim( (10, 1000) )
        thisMask.addToPlot(figureHandle.number)
          
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')


    def tearDown (self):
        if __name__ == "__main__":
            mpp.show()


if __name__ == "__main__":
    unittest.main()
    