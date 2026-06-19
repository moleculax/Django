# djblog/apps/categories/views.py

from multiprocessing import context

from django.http import JsonResponse
from django.shortcuts import render

from .models import Category

def categories(request, category_id=None):
    if category_id is None:
        # Traer todas las categorías
        categories = list(Category.objects.all().values(
            "id", "title", "slug", "published", "created", "updated"
        ))
        # return JsonResponse({
        #             "mensaje": "Listado de categorías",
        #             "estado": "exito",
        #             "data": categories
        #         })
        context = {
            "mensaje": "Listado de categorías",
            "estado": "exito",
            "data": categories
        }
    else:
        # Traer una sola categoría por id
        category = Category.objects.filter(pk=category_id).values(
                    "id",
                        "title",
                        "slug",
                        "published",
                        "created",
                        "updated"
                ).first()

        if category:
            # return JsonResponse({
            #     "mensaje": f"Categoría encontrada con id {category_id}",
            #     "estado": "exito",
            #     "data": category
            # })
            context =  {
                    "mensaje": f"Categoría encontrada con id {category_id}",
                    "estado": "exito",
                    "data": category
                }
        else:
            # return JsonResponse({
            #     "mensaje": f"Sin datos para el id {category_id}",
            #     "estado": "false",
            #     "data": None
            # })
            context =  {
                "mensaje": f"Sin datos para el id {category_id}",
                "estado": "false",
                "data": None
            }

    # ESTO HABILITA Y MUESTRA RESULTADO EN HTML
    return render(request, 'categories.html', context)
    # ESTO MUESTRA RESULTADO EN JSON PARA USAR EN FROND POR EJEMPLO REACT, NEXTJS, ETC
    # return JsonResponse(context)
