from urllib import request
from django.shortcuts import render

from pizza.models import Pizza
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory

# Create your views here.
def home(request):
    data = Pizza.objects.all()
    return render(request, 'pizza/home.html', {'data': data})


def order(request):
    multiple_pizza = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            current_pizza = filled_form.save()
            pizza_id = current_pizza.id
            message = f"Thank for ordering your {filled_form.cleaned_data['size']}  {filled_form.cleaned_data['topping1']} and {filled_form.cleaned_data['topping2']} pizza is on it way!"
            filled_form = PizzaForm()
        else:
            pizza_id = None
            message = 'Your Pizza has not ordered!'
        return render(request, 'pizza/order.html', {'form': filled_form, 'message':message,
                            'pizza_id': pizza_id, 'multiple_pizza': multiple_pizza})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form, 'multiple_pizza': multiple_pizza})



def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                # topping1 = form.cleaned_data['topping1']
                # topping2 = form.cleaned_data['topping2']
                # size = form.cleaned_data['size']
                # pizza = Pizza(topping1=topping1, topping2=topping2, size=size)
                # pizza.save()
                form.cleaned_data
                form.save()
            note = 'Pizza ordered!'
        else:
            note = 'order was not submmited'
        return render(request, 'pizza/pizzas.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset': formset})



def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        fillerd_form = PizzaForm(request.POST, instance=pizza)
        if fillerd_form.is_valid():
            fillerd_form.save()
            form = fillerd_form
            note = 'Order has been edited'
            return render(request, 'pizza/edit_order.html', {'form': form, 'pizza': pizza, 'note': note})

    return render(request, 'pizza/edit_order.html', {'form': form, 'pizza': pizza})

