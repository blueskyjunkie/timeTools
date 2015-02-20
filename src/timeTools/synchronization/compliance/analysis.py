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
import numpy.polynomial.polynomial as polynomial
import matplotlib.pyplot as mpp


class ComplianceException (Exception):
    
    def __init__ (self, value):
        self.value = value
        
        
    def __str__(self):
        return repr(self.value)


class ValidationException (Exception):
    
    def __init__ (self, value):
        self.value = value
        
        
    def __str__(self):
        return repr(self.value)


class Mask:
    '''
    A mask is comprised of a set of intervals over which a signal may be 
    analysed for compliance to the mask specification.
    '''
    def __init__ (self, intervalSet):
        self._intervalSet = intervalSet
        
        self._validateIntervalSet()
        
        
    def evaluate (self, signal):
        '''
        Establish that the signal is always within the specified mask bounds.
        '''
        result = True
        for thisInterval in self._intervalSet:
            if len(thisInterval) == 2:
                # Upper bound only spec
                result = self._evaluateUpperBound(thisInterval, signal)
                
            elif len(thisInterval) == 3:
                # lower & upper bound spec
                result = self._evaluateUpperLowerBound(thisInterval, signal)
                    
            else:
                raise ValidationException('Wrong number of elements in interval tuple')
                
        return result
    
    
    def addToPlot (self, figureInstanceNumber, *args, **kwargs):
        '''
        Add the mask to the specified Matplotlib figure.
        '''
        mpp.figure(figureInstanceNumber)
        
        for thisInterval in self._intervalSet:
            if len(thisInterval) == 2:
                # Upper bound only spec
                self._plotIntervalUpperBound(thisInterval, kwargs)
                
            elif len(thisInterval) == 3:
                # lower & upper bound spec
                self._plotIntervalUpperLowerBound(thisInterval, kwargs)
                
            else:
                raise ValidationException('Wrong number of elements in interval tuple')
               
    
    def addInterval (self, interval):
        '''
        Add an interval to the mask specification.
        '''
        self._intervalSet.append(interval)
        
        self._validateIntervalSet()
        
    
    def _validateIntervalSet(self):
        # An intervalSet is a list of tuples
        # An interval is a tuple of size 2 or 3
        #   * A size 2 tuple implies a single upper bound is specified such that 
        #       signal <= upper bound => pass
        #   * A size 3 tuple implies an upper and lower bound is specified such that
        #       lower bound <= signal <= upper bound => pass
        # Intervals cannot overlap
        # Intervals must be piecewise continuous
        pass
    
    
    def _evaluateUpperBound (self, interval, signal):
        signalBaseline = signal[0]
        signalValues = signal[1]
            
        intervalBound = interval[0]
        baselineInterval = interval[1]
        
        baselineIndex = self._evaluateInterval(baselineInterval, signalBaseline)
            
        baselineBound = polynomial.polyval(signalBaseline[baselineIndex], intervalBound)
            
        return not any(signalValues[baselineIndex] > baselineBound)
    
    
    def _evaluateUpperLowerBound (self, interval, signal):
        signalBaseline = signal[0]
        signalValues = signal[1]
            
        upperIntervalBound = interval[0]
        lowerIntervalBound = interval[1]
        baselineInterval = interval[2]
    
        baselineIndex = self._evaluateInterval(baselineInterval, signalBaseline)
        
        upperBaselineBound = polynomial.polyval(signalBaseline[baselineIndex], upperIntervalBound)
        lowerBaselineBound = polynomial.polyval(signalBaseline[baselineIndex], lowerIntervalBound)
            
        return not (any(signalValues[baselineIndex] > upperBaselineBound) or any(signalValues[baselineIndex] < lowerBaselineBound))
    
    
    def _evaluateInterval (self, baselineInterval, signalBaseline):
        baselineIndex = numpy.array([])
        
        if len(baselineInterval) == 1:
            # The interval is open ended
            intervalLowerBound = float(baselineInterval[0])
            baselineIndex = signalBaseline >= intervalLowerBound
            
        elif len(baselineInterval) == 2:
            # The interval is finite
            intervalLowerBound = float(baselineInterval[0])
            intervalUpperBound = float(baselineInterval[1])
            
            baselineIndex = numpy.logical_and((signalBaseline >= intervalLowerBound), (signalBaseline < intervalUpperBound))
            
        else:
            raise ValidationException('Incorrect number of interval elements, ' + repr(len(baselineInterval)))
            
        return baselineIndex
    
    
    def _plotIntervalUpperBound (self, interval, kwargs):
        assert(len(interval) == 2)
        
        upperIntervalBoundCoefficients = interval[0]
        baselineInterval = interval[1]
        
        self._plotIntervalBound(baselineInterval, upperIntervalBoundCoefficients, kwargs)
    
    
    def _plotIntervalUpperLowerBound (self, interval, kwargs):
        # Assume the current figure is the correct one
        assert(len(interval) == 3)
        
        upperIntervalBoundCoefficients = interval[0]
        lowerIntervalBoundCoefficients = interval[1]
        baselineInterval = interval[2]
        
        self._plotIntervalBound(baselineInterval, upperIntervalBoundCoefficients, kwargs)
        self._plotIntervalBound(baselineInterval, lowerIntervalBoundCoefficients, kwargs)
        

    def _plotIntervalBound (self, baselineInterval, intervalBoundCoefficients, kwargs):
        assert((len(baselineInterval) == 1) or (len(baselineInterval) == 2))
        
        numberPoints = max([2, (2 * (2 * (len(intervalBoundCoefficients) - 1)))])
        
        xLimits = self._getPlotIntervalXlimits(baselineInterval)
        
        xData = numpy.linspace(xLimits[0], xLimits[1], numberPoints)
        yData = polynomial.polyval(xData, intervalBoundCoefficients)
        
        # Assume the current figure is the correct one
        if not kwargs:
            mpp.plot(xData, yData, 'b-')
        else:
            mpp.plot(xData, yData, **kwargs)
            
        
    def _getPlotIntervalXlimits (self, baselineInterval):
        assert((len(baselineInterval) == 1) or (len(baselineInterval) == 2))
        
        xData = []
        if len(baselineInterval) == 1:
            # Use the current axis limit for the upper x-axis plot bound
            currentAxis = mpp.gca()
            
            xData = [baselineInterval[0] ]
            figureXLimits = currentAxis.get_xlim()
            xData.append(figureXLimits[1])
            
        elif len(baselineInterval) == 2:
            xData = baselineInterval
            
        else:
            raise ValidationException('Wrong length of interval, ' + repr(len(baselineInterval)))
            
        return xData
    