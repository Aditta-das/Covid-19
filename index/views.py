from django.shortcuts import render, redirect
from .models import Covid
from .forms import CreateForm
from django.views.generic import View, ListView, DetailView

class IndexView(View):
    def get(self, *args, **kwargs):
        form = CreateForm()
        return render(self.request, 'index.html', {'form': form})

    def post(self, *args, **kwargs):
        form = CreateForm(self.request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            breath = form.cleaned_data['breath']
            fever = form.cleaned_data['fever']
            cough = form.cleaned_data['cough']
            chills = form.cleaned_data['chills']
            sudden_confusion = form.cleaned_data['sudden_confusion']
            digestive = form.cleaned_data['digestive']
            pink_eye = form.cleaned_data['pink_eye']
            loss_taste = form.cleaned_data['loss_taste']
            fatigue = form.cleaned_data['fatigue']
            congestion = form.cleaned_data['congestion']

            cov = Covid(
                name=name,
                age=age,
                breath=breath,
                fever=fever,
                cough=cough,
                chills=chills,
                sudden_confusion=sudden_confusion,
                digestive=digestive,
                pink_eye=pink_eye,
                loss_taste=loss_taste,
                fatigue=fatigue,
                congestion=congestion,
            )
            cov.save()
            return redirect('/')
        return render(self.request, 'index.html')

def result(request):
    return render(request, 'resultwash.html')