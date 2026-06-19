from django.http import JsonResponse
from .models import Category

def categories(request, category_id=None):
    if category_id is None:
        # Traer todas las categorías
        categories = list(Category.objects.all().values(
            "id", "title", "slug", "published", "created", "updated"
        ))
        return JsonResponse({
            "mensaje": "Listado de categorías",
            "estado": "exito",
            "data": categories
        })
    else:
        # Traer una sola categoría por id
        category = Category.objects.filter(pk=category_id).values(
            "id", "title", "slug", "published", "created", "updated"
        ).first()

        if category:
            return JsonResponse({
                "mensaje": f"Categoría encontrada con id {category_id}",
                "estado": "exito",
                "data": category
            })
        else:
            return JsonResponse({
                "mensaje": f"Sin datos para el id {category_id}",
                "estado": "false",
                "data": None
            })
