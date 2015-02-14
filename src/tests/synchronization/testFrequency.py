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

import timeTools.synchronization.frequency as tsf


class TestFrequency (unittest.TestCase):

    def testConvertSkewToFfoPpb(self):
        inputSkew = numpy.array([1.003, 1.000006, 1.00000005])
        expectedFfoPpb = numpy.array([3e6, 6e3, 50])
        
        actualFfoPpb = tsf.convertSkewToFfoPpb(inputSkew)
        
        thisTolerance = spt.ToleranceValue(expectedFfoPpb, 0.1, spt.ToleranceUnit['percent'])
        self.assertTrue(numpy.all(thisTolerance.isWithinTolerance(actualFfoPpb)), 'Calculated FFO not equivalent')


    def testConvertFfoPpbToSkew(self):
        inputFfoPpb = numpy.array([3e6, 6e3, 50])
        expectedSkew = numpy.array([1.003, 1.000006, 1.00000005])
        
        actualSkew = tsf.convertFfoPpbToSkew(inputFfoPpb)
        
        thisTolerance = spt.ToleranceValue((expectedSkew - 1), 0.1, spt.ToleranceUnit['percent'])
        self.assertTrue(numpy.all(thisTolerance.isWithinTolerance(actualSkew - 1)), 'Calculated skew not equivalent')


if __name__ == "__main__":
    unittest.main()
    