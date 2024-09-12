from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from big_library.models import Article
from big_library.documents import ArticleDocument
from big_library.forms import DocumentSearchForm, ArticleForm


class DocumentListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = DocumentSearchForm(self.request.GET or None)
        context['form'] = form

        if form.is_valid():
            query = form.cleaned_data['query']
            search_results = ArticleDocument.search().query("multi_match", query=query, fields=['title', 'description', 'content']).execute()
            context['search_results'] = search_results
        else:
            context['search_results'] = None
        return context


class DocumentCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('big_library:document_list')


class DocumentUpdateView(UpdateView):
    model = Article
    fields = ['title', 'description', 'content']

    def get_success_url(self):
        return reverse('big_library:document_detail', kwargs={'pk': self.object.pk})


class DocumentDetailView(DetailView):
    model = Article


class DocumentDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('big_library:document_list')
