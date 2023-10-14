from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


handler404 = 'frontend.views.error404'
handler500 = 'frontend.views.error500'

urlpatterns = [
   
    path('error-404/', TemplateView.as_view(template_name='404.html'), name='error_404'),
    #url de mi pagina home
    path('', views.indexpage, name='index'),
    #url de listar cursos pagina para mostrar los cursos
    path('MCursos/', views.Clesson, name='LessCursos'),

    path('agregar_curso/', views.agregar_curso, name='agregar_curso'), 
    # esta url es para el formulario de registrar curso y listarlos
    path('frmregister/',views.frmregister,name="registro"),
    #este url es para eliminar cursos 
    path('agregar_curso/eliminarc/<codigo>', views.eliminarC),
    # esteurl es para editar los cursos
    path('agregar_curso/modificar_curso/<codigo>', views.modificar_curso),
    #esto es para guardar la modificacion del curso
    path('agregar_curso/editarc/guardarmodifi/<codigo>/', views.guardar_modificacion, name='guardar_modificacion'),
    #esto es para agregar usuario
    path('agregar_usuario/',views.agregar_Usuario,name='agregarUsuario'),
    #esto es la funcion del formulario
    path('frmUsuario/',views.FrmUsuario,name="frmUsuario"),
    #eror 404

    path('login/', views.tom_login, name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
        
]

