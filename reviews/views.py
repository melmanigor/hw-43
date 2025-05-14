from django.shortcuts import render,get_object_or_404,redirect
from clothing.models import ClothingModel
from .models import ReviewModel
from .forms import ReviewForm

def clothing_reviews(request,pk):
    clothing=get_object_or_404(ClothingModel,pk=pk)
    reviews=clothing.reviews.all()
    return render(request,'reviews/clothing_reviews.html',{
        'clothing':clothing,
        'reviews':reviews
        })

def add_review(request,pk):
    clothing=get_object_or_404(ClothingModel,pk=pk)
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.clothing=clothing
            review.save()
            return redirect('clothing_detail', pk=clothing.pk)
    else:
        form=ReviewForm()
    return render(request,'reviews/add_review.html',{'form':form,'clothing':clothing})
