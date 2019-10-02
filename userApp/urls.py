from django.urls import path
from . import views
from .views import (contList,
                    contDetail,
                    contNew,
                    contEdit,
                    contDelete,
                    )

urlpatterns = [
    #path('', views.contList, name = 'contList'),
    path('', contList.as_view(), name = 'contList'),
    path('content/<int:content_id>/', contDetail.as_view(), name = 'contDetail'),
    path('content/new/', contNew.as_view(), name = 'contNew'),
    path('content/edit/<int:content_id>/', contEdit.as_view(), name = 'contEdit'),
    path('content/delete/<int:content_id>', contDelete.as_view(), name = 'contDelete')
]