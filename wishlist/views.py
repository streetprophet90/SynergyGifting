
from django.shortcuts import render, redirect
from .models import Wishlist, Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    items = wishlist.items.all()
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist, 'items': items})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            request.user.wishlist.items.add(item)
            return redirect('wishlist')
    else:
        form = ItemForm()
    return render(request, 'wishlist/add_item.html', {'form': form})
