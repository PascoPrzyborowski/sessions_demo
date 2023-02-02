from django.shortcuts import render

from .models import Product
# Create your views here.
# detail view using FBV


def detail(request, pk):
    product = Product.objects.get(pk = pk)
    # breakpoint()
    # TODO: visitor count exercise

### Task 2###
    key = f"visitor{pk}"

    if request.session.get(key):
        request.session[key] += 1
    else:
        request.session[key] = 1
    # site_visits = request.session.get('site_visits', 0)
    # request.session['site_visits'] = site_visits + 1
            
    # retrieve information from the session
    site_visits = request.session.get('site_visits')
    
    context = {'product': product, 'site_visits': request.session[key]}
    
    return render(request, 'products/detail.html', context)




### Task 1###

    # if request.session['site_visits']:
    #     request.session['site_visits'] += 1
    # else:
    #     request.session['site_visits'] = 1
    # # site_visits = request.session.get('site_visits', 0)
    # # request.session['site_visits'] = site_visits + 1
            
    # # retrieve information from the session
    # site_visits = request.session.get('site_visits')
    
    # context = {'product': product, 'site_visits': site_visits}
    
    # return render(request, 'products/detail.html', context)

