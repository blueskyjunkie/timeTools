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

import math
import matplotlib.pyplot as mpp
import numpy

import timeTools.pdv.analysis.general as pag
import timeTools.pdv.exceptions as pex


def decimatePdvToPlotResolution (xData, yData, plotResolution, plotWidth):
    assert(len(xData) == len(yData))
    
    originalNumberSamples = len(yData)
    
    dataResolution = originalNumberSamples / plotWidth
    decimationFactor = math.floor(dataResolution / plotResolution)
    
    if decimationFactor != 0:
        # In the case of PDV we are mostly interested in the minima and maxima
        # so preserve those features in decimation block.
        numberWindows = math.floor(originalNumberSamples / decimationFactor)
        numberFeatures = 2 * numberWindows
        
        inputData = (xData, yData)
        decimatedData = (numpy.zeros(numberFeatures), numpy.zeros(numberFeatures))
        
        for k in numpy.arange(0, numberWindows):
            for m in range(0, 2):
                windowOffset = decimationFactor * k
                windowIndices = numpy.arange(windowOffset, (windowOffset + decimationFactor))
                
                decimatedData[m][2 * k] = numpy.min(inputData[m][windowIndices])
                decimatedData[m][(2 * k) + 1] = numpy.max(inputData[m][windowIndices])
                
        return decimatedData
    else:
        # The data resolution is lower than the plot resolution so decimation is unnecessary
        return xData, yData


def plotMinimumThresholdOnPdv (referenceTimeSeconds, inputPdv, timeStepSeconds, windowDurationSeconds, yUnit = '', figureInstance = None):
    plotResolutionDpi = 300
    plotWidthInches = 8
    
    figureNumber = []
    figureHandle = None
    if figureInstance != None:
        figureHandle = mpp.figure(figureInstance)
        figureNumber = figureInstance
    else:
        figureHandle = mpp.figure(figsize = (plotWidthInches, 5), dpi = plotResolutionDpi)
        figureNumber = figureHandle.number
    
    windowSize = math.floor(windowDurationSeconds / timeStepSeconds)
    thresholdDelay, offsetValues = pag.calculateMinimumThresholdPacketDelay(inputPdv, windowSize)
    
    decimatedReferenceTime, decimatedPdv = decimatePdvToPlotResolution(referenceTimeSeconds, inputPdv, plotResolutionDpi, plotWidthInches)
    decimatedOffsetTime, decimatedThresholdDelay = decimatePdvToPlotResolution(referenceTimeSeconds[offsetValues + windowSize - 1], thresholdDelay, plotResolutionDpi, plotWidthInches)
    
    mpp.plot(decimatedReferenceTime, decimatedPdv)
    mpp.plot(decimatedOffsetTime, decimatedThresholdDelay)
    
    xLabel = 'Reference Time (sec)'
    mpp.xlabel(xLabel)
    
    yLabel = 'Delay (' + yUnit + ')'
    mpp.ylabel(yLabel)
    
    ax = figureHandle.gca()
    ax.grid()
    
    return figureNumber
