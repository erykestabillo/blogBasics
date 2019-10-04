from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import (ContList,
                    ContDetail,
                    ContNew,
                    ContEdit,
                    ContDelete,
                    CategoryList,
                    )

urlpatterns = [
    path('', ContList.as_view(), name = 'contList'),
    path('content/<int:content_id>/', ContDetail.as_view(), name = 'contDetail'),
    path('content/new/', ContNew.as_view(), name = 'contNew'),
    path('content/edit/<int:content_id>/', ContEdit.as_view(), name = 'contEdit'),
    path('content/delete/<int:content_id>', ContDelete.as_view(), name = 'contDelete'),
    path('category/<int:category_id>/', CategoryList.as_view(), name = 'catList'),
]