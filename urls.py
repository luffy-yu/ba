from django.http import HttpResponse
from django.urls import include, path

from django.contrib import admin

admin.autodiscover()

from apps.core.views import (Index, SignUp, Logout, TermsOfService,
                             BanPage)
from apps.accounts.views import ProfileView, UserSettings


def favicon(request):
    f = open('static/favicon.ico', 'rb')
    x = f.read()
    f.close()
    return HttpResponse(x)


urlpatterns = [

    # Index views
    path('', Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('terms-of-service/', TermsOfService.as_view(), name='terms'),
    path('banned/', BanPage.as_view(), name='ban-page'),

    # Stuff to possibly move aside
    path('users/<username>/', ProfileView.as_view(), name='profile'),

    # Namespaces
    path('projects/', include(('apps.projects.urls', 'apps.projects'), namespace='projects')),
    path('accounts/', include(('apps.accounts.urls', 'apps.accounts'), namespace='accounts')),
    path('painters/', include(('apps.painters.urls', 'apps.painters'), namespace='painters')),

    # REST stuff
    path('api-auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework')),

    path('rest/', include(('apps.rest.urls', 'apps.rest'), namespace='api')),
    path('favicon.ico/', favicon),
    path('captcha/', include('captcha.urls')),
]
