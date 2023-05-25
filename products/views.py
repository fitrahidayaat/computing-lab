from django.shortcuts import render

def productsView(req):
    ctx = {
        'title': 'Computing Laboratory - Products'
    }
    return render(req, 'products/sudo.html', ctx)

def products4View(req):
    ctx = {
        'title': 'Computing Laboratory - Products'
    }
    return render(req, 'products/sudo4.html', ctx)

def products16View(req):
    ctx = {
        'title': 'Computing Laboratory - Products'
    }
    return render(req, 'products/sudo16.html', ctx)

def yinYangView(req):
    ctx = {
        'title': 'Yin Yang - Made Indrayana Putra'
    }
    return render(req, 'products/yin_yang.html', ctx)