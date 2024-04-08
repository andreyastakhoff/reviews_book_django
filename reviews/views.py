from django.shortcuts import render, redirect

from django.views import View

from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewsView(View):

    def get(self, request):
        form = ReviewForm()
        reviews = Review.objects.all()

        return render(request, 'reviews.html', {'form': form, 'reviews': reviews})

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')

            Review.objects.create(name=name, email=email, review=review, rating=rating)

            return redirect('reviews')
        
        form = ReviewForm()
        reviews = Review.objects.all()

        return render(request, 'reviews.html', {'form': form, 'reviews': reviews})
