'''
    This file is part of timetools.

    timetools is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    timetools is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with timetools.  If not, see <http://www.gnu.org/licenses/>.
'''

import matplotlib.pyplot as mpp
import os
import unittest

if __name__ == '__main__':
    thisDir = os.path.dirname( os.path.realpath( __file__ ) )
    testDir = os.path.join( 'timetools', 'tests' )
    
    mpp.ion()
    
    testsuite = unittest.TestLoader().discover( os.path.join( thisDir, testDir ) )
    unittest.TextTestRunner( verbosity = 1 ).run( testsuite )
    
    # Showing all plots is to be deferred until here 
    mpp.show()
    