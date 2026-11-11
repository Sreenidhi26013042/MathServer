
from django.shortcuts import render
def churn_bill(request):
    initial_customer = float(request.POST.get('initialcustomer', '0'))
    present_customer= float(request.POST.get('presentcustomer', '0'))
    churn =   (initial_customer/present_customer)*100 if request.method == 'POST' else 0
    
    print("initialcustomer =",initial_customer)
    print("presentcustomer =",present_customer)
    print("churn =",churn)
    return render(request, 'sreeapp/mathserver.html',{'initial_customer':initial_customer, 'present_customer': present_customer, 'churn': churn})











