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

from lict           import Lict
from metainer.mixin import MetainerMixin

import pytest

class Datainer(MetainerMixin):
    pass

d1 = Lict(0.1, __name__='d1')
d2 = Lict(0.2, __name__='d2')
d3 = Lict(0.3, __name__='d3')
d  = Datainer()

def test_mount():
    global d
    d.mounts = ['name', 'kind']
    d.set('x', d1)
    d.set('y', d2, kind='meta')
    d.set('z', d3, kind='data', hidden=True)

    assert vars(d) == {
        'mounts': ['name', 'kind'],
        'x': d1,
        'y': d2,
        'meta': d2,
        'data': d3,
    }

    assert d.x == d1
    assert d.y == d2

    with pytest.raises(AttributeError) as e:
        d.z
    assert str(e.value) == "'Datainer' object has no attribute 'z'"

    assert d.meta == d2
    assert d.data == d3
