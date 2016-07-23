from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Tag
from .forms import TagSelectForm


class Home(ListView):
    def get_queryset(self):
        # Defaults to `all` (when `tag` attribute is not present in GET request)
        tag_id = self.request.GET.get('tag', 'all')
        if tag_id == 'all':
            queryset = Product.objects.all()
        else:
            tag = Tag.objects.get(id=tag_id)
            queryset = tag.product_set.all()
        #-----------------------------------------------------------------------
        # This section slows the site down as the database has to be updated
        # for all the items in queryset. If queryset is bigger, it takes longer.
        # This is only tested in SQLite3 on magnetic storage. Results may
        # improve if the data access speed is fast. This is fairly likely to be
        # the case for more performant databases like MySQL, PostgreSQL, etc.
        for product in queryset:
            product.rating += 1
            product.save()
        #-----------------------------------------------------------------------
        return queryset.order_by('-rating')

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        form = TagSelectForm(initial={'tag': self.request.GET.get('tag', 'all')})
        context.update({'form': form})
        return context


class ProductDetail(DetailView):
    model = Product

    def get_object(self, queryset=None):
        obj = super(ProductDetail, self).get_object(queryset)
        obj.rating += 10
        obj.save()
        return obj
