# --------------------------------------------------------------------------
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 2 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

# -------------------------------------------------------------------------

'''
Created on March 30, 2016
@author: Andrew Abi-Mansour
'''

from PyGran import Simulator, Tools, Analyzer
import os

try:
	from PyGran import Visualizer
except:
	print("WARNING: Visualization not supported. Make sure wxwidgets and vtk libraries are properly installed on this system.")

from PyGran.Tools import run

__version__ = '1.0'
