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

import timeTools.synchronization.compliance.ituTG8261.eecOption1.networkWander as tscg8261eec1nw


class TestItuTG8261 (unittest.TestCase):

    def testEecOption1MtieMask (self):
        thisMask = tscg8261eec1nw.mtieNs
          
        figureHandle = mpp.figure()
        mpp.title(self.testEecOption1MtieMask.__name__)
        # Set the plot limits before the mask plot so that it will figure out 
        # appropriate ranges in the absence of signal data
        mpp.xlim( (0.1, 100000) )
        mpp.ylim( (100, 10000) )
        thisMask.addToPlot(figureHandle.number)
          
        mpp.yscale('log')
        mpp.xscale('log')
        mpp.grid(which='minor')
        

    def tearDown (self):
        if __name__ == "__main__":
            mpp.show()


if __name__ == "__main__":
    unittest.main()
    