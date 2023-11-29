from django.shortcuts import render, reverse
from .models import Bolo, Item
from .forms import BoloForm, ItemForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DatailView, CreateView, UpdateView, DeleteView
# Create your views here.


# def home(request):
#    return render(request, 'home.html')

class HomeTemplateView(TemplateView):
    template_name='home.html'

class BoloListView(ListView): 
    model=Bolo
    template_name="bolo/listar.html"
    context_object_name="bolos"
    ordering='-nome'
    paginate_by = 5
    
class BoloDatailView(DatailView):
    model=Bolo
    template_name="bolo/detalhar.html"
    context_object_name="bolo"
    pk_url_kwarg="id"

class BoloCreateView(CreateView):
    model=Bolo
    template_name="bolo/cadastrar.html"
    form_class=BoloForm

    def get_success_url(self):
        messages.add_message(self.request,messages.SUCCESS," Bolo Maravilhoso cadastrado com sucesso!")
        return reverse(listar-bolo)
    
class BoloUpdateView(UpdateView):
    model=Bolo
    template_name="bolo/atualizar.html"
    form_class=BoloForm  
    pk_url_kwarg="id"


    def get_success_url(self):
        messages.add_message(self.request,messages.SUCCESS," Bolo Maravilhoso atualizado com sucesso!")
        return reverse(listar-bolo)  
    
class BoloDeleteView(DeleteView):
    model=Bolo
    template_name="bolo/bolo_confirm_delete.html"
    pk_url_kwarg="id"


    def get_success_url(self):
        messages.add_message(self.request,messages.SUCCESS," Bolo Maravilhoso deletado com sucesso!")
        return reverse(listar-bolo)  
    
class ItemListView(ListView): 
    model=Item
    template_name="item/listar.html"
    context_object_name="itens"
    ordering='-recheio'
    paginate_by = 5

class ItemDatailView(DatailView):
    model=Item
    template_name="item/detalhar.html"
    context_object_name="item"
    pk_url_kwarg="id"

class ItemCreateView(CreateView):
    model=Item
    template_name="item/cadastrar.html"
    form_class=ItemForm

    def get_success_url(self):
        messages.add_message(self.request,messages.SUCCESS," Item Maravilhoso cadastrado com sucesso!")
        return reverse(listar-item)
    
class ItemUpdateView(UpdateView):
    model=Item
    template_name="item/atualizar.html"
    form_class=ItemForm  
    pk_url_kwarg="id"


    def get_success_url(self):
        messages.add_message(self.request,messages.SUCCESS," Item Maravilhoso atualizado com sucesso!")
        return reverse(listar-item)  
    
class ItemDeleteView(DeleteView):
    model=Item
    template_name="item/item_confirm_delete.html"
    pk_url_kwarg="id"


    def get_success_url(self):
        messages.add_message(self.request,messages.SUCCESS," Item Maravilhoso deletado com sucesso!")
        return reverse(listar-Item)  