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
    def __init__(self, namekey='name'):
        self.namekey = namekey

    def set(self, name, value, **kwargs):
        self.append(Lict(value, **{self.namekey:name}, **kwargs))

    def metadict(self, i):
        return {k:v for k, v in self[i].filter(cmp=lambda a, b: a != b)}
