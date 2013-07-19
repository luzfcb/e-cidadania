# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 Clione Software
# Copyright (c) 2010-2013 Cidadania S. Coop. Galega
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

from django.conf.urls import *
from django.conf import settings

from apps.ecidadania.news.views import DeletePost, ViewPost, AddPost, EditPost
from apps.ecidadania.news.url_names import *


urlpatterns = patterns('apps.ecidadania.news.views',

    url(r'^add/$', AddPost.as_view(), name=POST_ADD),

    url(r'^(?P<post_id>\d+)/delete/$', DeletePost.as_view(),
        name=POST_DELETE),

    url(r'^(?P<post_id>\d+)/edit/$', EditPost.as_view(), name=POST_EDIT),

    url(r'^(?P<post_id>\d+)', ViewPost.as_view(), name=POST_VIEW),

)
