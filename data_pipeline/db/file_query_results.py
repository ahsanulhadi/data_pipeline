# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# 
###############################################################################
# Module:    file_query_results
# Purpose:   Represents the query result object returned from a file query
#
# Notes:
###############################################################################

import itertools

from .query_results import QueryResults
from data_pipeline.stream.file_reader import FileReader


def default_post_process_func(line):
    return line


class FileQueryResults(QueryResults):

    def __init__(self, filename, post_process_func):
        super(FileQueryResults, self).__init__()
        self._handle = FileReader(filename)

        if post_process_func is None:
            self._post_process_func = default_post_process_func
        else:
            self._post_process_func = post_process_func

    def __iter__(self):
        return self

    def next(self):
        line = self._handle.readline().strip('\n')
        if not line:
            self._handle.close()
            raise StopIteration
        return self._post_process_func(line)

    def fetchone(self):
        line = None
        try:
            line = self.next()
        except StopIteration, e:
            pass
        return line

    def fetchall(self):
        return [self._post_process_func(l.strip('\n'))
                for l in self._handle]

    def fetchmany(self, arraysize=None):
        if arraysize > 0:
            return [self._post_process_func(l.strip('\n'))
                    for l in itertools.islice(self._handle, arraysize)]
        return self.fetchall()

    def __del__(self):
        self._handle.close()
