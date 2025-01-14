# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Generalize rule snapshot testing """
from gcpdiag import config
from gcpdiag.runbook import gce, snapshot_test_base


class Test(snapshot_test_base.RulesSnapshotTestBase):
  rule_pkg = gce
  project_id = 'gcpdiag-gce-faultyssh-runbook'
  config.init({'auto': True}, project_id)

  rule_parameters = [{
      'name': 'faulty-linux-ssh',
      'zone': 'europe-west2-a',
      'principal': 'cannotssh@example.com',
      'tunnel_through_iap': 'True',
      'os_login': 'True'
  }, {
      'name':
          'valid-linux-ssh',
      'zone':
          'europe-west2-a',
      'principal':
          'canssh@gcpdiag-gce-faultyssh-runbook.iam.gserviceaccount.com',
      'tunnel_through_iap':
          'True',
      'os_login':
          'True'
  }, {
      'name': 'faulty-windows-ssh',
      'zone': 'europe-west2-a',
      'principal': 'cannot@example.com',
      'tunnel_through_iap': 'False',
      'os_login': 'False',
      'local_user': 'no_user'
  }]
