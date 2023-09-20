from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import *


class OrderList(ListView):
    model = Order
    template_name = 'orders/orders.html'
    context_object_name = 'orders'
    extra_context = {'title': 'Таблица заявок'}


class ShowOrder(DetailView):
    model = Order
    template_name = 'orders/order_info.html'
    pk_url_kwarg = 'order_id'
    context_object_name = 'order'


class CreateOrder(CreateView):
    form_class = OrderForm
    template_name = 'orders/create_order.html'
    extra_context = {'title': 'Создание Заявки'}
    success_url = reverse_lazy('orders')

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['client_name']
            client_phone = form.cleaned_data['client_phone']
            client = Client.objects.filter(client_phone=client_phone).first()
            client = client or Client.objects.create(client_name=client_name, client_phone=client_phone)
            device_group = form.cleaned_data['device_group']
            device_brand = form.cleaned_data['device_brand']
            device_model = form.cleaned_data['device_model']
            device_serial = form.cleaned_data['device_serial']
            device = Device.objects.create(group=device_group, brand=device_brand, model=device_model, serial_number=device_serial)
            order_description = form.cleaned_data['order_description']
            price = form.cleaned_data['price']
            order = Order.objects.create(client=client, device=device, order_description=order_description, order_status='open', price=price)
            return HttpResponseRedirect('/orders/')
    else:
        form = OrderForm
    return render(request, 'orders/create_order.html', {'form': form})


class OrderUpdate(UpdateView):
    model = Order
    template_name = 'orders/order_info.html'
    extra_context = {'title': 'Просмотр и редактирование заказа'}
    fields = ['client', 'device', 'order_description', 'order_status', 'price', 'services']
    success_url = reverse_lazy('orders')