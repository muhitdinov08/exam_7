from django.urls import path

from liberty_market.views import Home_page, Explore_page, Item_detail, UserLoginView, UserRegisterView, UserLogoutView, \
    CreateItem, Author_page, OrdersView, Filter_category, MyItems, Filter_items_category, UpdateItem

app_name = 'liberty_market'
urlpatterns = [
    path('', Home_page.as_view(), name='home_page'),
    path('my_item/', MyItems.as_view(), name='my_item'),
    path('explore/', Explore_page.as_view(), name='explore_page'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('order/<id>', OrdersView.as_view(), name='order_page'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('create/', CreateItem.as_view(), name='create_item'),
    path('author_list/', Author_page.as_view(), name='author'),
    path('explore/<category_id>', Filter_category.as_view(), name='filter_page'),
    path('update_item/<item_id>', UpdateItem.as_view(), name='update_item'),
    path('my_items/<category_id>', Filter_items_category.as_view(), name='filter'),
    path('item_detail/<pk>', Item_detail.as_view(), name='item_details'),
]
