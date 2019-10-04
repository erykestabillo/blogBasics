from django.shortcuts import render, redirect,render_to_response
from .models import Content,Category
from django.utils import timezone
from .forms import ContentForm
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#def contList(request):
#    cont = Content.objects.filter(datePublished__lte = timezone.now()).order_by('datePublished')
#    return render(request, 'userApp/contentList.html', {'cont' : cont})

class ContList(LoginRequiredMixin,TemplateView):
    #import pdb; pdb.set_trace()
    login_url = '/accounts/login/'
    template_name = "contentList.html"

    def get(self, request, **kwargs):
        contents = Content.objects.filter(date_published__lte = timezone.now()).order_by('date_published')
        category_list = Category.objects.all()
        return render(request,self.template_name, {"queryset":contents, "category_list": category_list})
    
    

class CategoryList(TemplateView):
    template_name = "contentList.html"
    def get(self,request,**kwargs):
        category_id = kwargs.get('category_id')
        categ = Category.objects.get(pk = category_id)
        queryset = Content.objects.filter(category = categ)
        category_list = Category.objects.all()
        
        return render(request,self.template_name, {"queryset":queryset, "category_list": category_list})

class TagList(TemplateView):
    template_name = "contentList.html"
    def get(self,request,**kwargs):
        tag = kwargs.get('tag')

        queryset = Content.objects.filter(tags__name = tag)
        
        return render(request,self.template_name, {"queryset":queryset})
        

#def contDetail(request,pk):
#    cont = Content.objects.get(pk=pk)
#    return render(request,'userApp/contentDetail.html', {'cont' : cont})


class ContDetail(LoginRequiredMixin,TemplateView):
    template_name = "contentDetail.html"
    login_url = '/accounts/login/'

    def get(self, request, **kwargs):
        content_id = kwargs.get('content_id')
        content = get_object_or_404(Content,pk = content_id)
        #queryset = Content.objects.get(pk=content_id)
        return render(request,self.template_name, {'cont' : content_id, 'queryset':content})


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

class ContNew(LoginRequiredMixin,TemplateView):
    template_name = "contentNew.html"
    form = ContentForm
    login_url = '/accounts/login/'


    def get(self, request):
        form = self.form()
        return render(request,self.template_name, {'form':form})

    def post(self, request):
        form = self.form(request.POST,request.FILES)
        if form.is_valid():
            queryset = form.save(commit=False)
            queryset.author = request.user
            queryset.date_published = timezone.now()
            queryset.save()
            form.save_m2m()
            return redirect('contList')
        
        return render(request,self.template_name, {'form':form})



        
        



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

class ContEdit(TemplateView):
    template_name = "contentNew.html"
    form = ContentForm

    def get(self, *args, **kwargs):
        
        content_id = kwargs.get('content_id')
        content = Content.objects.get(pk=content_id)
        form = self.form(instance=content)
        return render(self.request,self.template_name, {'form':form})

    def post(self,request,**kwargs):
        content_id = kwargs.get('content_id')
        content = Content.objects.get(pk=content_id)
        form = self.form(request.POST,request.FILES,instance=content)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.author = request.user
            form_data.date_published = timezone.now()
            form_data.save()
            form.save_m2m()
            return redirect('contList')

        return render(request,self.template_name, {'form':form})
        
#def contDelete(request,pk):
#    cont = Content.objects.get(pk=pk)
#    cont.delete()
#    return redirect('contList')

class ContDelete(TemplateView):

    def post(self,request,**kwargs):
        content_id = kwargs.get('content_id')
        content = Content.objects.get(pk=content_id, author=request.user)
        content.image.delete(save=True)
        content.delete()
        return redirect('contList')
    