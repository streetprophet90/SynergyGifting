from django.shortcuts import render, redirect
from .models import Order
from wishlist.models import Item, Wishlist
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def place_order(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.giver = request.user
            order.item = item
            order.receiver = item.wishlist.user
            order.save()
            return redirect('wishlist')
    else:
        form = OrderForm()
    return render(request, 'orders/place_order.html', {'form': form, 'item': item})
