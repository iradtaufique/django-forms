from cProfile import label
from dataclasses import fields
from pyexpat import model
from random import choices
from django import forms

from pizza.models import Pizza, Size


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping1', max_length=100)
#     topping2 = forms.CharField(label='Topping2', max_length=100)
    # size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
    # toppings = forms.MultipleChoiceField(label='select toppings', choices=[('4sea', '4 Season'), ('chkne', 'Chicken Pizza'), ('Bf', 'Beaf Pizza')],
    #  widget=forms.CheckboxSelectMultiple)


"""using django model forms"""
class PizzaForm(forms.ModelForm):
    """customizing size with widgets"""
    # size =forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
    """allow image upload"""
    # image = forms.ImageField()
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}