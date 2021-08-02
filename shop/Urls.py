from django.urls import path
from . import views
urlpatterns = [
   path("",views.index,name="shop_home"),
   path("about/",views.about,name="Aboutus"),
   path("contact/",views.contact,name="contactus"),
   path("tracker/",views.tracker,name="Tracking status"),
   path("search/",views.Search,name="Search"),
   path("Productview/",views.Productview,name="productview"),
   path("Checkout/",views.Checkout,name="checkout"),


]
