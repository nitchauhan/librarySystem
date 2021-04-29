from django.shortcuts import render, HttpResponse, redirect
from . models import Contact, Book
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout    
from .forms import Edit_Blog
from .forms import Purchase_book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# username : lib_app  password :123

# Create your views here.
def home(request):
    return render(request,'home.html')
    
def about(request):
    return render(request,'about.html')

def addbook(request):
    if request.method=='POST':
         name = request.POST['name']
         author = request.POST['author']
         category = request.POST['category']
         bookdesc = request.POST['bookdesc']     
         bookprice = request.POST['bookprice']  
         Tenatative_Return_Date = request.POST['Tenatative_Return_Date']   
         require_date = request.POST['require_date']

       
         if len(name)<2:
            messages.error(request, "plz Fill the Correct name length")    
         elif len(author)<2:
            messages.error(request, "plz Fill the Correct email address")  
         elif len(category)<2:
            messages.error(request, "plz Fill Correct email Catagory")    
         elif len(bookdesc)<10:
            messages.error(request, "plz more word added in descriptions")  
         elif len(bookprice)==0:
            messages.error(request, "plz Fill the two digit price")    
         else:
            book = Book(name=name, author=author, category=category, bookdesc=bookdesc, bookprice=bookprice)
            book.save()
            messages.success(request,"Your book has been succesfully added..")  
            return redirect('viewbook') 
         
    return render(request,'addbook.html')


def viewbook(request):
    post1 = Book.objects.all()
    print(post1)
    paginator = Paginator(post1, 2)
    page = request.GET.get('page')
 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # return render(request, 'viewbook.html',{'post1':post1})
    return render(request, 'viewbook.html',{'page':page,'posts':posts})
    
    
def delete(request,bookid):
    blog = Book.objects.get(bookid=bookid)
    blog.delete()
    print(blog)
    messages.success(request,"Delete succcessfully")
    return redirect('/')
    # return render(request, 'viewbook.html',{'blog':blog})
    
def edit(request,bookid):
    blog = Book.objects.get(bookid=bookid)
    editblog = Edit_Blog(instance=blog)
    if request.method=='POST':
        form = Edit_Blog(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,"Updating Data Succesfully...")
            return redirect('home')

    return render(request,'editbook.html',{'edit_blog':editblog})
    # return render(request,'editbook.html',editblog)


def purchasebook(request,bookid):
    
    blog = Book.objects.get(bookid=bookid)
    purchase_book = Purchase_book(instance=blog)

    if request.method=='POST':
        form = Purchase_book(request.POST)
        name = request.POST['name']   
        bookprice = request.POST['bookprice']   
         
        if len(name)<2:
            messages.error(request, "plz Fill the Correct information")
        
        if (int(bookprice)) > 500:
             messages.error(request,"debt is not more than Rs.500")    
        else:
            book = Book(name=name, bookprice=bookprice)
            book.save()
            messages.success(request,"Your book has been succesfully purchase..") 
            return redirect('purchaseviewbook') 
        #   form = Purchase_book(request.POST,instance=blog)
        #   if form.is_valid():
        #     form.save()
        #     messages.success(request,"purchase book Succesfully...")
        #     return redirect('home')
        # name = request.POST['name']   
        # bookprice = request.POST['bookprice']   
         
    return render(request,'purchasebook.html',{'purchase_book':purchase_book})

def purchaseviewbook(request):
    pv = Book.objects.all()
    print(pv)
    paginator = Paginator(pv, 11)
    page = request.GET.get('page')
 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # return render(request, 'viewbook.html',{'post1':post1})
    # return render(request, 'viewbook.html',{'page':page,'posts':posts})
    return render(request, 'purchaseviewbook.html',{'page':page,'posts':posts})
    # pv = Book.objects.all()
    # print(pv)
    # return render(request, 'purchaseviewbook.html',{'pv':pv})
    
def issuebook(request):
    if request.method=='POST':
         name = request.POST['name']
         author = request.POST['author']
        #  category = request.POST['category']         
        #  bookdesc = request.POST['bookdesc']         
         require_date = request.POST['require_date']
         Tenatative_Return_Date = request.POST['Tenatative_Return_Date']
         
        #  if len(name)<2 or len(author)<3 or len(category)<1:
         if len(name)<2:
            messages.error(request, "plz Fill the Correct Name")    
         if len(author)<2:
            messages.error(request, "plz Fill the Correct author name")    
         else:
            book = Book(name=name, author=author, require_date=require_date, Tenatative_Return_Date=Tenatative_Return_Date)
            book.save()
            messages.success(request,"Your message has been succesfully sent..")
            return redirect('viewissuebook')   
     
    return render(request,'issuebook.html')

def viewissuebook(request):
    viewissue = Book.objects.all()
    print(viewissue)
    return render(request, 'viewissuebook.html',{'viewissue':viewissue})
    
def contact(request):
     if request.method=='POST':
         name = request.POST['name']
         email = request.POST['email']
         phone = request.POST['phone']
         content = request.POST['content']
         print(name,email,phone,content)
         
         
         if len(name)<2:
            messages.error(request, "plz Fill the Correct name length")    
         elif len(email)<2:
            messages.error(request, "plz Fill the Correct email address")  
         elif len(phone)<2:
            messages.error(request, "plz Fill the 10 numbers length")    
         elif len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<4:
            messages.error(request, f"plz Fill the Correct name Email and Phonenumber")
         else:
            contact = Contact(name=name,email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Your message has been succesfully sent..")  
     return render(request,'contact.html')
    
def search(request):
    query = request.GET['query'].upper()
    if len(query)>78:
        allPosts = Book.objects.none()
    else:
        allPostsAuthor = Book.objects.filter(author__icontains=query)
        allPostsTitle = Book.objects.filter(name__icontains=query)
        allPostsContent = Book.objects.filter(bookdesc__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent,allPostsAuthor)

    if allPosts.count() == 0:
         messages.warning(request,"No search Results found.Please refine Your query")
    params = {'allPosts':allPosts, 'query':query}
    return render(request,"search.html",params)

#django API System
def signupHandle(request):
    # get the post param
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
         # check the errorneous inputs
        if len(username) > 10 or len(username) < 2:
            messages.error(request,"Username Must be Under 10 Characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"Username Should only Contain Letter and Characters")
            return redirect('home')

        if len(pass1) > 20 or len(pass1) < 2:
            messages.error(request,"Password Must be Under 10 Characters")
            return redirect('home')           

        if pass1 != pass2:
            messages.error(request,"Password Does Not Match,Please Enter Right Password")
            return redirect('home')

        # create the user(import user auth)
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your I-Coder Acoount Has been Successfully Created.....!")
        return redirect('home')
    else:
        return HttpResponse('404 - NOt Found!!')
       
# loggin - model
def loginHandle(request):
    if request.method == 'POST':
        usernamelogin = request.POST['usernamelogin']
        passwordlogin = request.POST['passwordlogin']

        user = authenticate(username = usernamelogin, password=passwordlogin)
        
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged In")
        else:
            messages.error(request,"Invalid Credentials , Please Try Again")
    return redirect('home')

# log-out model
def logoutHandle(request):
    logout(request)
    messages.success(request,"Successfully Logout")    
    return redirect('home')

