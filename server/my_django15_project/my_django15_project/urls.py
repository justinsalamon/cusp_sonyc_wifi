from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_django15_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#     url(r'^books/(?P<title>\w+)/$', 'books.views.index'),
    url(r'^books/$', 'books.views.index'),
]
