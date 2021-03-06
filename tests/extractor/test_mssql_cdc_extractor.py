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
import pytest
from pytest_mock import mocker
from data_pipeline.extractor.mssql_cdc_extractor import MssqlCdcExtractor
from data_pipeline.extractor.exceptions import InvalidArgumentsError
from data_pipeline.db.connection_details import ConnectionDetails


@pytest.fixture()
def extractor_mockdb(mocker):
    # Return an empty list of results as we're not checking results
    config = {'execute_query.return_value': []}
    mockdb = mocker.Mock(**config)
    return (MssqlCdcExtractor(mockdb), mockdb)


@pytest.mark.skip(reason="Not implemented")
def test_poll_cdcs_specific_segowners_and_tables(mocker, extractor_mockdb):
    (extractor, mockdb) = extractor_mockdb
    extractor.poll_cdcs(1, 2, ['segA', 'segB'], ['tableA', 'tableB'])
    expected_query = "AN SQL STRING"
    mockdb.assert_has_calls([
        mocker.call.execute_query(expected_query)
    ])


@pytest.mark.skip(reason="Not implemented")
def test_poll_cdcs_specific_segowners_and_all_tables(mocker, extractor_mockdb):
    (extractor, mockdb) = extractor_mockdb
    extractor.poll_cdcs(1, 2, ['segA', 'segB'], [])
    expected_query = "AN SQL STRING"
    mockdb.assert_has_calls([
        mocker.call.execute_query(expected_query)
    ])


@pytest.mark.skip(reason="Not implemented")
def test_poll_cdcs_all_segowners_and_specific_tables(mocker, extractor_mockdb):
    (extractor, mockdb) = extractor_mockdb
    extractor.poll_cdcs(1, 2, [], ['tableA', 'tableB'])
    expected_query = "AN SQL STRING"
    mockdb.assert_has_calls([
        mocker.call.execute_query(expected_query)
    ])


@pytest.mark.skip(reason="Not implemented")
def test_poll_cdcs_all_segowners_and_tables(mocker, extractor_mockdb):
    (extractor, mockdb) = extractor_mockdb
    extractor.poll_cdcs(1, 2, [], [])
    expected_query = "AN SQL STRING"
    mockdb.assert_has_calls([
        mocker.call.execute_query(expected_query)
    ])


@pytest.mark.skip(reason="Not implemented")
def test_poll_cdcs_valid_start_end_scn(mocker, extractor_mockdb):
    (extractor, mockdb) = extractor_mockdb
    extractor.poll_cdcs(1, 2, [], [])
    mockdb.assert_has_calls([
        mocker.call.execute_query(mocker.ANY)
    ])


@pytest.mark.skip(reason="Not implemented")
def test_poll_cdcs_start_gt_end_scn(mocker, extractor_mockdb):
    (extractor, mockdb) = extractor_mockdb
    with pytest.raises(InvalidArgumentsError):
        extractor.poll_cdcs(2, 1, [], [])


@pytest.mark.skip(reason="Not implemented")
def test_connect_data_source(mocker, extractor_mockdb):
    (extractor, mockdb) = extractor_mockdb
    conn_details = ConnectionDetails(userid='user', password='pass',
                                     host='db', port=1234, dbsid='orcl')
    extractor.connect_data_source(conn_details)
    mockdb.connect.assert_called_once_with(conn_details)
