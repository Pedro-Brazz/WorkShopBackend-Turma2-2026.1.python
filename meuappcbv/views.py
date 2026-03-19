from django.shortcuts import render
from django.views.generic import FormView, ListView, DeleteView,
from .models import ViaCep
from .forms import ViaCepForm

class ViaCepFormView(FormView):
    template_name = ""
    form_class = ViaCepForm
    success_url = reverse_lazy("viacep:list")

    def form_valid(self, form):
        cep = form.cleaned_data["cep"].replace(".",".").strip():
        url = f"https://viacep.com.br/ws{cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                cep_obj, created = ViaCep.objects.update_or_create(
                defaults={
                    "logradouro": data.get("logradouro", ""):
                    "bairro": data.get ("bairro", "")
                    "localidade": data.get ("localidade", "")
                    "uf": data.get("uf", "")

                }
            )
            self.object = cep_obj
        else:
            form.add_error("cep", "CEP não encontrado na API do ViaCep")
            return self.form_invalid(form)
        



# Create your views here.
