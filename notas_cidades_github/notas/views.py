from django.db.models import Avg, Max, Min
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Nota

def home(request):
    notas = Nota.objects.all()

    busca = request.GET.get("busca", "").strip()
    cidade = request.GET.get("cidade", "").strip()
    curso = request.GET.get("curso", "").strip()
    ordem = request.GET.get("ordem", "nota_desc")

    if busca:
        from django.db.models import Q
        notas = notas.filter(
            Q(nome__icontains=busca) |
            Q(cidade__icontains=busca) |
            Q(curso__icontains=busca)
        )

    if cidade:
        notas = notas.filter(cidade=cidade)

    if curso:
        notas = notas.filter(curso=curso)

    if ordem == "nota_asc":
        notas = notas.order_by("nota", "nome")
    elif ordem == "nome":
        notas = notas.order_by("nome")
    else:
        notas = notas.order_by("-nota", "nome")

    cidades = Nota.objects.values_list("cidade", flat=True).distinct().order_by("cidade")
    cursos = Nota.objects.values_list("curso", flat=True).exclude(curso="").distinct().order_by("curso")

    stats = notas.aggregate(
        media=Avg("nota"),
        maior=Max("nota"),
        menor=Min("nota"),
    )

    top = list(
        notas.order_by("-nota")[:10].values("nome", "nota", "cidade")
    )

    paginator = Paginator(notas, 20)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "page_obj": page_obj,
        "cidades": cidades,
        "cursos": cursos,
        "busca": busca,
        "cidade_selecionada": cidade,
        "curso_selecionado": curso,
        "ordem": ordem,
        "stats": stats,
        "top": top,
    }
    return render(request, "notas/home.html", context)
