from django.shortcuts import render,redirect
from .models import user_data,admin_panel,product,order_detail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Userform


# Create your views here.

def login(request):
    

    if request.method == 'POST':
        if user_data.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            flip = user_data.objects.get(username=request.POST['username'],password=request.POST['password'])
            hm = order_detail.objects.all()
            request.session['username']=flip.username
            return render(request,'succes_login.html',{'flip':flip,'hm':hm})    
        elif admin_panel.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():  
            admin1 = admin_panel.objects.get(username=request.POST['username'],password=request.POST['password'])
            skt = order_detail.objects.all()
            request.session['username']=admin1.username
            context = {
                'admin1':admin1,
                'skt':skt
            }
            return render(request,'adminview.html',context)                                         
        else:
            messages.warning(request,'INVALID ATTEMPT',extra_tags='warn')
            return redirect('/')
    

    
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 =request.POST['password2']
        
        if password==password2:
            if user_data.objects.filter(email=email):
                messages.info(request,'Please enter new email',extra_tags='email')
                return redirect('register')
            elif user_data.objects.filter(username=username):
                messages.info(request,'Please enter new username',extra_tags='username')
                return redirect('register')
            else:    
                profile = user_data(first_name=first_name,last_name=last_name,email=email,password=password,password2=password2,username=username)
                profile.save()
                messages.info(request,f'{first_name} you create account succesfully',extra_tags='lul')
                return redirect('register')
        else:
            messages.info(request,'Please write same password in both fields',extra_tags='password')   
            return redirect('register') 

    return render(request,'register.html')    

def customer(request):
        order = request.session.get('order_detail')
        hm = order_detail.objects.all()
        context = {
            'hm':hm,
            'order':order,
        }
    
        return render(request,'succes_login.html',context)


def place(request):
    sm = user_data.objects.all()
    sp = product.objects.all()
    km = order_detail.objects.all()  
    if request.method == 'POST':
 
        username = request.POST['username']
        product_name = request.POST['product_name']
        productprice = request.POST['productprice']
        quantity = request.POST['quantity']
        total_price = int(request.POST['productprice'])*int(request.POST['quantity'])
        address = request.POST['address']
        number = request.POST['number']
        strm = order_detail(username=username,product_name=product_name,productprice=productprice,quantity=quantity,total_price=total_price,address=address,number=number)
        strm.save()
        messages.info(request,f'{username} you have succesfully submitted order',extra_tags='done')
        return redirect('customer')

    
    context = {
        'sm':sm,
        'sp':sp,
        'km':km,
    }
   
    return render(request,'place.html',context)


def summary(request):
    return render(request,'summary.html')  


def logout(request):
    try:
        del request.session['username']
    except:
        return redirect('/')

    return redirect('/') 

def adminv(request):
    skt = order_detail.objects.all()
    return render(request,'adminview.html',{'skt':skt})    

def delete(request,id,username):
    dele = order_detail.objects.get(id=id,username=username)
    dele.delete()
    messages.info(request,f'Horay.. you deleted {username} smoothly', extra_tags='delet')
    return redirect('adminview')

def update(request,id,username):
    insr = order_detail.objects.get(id=id)
    if request.method == 'POST':
        form = Userform(request.POST,instance=insr)
        if form.is_valid():
            form.save()
        messages.info(request,f'you have succesfully modify {username}',extra_tags='done1')
        return redirect('adminview')

    
    return render(request,'update.html',{'insr':insr})    

        
