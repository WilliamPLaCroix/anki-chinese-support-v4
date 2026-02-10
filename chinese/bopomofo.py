# Copyright © 2012 Thomas TEMPÉ <thomas.tempe@alysse.org>
# Copyright © 2014 Alex Griffin <alex@alexjgriffin.com>
# Copyright © 2017-2019 Joseph Lorimer <joseph@lorimer.me>
# Copyright © 2023-2024 Gustaf Carefall <https://github.com/Gustaf-C>
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


from .consts import bopomofo_replacements
from .util import cleanup


def bopomofo(pinyin):
    from .transcribe import replace_tone_marks

    assert isinstance(pinyin, list)
    result = []
    for word in replace_tone_marks(pinyin):
        s = cleanup(word).lower()
        for (a, b) in bopomofo_replacements:
            s = s.replace(a, b)
        result.append(s)
    return result
