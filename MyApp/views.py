from django.shortcuts import render
from .models import Course,Candidiates, Reviews

# Create your views here.
def index(request):
    course = Course.objects.all()

    return render(request,'MyApp/index.html',{'course':course})

def enrollnow(request):
    if request.method == 'POST':
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        city = request.POST.get('city',"")
        course_id = request.POST.get('course_id',"")
        candidiates = Candidiates(candidiate_name = name, candidiate_email=email, candidiate_number= phone,
        candidiate_city= city, course_id=course_id)
        candidiates.save()
        thank = True
        candidiate_id = candidiates.candidiate_id
        print(candidiate_id)
        return render(request,'MyApp/enrollnow.html',{'thank':thank,'ID':candidiate_id})


    return render(request,'MyApp/enrollnow.html')

def courseview(request,id):
    courseId = Course.objects.filter(course_id=id)
    return render(request,'MyApp/courseview.html',{'ID':courseId[0]})

def reviews(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        review = request.POST.get('review', '')
        hide = request.POST.get('hide', 'hide')
        reviews = Reviews(review_name=name, review_email=email, review=review, hide_review= hide)
        reviews.save()
    reviews = Reviews.objects.all()
    # for i in reviews:
    #     if i.hide_review != 'hide':
    #         hide = i.hide_review




    return render(request, 'MyApp/reviews.html', {'reviews':reviews})