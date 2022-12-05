from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic
# Create your views here.


class View_user_notes(generic.ListView):
    template_name = 'all.html'
    queryset = models.Model_notes_of_user.objects.all()

    def get_queryset(self):
        return models.Model_notes_of_user.objects.all()

class View_all_books_more(generic.DetailView):
    template_name = 'aboutBook.html'

    def get_object(self, **kwargs):
        id_ = self.kwargs.get('id')
        return get_object_or_404(models.Model_all_books, id=id_)



class View_create_note(generic.CreateView):
    template_name = 'add.html'
    form_class = forms.Form_notes
    queryset = models.Model_notes_of_user.objects.all()
    success_url = '/notes/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(View_create_note, self).form_valid(form=form)


class View_update_note(generic.UpdateView):
    template_name = 'update.html'
    form_class = forms.Form_notes
    success_url = '/notes/'

    def get_object(self, **kwargs):
        note_id = self.kwargs.get('id')
        return get_object_or_404(models.Model_notes_of_user, id=note_id)

    def form_valid(self, form):
        return super(View_update_note, self).form_valid(form=form)


class View_delete_note(generic.DeleteView):
    template_name = 'delete.html'
    success_url = '/notes/'

    def get_object(self, **kwargs):
        note_id = self.kwargs.get('id')
        return get_object_or_404(models.Model_notes_of_user, id=note_id)
