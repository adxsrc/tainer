# Copyright 2017 Chi-kwan Chan
# Copyright 2017 Harvard-Smithsonian Center for Astrophysics
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from metainer import *

class Datainer(Metainer):
    pass

d1 = Lict(0.1, __name__='d1')
d2 = Lict(0.2, __name__='d2')
d3 = Lict(0.3, __name__='d3')

def test_set():
    d = Datainer()
    d.set('x', d1, kind='coord')
    d.set('y', d2, kind='coord')
    d.set('z', d3, kind='coord')
    assert d._metainer == [
        [d1, ('name', 'x'), ('kind', 'coord')],
        [d2, ('name', 'y'), ('kind', 'coord')],
        [d3, ('name', 'z'), ('kind', 'coord')],
    ]

def test_setattr():
    d = Datainer()
    d.x = d1
    d.y = d2
    d.z = d3
    assert d._metainer == [
        [d1, ('name', 'x')],
        [d2, ('name', 'y')],
        [d3, ('name', 'z')],
    ]
