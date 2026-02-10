# Copyright © 2012-2015 Thomas TEMPÉ <thomas.tempe@alysse.org>
# Copyright © 2012 Roland Sieker <ospalh@gmail.com>
# Copyright © 2013 Chris Hatch <foonugget@gmail.com>
# Copyright © 2014 Alex Griffin <alex@alexjgriffin.com>
# Copyright © 2017-2021 Joseph Lorimer <joseph@lorimer.me>
# Copyright © 2020 Joe Minicucci <https://joeminicucci.com>
# Copyright © 2023-2024 Gustaf Carefall <https://github.com/Gustaf-C>
# Copyright © 2023-2025 Kieran Black <https://github.com/kieranlblack>
# Copyright © 2025 fetsorn <https://github.com/fetsorn>
# Copyright © 2025 Shigeyuki <http://patreon.com/Shigeyuki>
#
# other contributors, see: https://github.com/Gustaf-C/anki-chinese-support-3/graphs/contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
from os.path import dirname, join

sys.path.append(join(dirname(__file__), 'lib'))

from . import main

main.load()

from ._shige_patch import set_shige_patch
set_shige_patch()
