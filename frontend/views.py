from django.shortcuts import redirect, render
from .models import Curso,Usuario
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def indexpage(request):
    return render(request,'index.html')


def Clesson(request):
    cursos = Curso.objects.all()  # Obtén todos los cursos
    return render(request, 'cursos.html', {'cursos': cursos})



def agregar_curso(request):
    cursos = Curso.objects.all()  # Obtén todos los cursos
    return render (request, 'in_cursos.html',{'cursos':cursos})


def frmregister(request):
    
    if request.method == 'POST':
        nombre = request.POST['txtnombre']
        descripcion = request.POST['txtdescripcion']
        duracion = request.POST['txtduracion']
        precio_individual = request.POST['txtPIndividual']
        precio_grupal = request.POST['txtPGrupal']
        imagen = request.FILES['txtImagenCurso']  # Obtener la imagen del formulario

        curso = Curso(
            nombre=nombre,
            descripcion=descripcion,
            duracion=duracion,
            precio_individual=precio_individual,
            precio_grupal=precio_grupal,
            imagen=imagen  # Asignar la imagen al campo 'imagen' del modelo
        )

        curso.save()  # Guardar el curso en la base de datos
    return redirect('/agregar_curso/')

 
#aqui sera la vista para eliminar curso
def eliminarC(request,codigo):
    curso = Curso.objects.get(idcurso=codigo)
    curso.delete()
    return redirect('/agregar_curso/')

def modificar_curso(request, codigo):
    curso = Curso.objects.get(idcurso=codigo)
    return render(request, "editarcurso.html", {"curso": curso})

def guardar_modificacion(request, codigo):
    if request.method == 'POST':
        nombre = request.POST['txtnombre']
        descripcion = request.POST['txtdescripcion']
        duracion = request.POST['txtduracion']
        precio_individual = request.POST['txtPIndividual']
        precio_grupal = request.POST['txtPGrupal']
        
        curso = Curso.objects.get(idcurso=codigo)
        curso.nombre = nombre
        curso.descripcion = descripcion
        curso.duracion = duracion
        curso.precio_individual = precio_individual
        curso.precio_grupal = precio_grupal
        
        # Verificamos si se subió una nueva imagen
        if 'txtImagenCurso' in request.FILES:
            imagen = request.FILES['txtImagenCurso']
            curso.imagen = imagen
        
        curso.save()
        return redirect('/agregar_curso/')  
    


@login_required
def agregar_Usuario(request):
    usuario = Usuario.objects.all()  # Obtén todos los cursos
    return render (request, 'AUsuario.html',{'usuario':usuario})

def  FrmUsuario(request):
    if request.method=='POST':
        Unombre= request.POST['txtnombre']
        Udireccion = request.POST['txtdireccion']
        Ucorreo= request.POST['txtCorreo']
        UTelefono= request.POST['txtelefono']
        Upassword = request.POST['txtPassword']

        Datosusuario= Usuario(
            nombre = Unombre,#nombre
            telefono = UTelefono,#telefono
            correo= Ucorreo,#correo
            direccion=Udireccion,#direccion
            password=Upassword
        )
        Datosusuario.save()
        return redirect('/agregar_usuario/')
    

def tom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('LessCursos')  # Cambia esto al nombre de tu página principal
        else:
            # Si la autenticación falla, puedes manejarlo como quieras
            return render(request, 'login.html', {'error_message': 'Credenciales inválidas'})
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')


#manejo de errores

def error404(request, exception):
    return render(request, '404.html', status=404)
def error500(request):
    return render(request, '500.html', status=500)

  
  
    
       
    





