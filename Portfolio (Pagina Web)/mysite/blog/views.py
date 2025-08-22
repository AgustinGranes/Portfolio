from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
from django.utils import timezone
import json
from .models import Post, Contact, Comment

def portfolio_view(request):
    """Vista principal del portfolio"""
    # Obtener todos los posts para mostrar en el blog
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/portfolio.html', {'posts': posts})

def home(request):
    """Alias para portfolio_view para compatibilidad"""
    return portfolio_view(request)

@csrf_exempt
@require_http_methods(["POST"])
def contact_form(request):
    """Maneja el formulario de contacto"""
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            message = data.get('message', '').strip()
        else:
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            message = request.POST.get('message', '').strip()

        # Validaciones
        if not name or not email or not message:
            return JsonResponse({'success': False, 'error': 'Todos los campos son obligatorios'})
        
        if len(name) > 100:
            return JsonResponse({'success': False, 'error': 'El nombre es demasiado largo'})
        
        if len(message) > 1000:
            return JsonResponse({'success': False, 'error': 'El mensaje es demasiado largo'})

        # Crear el contacto
        contact = Contact.objects.create(
            name=name, 
            email=email, 
            message=message
        )
        
        return JsonResponse({
            'success': True, 
            'message': '¡Mensaje enviado correctamente! Te contactaré pronto.'
        })

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Datos inválidos'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': 'Error interno del servidor'})

def get_comments(request, post_id):
    """Obtiene los comentarios de un post"""
    try:
        post = get_object_or_404(Post, pk=post_id)
        comments = Comment.objects.filter(post=post).order_by('-created_date')
        
        comments_data = [
            {
                'username': c.username,
                'content': c.content,
                'created_date': c.created_date.strftime('%d/%m/%Y %H:%M')
            } for c in comments
        ]
        
        return JsonResponse({'success': True, 'comments': comments_data})
    
    except Exception as e:
        return JsonResponse({'success': False, 'error': 'Error al obtener comentarios'})

@csrf_exempt
@require_POST
def add_comment(request, post_id):
    """Añade un comentario a un post"""
    try:
        data = json.loads(request.body)
        username = data.get('username', '').strip()
        content = data.get('content', '').strip()
        
        # Validaciones
        if not username or not content:
            return JsonResponse({'success': False, 'error': 'Por favor completa todos los campos'})
        
        if len(username) > 100:
            return JsonResponse({'success': False, 'error': 'El nombre es demasiado largo'})
        
        if len(content) > 1000:
            return JsonResponse({'success': False, 'error': 'El comentario es demasiado largo'})
        
        # Obtener el post y crear el comentario
        post = get_object_or_404(Post, pk=post_id)
        Comment.objects.create(
            post=post, 
            username=username, 
            content=content, 
            created_date=timezone.now()
        )
        
        return JsonResponse({'success': True})
    
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Datos inválidos'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': 'Error al enviar comentario'})