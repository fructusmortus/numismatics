from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SaveCollectionForm
from .models import Collection


class CreateCollection(CreateView):
    model = Collection
    form_class = SaveCollectionForm
    template_name = 'save.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(CreateCollection, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateCollection(UpdateView):
    model = Collection
    form_class = SaveCollectionForm
    template_name = 'save.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(UpdateCollection, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class DeleteCollection(DeleteView):
    template_name = 'delete.html'
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Collection, pk=id_)
