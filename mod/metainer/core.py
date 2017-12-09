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

from lict import Lict

class Metainer(Lict):
    """Metainer

    `Metainer` is a metadatabase based on `Lict`.

    """
    def __init__(self, namekey='name', mountkey='mounts', hiddenkey='hidden'):
        self.namekey   = namekey
        self.mountkey  = mountkey
        self.hiddenkey = hiddenkey

    def set(self, name, value, **kwargs):
        self.append(Lict(value, **{self.namekey:name}, **kwargs))

    def mount(self, i, setback):
        # Special keys that metainer uses

        value = self[i].get()[0]
        pairs = {k:v for k, v in self[i].filter(cmp=lambda a, b: a != b)}

        # Cache value to `__dict__` according to their metadata
        keys = [self.namekey]
        for row in self:
            if self.mountkey in row.get(self.namekey):
                keys = row[0]

        for k in keys:
            if k in pairs:
                if not k == self.namekey or not pairs.get(self.hiddenkey, False):
                    setback(pairs[k], value)
