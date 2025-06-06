# coding=utf-8
# Copyright 2025 The Google Research Authors.
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

# coding=utf-8
# Copyright 2022 The Google Research Authors.
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
"""Install graph_sampler."""

from setuptools import setup

setup(
    name='graph_sampler',
    version='0.0',
    description='For sampling graphs or molecules.',
    author='Google LLC',
    author_email='noreply@google.com',
    url='https://github.com/google-research/google-research/tree/master/graph_sampler',
    packages=['graph_sampler'],
    install_requires=[
        'absl-py',
        'igraph',
        'numpy',
        'pandas',
        'pytest',
        'rdkit-pypi',
        'runstats',
    ],
    python_requires='>=3.6',
)
