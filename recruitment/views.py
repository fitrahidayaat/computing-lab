from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .grader import submit, check, jdoodle

def recruitmentView(req):
    ctx = {
        'title': 'Computing Laboratory - Recruitment'
    }
    return render(req, 'recruitment/recruitment.html', ctx)

def submitView(req):
    if req.method == 'POST':
        nim = req.POST.get('nim')
        solution = req.POST.get('solution')
        return HttpResponse(jdoodle(nim, solution))
        
    return redirect('recruitment')

@csrf_exempt
def checkView(req):
    if req.method == 'POST':
        nim = req.POST.get('nim')
        datas = req.POST.get('datas')
        print(nim)
        print(datas)
        return HttpResponse(check(nim, datas))
        