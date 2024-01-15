from django.shortcuts import render
from django.views.generic import TemplateView

from core.services import generate_data


class RecordsView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super(RecordsView, self).get_context_data(**kwargs)
        print(generate_data())
        context["items"] = generate_data()
        return context


