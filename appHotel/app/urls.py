from django.urls import path
from .views import cliente_views, tipoAcomodacao_views, acomodacao_views, diarias_view


urlpatterns = [
    path('cliente/cadastrar', cliente_views.cadastrar_cliente,
         name='cadastrar_cliente'),
    path('cliente/listar', cliente_views.listar_clientes, name='listar_clientes'),
    path('cliente/editar/<int:id>',
         cliente_views.editar_cliente, name='editar_cliente'),
    path('tipos/cadastrar', tipoAcomodacao_views.cadastrar_tiposAcomodacao,
         name='cadastrar_tipos'),
    path('tipos/listar', tipoAcomodacao_views.listar_tiposAcomodacao,
         name='listar_tipos'),
    path('tipo/editar/<int:id>',
         tipoAcomodacao_views.editar_tiposAcomodacao, name='editar_tipos'),
    path('acomodacao/cadastrar', acomodacao_views.cadastrar_acomodacoes,
         name='cadastrar_acomodacao'),
    path('acomodacao/listar', acomodacao_views.listar_acomodacoes,
         name='listar_acomodacao'),
    path('acomodacao/editar/<int:id>',
         acomodacao_views.editar_acomodacao, name='editar_acomodacao'),
    path('diarias/cadastrar', diarias_view.cadastrar_diarias,
         name='cadastrar_diarias'),
    path('diarias/listar', diarias_view.listar_diarias, name='listar_diarias'),
    path('diarias/editar/<int:id>',
         diarias_view.editar_diarias, name='editar_diarias'),
]
