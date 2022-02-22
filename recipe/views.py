import pandas as pd

from django.shortcuts import render
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe    
from django.contrib.auth.mixins import LoginRequiredMixin                            #to access Book model        
from django.contrib.auth.decorators import login_required

from .forms import RecipeSearchForm
from .utils import get_chart

# Create your views here.


def home(request):
   return render(request, 'recipe/recipes_home.html')


# Create your views here.
def recipes(request):

    form = RecipeSearchForm(request.POST or None)

    recipes_df = None
    chart = None

    qs = Recipe.objects.all()

    #check if the button is clicked
    if request.method =='POST':
        recipe_name = request.POST.get('recipe_name')
        chart_type = request.POST.get('chart_type')
        print (recipe_name, chart_type)

        qs = Recipe.objects.filter(name__icontains=recipe_name)

        if qs:
            recipes_df = pd.DataFrame(qs.values())
            # recipes_df['book_id'] = recipes_df['book_id'].apply(get_bookname_from_id)
            chart = get_chart(chart_type, recipes_df, labels=recipes_df['name'].values)
            recipes_df = recipes_df.to_html()

    context = {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart,
        'qs': qs,
    }
    return render(request, 'recipe/list.html', context)


@login_required
def records(request):
    #do nothing, simply display page
    form = SalesSearchForm(request.POST or None)
    sales_df = None
    chart = None

    qs = Sale.objects.all()

    #check if the button is clicked
    if request.method =='POST':
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')
        print (book_title, chart_type)

        qs = Sale.objects.filter(book__name__icontains=book_title)

        if qs:
            sales_df = pd.DataFrame(qs.values())
            sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)
            chart = get_chart(chart_type, sales_df, labels=sales_df['date_created'].values)
            sales_df = sales_df.to_html()

    context = {
        'form': form,
        'sales_df': sales_df,
        'chart': chart,
    }
    return render(request, 'sales/records.html', context)


class RecipeDetailView(LoginRequiredMixin, DetailView):                       #class-based view
   model = Recipe                                        #specify model
   template_name = 'recipe/detail.html'                 #specify template
