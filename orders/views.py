from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from wishlist.models import Item, Wishlist
from .forms import OrderForm

@login_required
def place_order(request, item_id, slug=None):
    item = Item.objects.get(id=item_id)
    wishlist = Wishlist.objects.filter(items=item).first()
    if not wishlist:
        return redirect('wishlist')  # Redirect to wishlist if no such wishlist exists
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.giver = request.user
            order.item = item
            order.receiver = wishlist.user
            order.save()
            return redirect('order_confirmation')
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form, 'item': item, 'slug': slug})

@login_required
def order_confirmation(request):
    return render(request, 'order_confirmation.html')
