
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include

import debug_toolbar


urlpatterns = [
    path('', RedirectView.as_view(url='/mytodo')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mytodo/', include('mytodo.urls')),
]
