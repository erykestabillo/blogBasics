from django.shortcuts import render, redirect
from .models import Content
from django.utils import timezone
from .forms import contentForm
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.

#def contList(request):
#    cont = Content.objects.filter(datePublished__lte = timezone.now()).order_by('datePublished')
#    return render(request, 'userApp/contentList.html', {'cont' : cont})

class contList(TemplateView):
    model = Content
    
    template_name = "contentList.html"

    def get(self, request, **kwargs):
        queryset = Content.objects.filter(datePublished__lte = timezone.now()).order_by('datePublished')
        return render(request,self.template_name, {"queryset":queryset})


#def contDetail(request,pk):
#    cont = Content.objects.get(pk=pk)
#    return render(request,'userApp/contentDetail.html', {'cont' : cont})


class contDetail(TemplateView):
    model = Content
    template_name = "contentDetail.html"

    def get(self, request, **kwargs):
        content_id = kwargs.get('content_id')
        queryset = Content.objects.get(pk=content_id)
        return render(request,self.template_name, {'cont' : content_id, 'queryset':queryset})


#def contNew(request):
#    if request.method == "POST":
#        form = contentForm(request.POST)
#        if form.is_valid():
#            cont = form.save(commit=False)
#            cont.author = request.user
#            cont.datePublished = timezone.now()
#            cont.save()
#            return redirect('contDetail', pk = cont.pk)
        
#    else:
#        form = contentForm()
#        return render(request, 'userApp/contentNew.html', {'form' : form})

class contNew(TemplateView):
    model = Content
    template_name = "contentNew.html"
    form = contentForm

    def get(self, request):
        form = self.form()
        return render(request,self.template_name, {'form':form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            queryset = form.save(commit=False)
            queryset.author = request.user
            queryset.datePublished = timezone.now()
            queryset.save()
            return redirect('contList')



#def contEdit(request,pk):
#    cont = Content.objects.get(pk=pk)
#    if request.method == "POST":
#        form = contentForm(request.POST,instance = cont)
#        if form.is_valid():
#            cont = form.save(commit=False)
#            cont.author = request.user
#            cont.datePublished = timezone.now()
#            cont.save()
#            return redirect('contDetail', pk = cont.pk)
        
#    else:
#        form = contentForm(instance = cont)
#        return render(request, 'userApp/contentNew.html', {'form' : form})

class contEdit(TemplateView):
    template_name = "contentNew.html"
    form = contentForm

    def get(self, request, **kwargs):
        form = self.form()
        content_id = kwargs.get('content_id')
        queryset = Content.objects.get(pk=content_id)
        form = contentForm(instance=queryset)
        return render(request,self.template_name, {'cont' : content_id, 'queryset':queryset,'form':form})

    def post(self,request,**kwargs):
        content_id = kwargs.get('content_id')
        queryset = Content.objects.get(pk=content_id)
        form = self.form(request.POST,instance=queryset)
        if form.is_valid():
            queryset = form.save(commit=False)
            queryset.author = request.user
            queryset.datePublished = timezone.now()
            queryset.save()
            return redirect('contList')


  



#def contDelete(request,pk):
#    cont = Content.objects.get(pk=pk)
#    cont.delete()
#    return redirect('contList')

class contDelete(TemplateView):

    def get(self,request,**kwargs):
        content_id = kwargs.get('content_id')
        queryset = Content.objects.get(pk=content_id)
        queryset.delete()
        return redirect('contList')
    