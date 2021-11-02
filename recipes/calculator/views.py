from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def home_view(request):
    return HttpResponse('Домашняя страница сервиса-помощника для приготовления блюд<br><br>'
                        'Cписок доступных блюд:<br>'
                        'Омлет: omlet/<br>'
                        'Паста: pasta/<br>'
                        'Бутер: buter/')


def recipe_view(request, dish):
    template_name = 'calculator/index.html'

    recipe = DATA.get(dish)
    if recipe is None:
        return HttpResponse('Такого рецепта не знаю :(')

    option_param = request.GET.get('servings', '1')

    if option_param.isdigit():
        copy_dict = recipe.copy()
        for ingredient in copy_dict:
            copy_dict[ingredient] = copy_dict[ingredient] * int(option_param)
        context = {
            'recipe': copy_dict
        }
    else:
        return HttpResponse(f'{option_param} - не целое число!')

    return render(request, template_name, context)
