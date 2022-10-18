from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def mainFunc(request):
    return render(request, 'index.html')

class CallView(TemplateView):
    template_name = "callget.html"

def insertFunc(request):
    return render(request, 'insert.html')
    
def insertprocessFunc(request):
    # java : requset.getParameter("name") 이거와 같다
    irum = request.GET.get("name") # GET방식으로 받아와서 get으로 써야한다
    print(irum)
    return render(request, 'list.html', {'myname':irum})

def insertFunc2(request):
    if request.method == 'GET':
        return render(request, 'insert2.html')
    elif request.method == 'POST':
        irum = request.POST.get("name")
        return render(request, 'list.html', {'myname':irum})
    else:
        print('요청 에러')
    
    
    
