from django.shortcuts import render
from plan_A_app.models import Plan1
from plan_B_app.models import Plan2
from plan_C_app.models import Plan3


def home(request):
    plan_a = Plan1.objects.all()
    plan_b = Plan2.objects.all()
    plan_c = Plan3.objects.all()
    return render(request,'home_app/index.html',context={'plan_a':plan_a,'plan_b': plan_b, 'plan_c':plan_c})