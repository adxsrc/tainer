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

from lict     import Lict
from metainer import Metainer

d1 = Lict(0.1, __name__='d1')
d2 = Lict(0.2, __name__='d2')
d3 = Lict(0.3, __name__='d3')

def test_mount():
    m  = Metainer()
    m.set('mounts', ['name', 'kind'])
    m.set('x', d1)
    m.set('y', d2, kind='meta')
    m.set('z', d3, kind='data', hidden=True)

    g = m.group('name')
    assert g.get('mounts')[0][0] == ['name', 'kind']
    assert g.get('x')[0][0]      == d1
    assert g.get('y')[0][0]      == d2
    assert g.get('z')[0][0]      == d3
