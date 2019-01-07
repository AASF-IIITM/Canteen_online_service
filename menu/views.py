from django.http import HttpResponse
from django.views import generic
from .models import Menu, Sabzi, Thali, Desserts, Beverages, Breads, Snacks, StreetFood, Rice


class DetailView(generic.ListView):
    model = Menu
    template_name = 'menu/detail.html'
    context_object_name = 'all_menu'

    def get_queryset(self):
        return Menu.objects.all()


class IndexView(generic.ListView):
    template_name = 'menu/index.html'

    def get_queryset(self):
        return HttpResponse("Welcome Smith")


class SabziView(generic.ListView):
    template_name = 'menu/Sabzi.html'
    model = Sabzi
    context_object_name = 'all_sabzi'

    def get_queryset(self):
        return Sabzi.objects.all()


class ThaliView(generic.ListView):
    template_name = 'menu/thali.html'
    model = Thali
    context_object_name = 'all_thali'

    def get_queryset(self):
        return Thali.objects.all()


class BreadsView(generic.ListView):
    template_name = 'menu/Breads.html'
    model = Breads
    context_object_name = 'all_breads'

    def get_queryset(self):
        return Breads.objects.all()


class BeveragesView(generic.ListView):
    template_name = 'menu/Beverages.html'
    model = Beverages
    context_object_name = 'all_beverages'

    def get_queryset(self):
        return Beverages.objects.all()


class SnacksView(generic.ListView):
    template_name = 'menu/Snacks.html'
    model = Snacks
    context_object_name = 'all_snacks'

    def get_queryset(self):
        return Snacks.objects.all()


class StreetFoodView(generic.ListView):
    template_name = 'menu/Street Food.html'
    model = StreetFood
    context_object_name = 'all_streetfood'

    def get_queryset(self):
        return StreetFood.objects.all()


class DessertsView(generic.ListView):
    template_name = 'menu/Desserts.html'
    model = Desserts
    context_object_name = 'all_desserts'

    def get_queryset(self):
        return Desserts.objects.all()


class RiceView(generic.ListView):
    template_name = 'menu/Rice.html'
    model = Rice
    context_object_name = 'all_rice'

    def get_queryset(self):
        return Rice.objects.all()











