from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView


from .forms import ReviewForm
from .models import Review


class ReviewView(CreateView):
    model = Review
    # fields = "__all__"
    form_class = ReviewForm
    template_name = "reviews/reviews.html"
    success_url = "/thank-you"

# no need to validate for createvew
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

# post get methods classic view
    # def get(self,request):
    #     form = ReviewForm()
    #
    #     return render(request, "reviews/reviews.html", {
    #         "form": form
    #     })
    #
    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    #
    #     return render(request, "reviews/reviews.html", {
    #         "form": form
    #     })

# classic view function instead of classView
# def review(request):
#     # manual form without django
#     if request.method == "POST":
#         # entered_username = request.POST['username']
#         # excisting_data = Review.objects.get(pk=1)
#         form = ReviewForm(request.POST)
#         # if entered_username == "" and len(entered_username)>=100:
#         #     return render(request, "reviews/reviews.html", {
#         #         "has_error": True
#         #     })
#         if form.is_valid():
#             # no output, now storing to the DB
#             # print(form.cleaned_data)
#
#             # no needed to save it if modelform is used
#             # review = Review(user_name=form.cleaned_data['user_name'],
#             #                 review_text = form.cleaned_data['review_text'],
#             #                 rating =form.cleaned_data['rating'], )
#             # review.save()
#             form.save()
#
#             return HttpResponseRedirect("/thank-you")
#
#     else:
#
#          form = ReviewForm()
#
#     return render(request, "reviews/reviews.html", {
#         "form": form
#     })

# ordinary view function
# def thank_you(request):
#     return render(request, "reviews/thank_you.html", {
#         "has_error": False
#     })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "this works"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

# filtering all the list
    # def get_queryset(self):
    #     base_query=  super().get_queryset()
    #     data= base_query.filter(rating__gt=4)
    #     return data

# classic templateview
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"]= reviews
    #     return context


class DetailedReviewView(DetailView):
    template_name = "reviews/detailed_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request=self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


# ordinary templateview
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     detailed = Review.objects.get(pk=review_id)
    #     context["detailed"]=detailed
    #     return context
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # cant store objects in sessions
        # fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"]=review_id
        return HttpResponseRedirect("/reviews/" + review_id)