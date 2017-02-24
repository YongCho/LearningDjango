from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

# Import this so you can use the items.
from inventory.models import Item


# Create your views here.
def index(request):
    # return HttpResponse('<p>In index view</p>')

    items = Item.objects.exclude(amount=0)
    # Rendering from a template page. This template page is expecting some variables to be filled.
    # We pass the variables in a dictionary of variable name/value pairs.
    return render(request, 'inventory/index.html', {
        'items': items,
    })


# id parameter comes from the named group in the url regex pattern.
def item_detail(request, item_id):
    # return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))

    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        raise Http404('this item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })
