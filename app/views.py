from django.shortcuts import render
from app.forms import NameForm, HowOldForm, OrderForm,FontForm,TeenForm,xyzForm,averageForm
from django.http.response import HttpResponse
from django.http.request import HttpRequest


# Create your views here.

#OPENING PAGE
def main_page(request:HttpRequest) -> render:
    return render(request, "index.html")

def function_page(request: HttpRequest) -> render:
    return render(request, "function.html")


#CODINGBAT OVER FORMS
def codingbat_page(request: HttpRequest) -> render:
    return render(request, "codingbat.html")

def render_font_time(request:HttpRequest) -> render:
    form = FontForm(request.GET)
    if form.is_valid():
        str_1 = form.cleaned_data["str_1"]
        num_1 = form.cleaned_data["num_1"]
        front_len = 3
        if front_len > len(str_1):
            front_len = len(str_1)
        front = str_1[:front_len]
        
        result = ""
        for i in range(num_1):
            result = result + front
        return render(request, "font-time-page.html",{"form":form, "result":result})
    else:
        return render(request, "font-time-page.html")
    
def render_no_teen(request:HttpRequest) -> render:
    form = TeenForm(request.GET)
    if form.is_valid():
        int_value1 = form.cleaned_data["int_value1"]
        int_value2 = form.cleaned_data["int_value2"]
        int_value3 = form.cleaned_data["int_value3"]

        def not_teen(n):
            return n if n not in [13,14,15,16,17,18,19] else 0

        total = not_teen(int_value1)+not_teen(int_value2)+not_teen(int_value3)
        return render(request, "no-teen-sum.html", {"form":form, "total":total})
    else:
        return render(request, "no-teen-sum.html")
    


def xyz_there(request:HttpRequest) -> render:
    form = xyzForm(request.GET)
    if form.is_valid():
        xyz_string = form.cleaned_data["xyz_string"]
        if "xyz" in xyz_string and ".xyz" not in xyz_string:
            answer = True
        else:
            answer = False
        return render(request, "xyz.html", {"form":form, "answer":answer})
    else:
        return render(request, "xyz.html")

def centered_average(request:HttpRequest) -> render:
    form = averageForm(request.GET)
    if form.is_valid():
        val_1 = form.cleaned_data["val_1"]
        val_2 = form.cleaned_data["val_2"]
        val_3 = form.cleaned_data["val_3"]
        val_4 = form.cleaned_data["val_4"]
        val_5 = form.cleaned_data["val_5"]
        val_6 = form.cleaned_data["val_6"]
        val_7 = form.cleaned_data["val_7"]

        if val_6 is None:
            nums = [val_1,val_2,val_3,val_4,val_5]
        elif val_7 is None:
            nums = [val_1,val_2,val_3,val_4,val_5,val_6]
        else:
            nums = [val_1,val_2,val_3,val_4,val_5,val_6,val_7]

        nums.sort()
        average = sum(nums[1:-1]) / (len(nums) - 2)

        return render(request, "centered-average.html", {"average":average,"form":form})
    else:
        return render(request, "centered-average.html")



#FUNCTIONS OVER FORMS

def hey_you_page(request: HttpRequest):
    form = NameForm(request.GET)
    if form.is_valid():
        input_name = form.cleaned_data["name_input"]
        return render(request, "hey.html", {"form":form, "name_input": input_name})
    else:
        return render(request, "hey.html", {"form":form})


def render_old(request: HttpRequest):
    form = HowOldForm(request.GET)
    if form.is_valid():
        birth_year = form.cleaned_data["birth_year"]
        age_year = form.cleaned_data["age_year"]
        answer = age_year - birth_year
        return render(
            request,
            "how_old.html",
            {"birth_year": birth_year, "age_year": age_year, "answer": answer},
        )
    else:
        return render(request, "how_old.html")


def render_order(request: HttpRequest):
    form = OrderForm(request.GET)
    if form.is_valid():
        Burger = form.cleaned_data["Burger"]
        Fries = form.cleaned_data["Fries"]
        Drink = form.cleaned_data["Drink"]
        BurgerT = Burger * 4.5
        FriesT = Fries * 1.5
        DrinkT = Drink * 1
        total = BurgerT + FriesT + DrinkT
        return render(request,"order.html",{"Burger": Burger, "Fries": Fries, "Drink": Drink, "total": total})
    else:
        return render(request, "order.html")