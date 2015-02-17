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


# Holdover transient response, Section 8.1, Rec. ITU-T G.8263/Y.1363 (02/2012), pp7
a1 = 1.0
a2 = 10.0
b = 1.16e-5
c = 150
d = 1.16e-5

transientResponsePhaseErrorNs = numpy.array([c, (a1 + a2), 0.5 * b])
transientResponseFfoPpb = numpy.array([(a1 + a2), b])
transientResponseFfoRatePpbPerSecond = numpy.array([d])
