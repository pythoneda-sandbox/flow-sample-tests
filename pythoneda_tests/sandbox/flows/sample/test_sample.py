"""
pythoneda/sandbox/flows/sample/test_sample.py

This file defines tests for Sample Flow.

Copyright (C) 2023-today rydnr's https://github.com/pythoneda-sandbox/flow-sample-tests

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import pytest
from pythoneda import Flow
from pythoneda.sandbox.flows.sample import Sample


def test_create_flow():
    flow = Sample.event1(None)
    assert flow is not None


def test_wip():
    flow = Sample.event1(None)
    assert is_persisted(flow)


def is_persisted(flow: Flow) -> bool:
    """
    Checks whether given flow is persisted or not.
    :param flow: The flow.
    :type flow: pythoneda.Flow
    """
    return False
