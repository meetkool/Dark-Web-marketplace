from django.urls import path, include, re_path

from . import views as account_views
from orders import views as order_views

urlpatterns = [
    path('', include("accounts.passwords.urls")),
    # Removed: path('accounts/', include('django.contrib.auth.urls')) - conflicts with our logout URL

    # url(r'^profile/update/pgp-key/$', account_views.UserPgpUpdateView.as_view(), name='user_pgp_update'),

    re_path(r'^profile/update/change_terms/$', account_views.Changeterms.as_view(), name='change_terms'),
    re_path(r'^profile/update/pgp-key/$', account_views.UserPgpUpdateView.as_view(), name='user_pgp_update'),
    re_path(r'^profile/$', account_views.UserProfileView.as_view(), name='user_profile'),
    re_path(r'^profile/favorite/$', account_views.favorite_detail, name='user_favorites'),
    re_path(r'^ratings/$', account_views.user_ratings, name='user_ratings'),
    re_path(r'^profile/vendor_stats/$', account_views.vendor_stats, name='vendor_stats'),


    # User Order(s)
    re_path(r'^orders/$', account_views.UserOrdersListView.as_view(), name='user_order_list'),
    re_path(r'^orders/(?P<order_id>\d+)/$', account_views.UserOrderDetailView.as_view(), name='user_order_detail'),
    re_path(r'^completeOrder/(?P<order_id>\d+)/$', account_views.complete_order, name='user_order_complete'),
    re_path(r'^disputeOrder/(?P<order_id>\d+)/$', account_views.dispute_order, name='user_order_dispute'),
    re_path(r'^waiting/(?P<order_id>\d+)/(?P<address>[-\w]+)/(?P<cost>\d+\.\d{8})$', order_views.waiting, name='waiting'),

    # Trust/Untrust
    re_path(r'^trust/$', account_views.trust_vendor, name='trust_vendor'),
    re_path(r'^untrust/$', account_views.untrust_vendor, name='untrust_vendor'),

    # Commenting
    re_path(r'^comment/$', account_views.comment_order_item, name='comment_order_item'),
]
