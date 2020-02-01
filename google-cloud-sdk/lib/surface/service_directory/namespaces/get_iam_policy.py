# -*- coding: utf-8 -*- #
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""`gcloud service-directory namespaces get-iam-policy` command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.service_directory import namespaces
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.service_directory import resource_args

_RESOURCE_TYPE = 'namespace'


@base.Hidden
class GetIamPolicy(base.ListCommand):
  """Get IAM policy for a namespace."""

  @staticmethod
  def Args(parser):
    resource_args.AddNamespaceResourceArg(
        parser,
        """for which to get IAM policy.""")
    base.URI_FLAG.RemoveFromParser(parser)

  def Run(self, args):
    client = namespaces.NamespacesClient()
    namespace_ref = args.CONCEPTS.namespace.Parse()

    return client.GetIamPolicy(namespace_ref)
