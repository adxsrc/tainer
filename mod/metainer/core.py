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

from abc  import ABCMeta
from lict import Lict

class Metainer(metaclass=ABCMeta):
    """Metainer

    `Metainer` provides a metadata-based mixin for building
    interpolatable python classes.

    """
    __slots__ = ('_metainer')

    @property
    def metainer(self):
        try:
            m = super().__getattribute__('_metainer')
        except AttributeError:
            m = Lict()
            super().__setattr__('_metainer', m)
        return m

    def set(self, name, value, **kwargs):
        self.metainer.append(Lict(value, name=name, **kwargs))
        super().__setattr__(name, value)

    def __setattr__(self, name, value):
        self.set(name, value)

    def __getattr__(self, name):
        return super().__getattr__(name)
