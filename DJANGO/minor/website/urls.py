
from django.urls import path
from . import views
from . import signup
from . import recommendation
from . import SecondRecommendation

urlpatterns = [
    path('',views.index,name="Home"),
    path('about/',views.about,name="about"),

    path("contact/", views.contact, name="contact"),
    path("reservation/", views.reservation, name="reservation"),
    path("reservationshow/", views.reservationshow, name="reservationshow"),


    path("contactshow/", views.contactshow, name="contactshow"),

    path('meal/',views.meal,name="meal"),
    path('mealaffich/',views.mealaffich,name="mealaffich"),
    path('meall/',views.meall,name="meall"),
    path('nutrient/',views.nutrient,name="nutrient"),
    path('diet/',views.diet,name="diet"),

    path('emp',views.emp),
    path('show',views.show),
        path('showusers',views.showusers),

    path('guidelinesuser/',views.guidelinesuser),

    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
    path('deletereservation/<int:id>',views.deletereservation),
    path('deletecontact/<int:id>',views.deletecontact),



    path('order/',views.order,name="order"),
    path('signup/',signup.signup_user,name="signup"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('create_profile/',signup.create_profile,name="create_profile"),
    path('buy/',views.buy,name="buy"),
    path('decider/',views.decider,name="decider"),
    path('recommend/',recommendation.Recommend,name="recommend"),
    path('SecondRecommend/',SecondRecommendation.Recommend,name="SecondRecommend"),
    path('LikeRate/',views.LikeRate,name="LikeRate"),
]