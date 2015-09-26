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

import timeTools.signalProcessing.tolerance as spt

import timeTools.synchronization.analysis.tdevKernels as satk


class TestTdevKernels(unittest.TestCase):

    def testMean(self):
        timeError = numpy.array([1, 0, 4, 2, 5, 1, 4, 0, 3])
        n = 3
        j = 1
        
        expectedResult = -1.333333333
        
        actualResult = satk.mean(timeError, n, j)
        
        resultTest = spt.ToleranceValue(expectedResult, 0.1, spt.ToleranceUnit['percent'])
        self.assertTrue(resultTest.isWithinTolerance(actualResult), 'Mean kernel wrong result')


    def testMinimum(self):
        timeError = numpy.array([1, 0, 4, 2, 5, 1, 4, 0, 3])
        n = 3
        j = 1
        
        expectedResult = -2
        
        actualResult = satk.minimum(timeError, n, j)
        
        resultTest = spt.ToleranceValue(expectedResult, 0.1, spt.ToleranceUnit['percent'])
        self.assertTrue(resultTest.isWithinTolerance(actualResult), 'Mean kernel wrong result')
        

if __name__ == "__main__":
    unittest.main()
    