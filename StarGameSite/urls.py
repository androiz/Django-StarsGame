from django.conf.urls import patterns, include, url
from django.contrib import admin
from StarGameApp.views import LoginView

urlpatterns = patterns('',
    # Login/Logout:
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', 'StarGameApp.views.user_logout', name='logout'),

    #Juego
    url(r'^principal/', 'StarGameApp.views.principalView', name='principal'),
    url(r'^edificios/', 'StarGameApp.views.edificiosView', name='edificios'),
    url(r'^unidades/', 'StarGameApp.views.unidadesView', name='unidades'),
    url(r'^tecnologias/', 'StarGameApp.views.tecnologiasView', name='tecnologias'),
    url(r'^datosCuenta/', 'StarGameApp.views.datosCuentaView', name='datosCuenta'),

    #Admin
    url(r'^admin/', include(admin.site.urls)),
)
