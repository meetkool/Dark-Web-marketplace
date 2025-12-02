from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from accounts import views as account_views
from vendor import views as vendor_views
from main import views as product_views

urlpatterns = [
    path('alibaba/', admin.site.urls),
    path('support/', include('support.urls')),
    re_path(r'^captcha/', include('captcha.urls')),
    re_path(r'^signup/$', account_views.signup, name='signup'),
    re_path(r'^signin/$', account_views.LoginView.as_view(), name='signin'),
    re_path(r'^signin/gpg_auth/$', account_views.gpg_auth, name='gpg_auth'),
    re_path(r'^signin/gpg_verify/$', account_views.gpg_verify, name='gpg_verify'),
    re_path(r'^logout/$', account_views.logout_view, name='logout'),
    re_path(r'^accounts/login/$', RedirectView.as_view(url='/signin')),
    re_path(r'^profile/update_tfalogin', account_views.update_tfalogin, name='update_tfalogin'),
    # Vendor Urls
    re_path(r'^vendor/$', vendor_views.vendor_dashboard, name='vendor_dashboard'),
    re_path(r'^vendor/add_product', vendor_views.add_product, name='user_vendor_add_product'),
    re_path(r'^vendor/save_product', vendor_views.save_product, name='user_vendor_save_product'),
    re_path(r'^vendor/delete_product/(?P<product_id>\d+)/$', vendor_views.delete_product, name='user_vendor_delete_product'),
    re_path(r'^vendor/edit_product/(?P<product_id>\d+)/$', vendor_views.edit_product, name='user_vendor_edit_product'),
    re_path(r'^vendor/shipping_options/(?P<shipping_option_id>\d+)/$', vendor_views.edit_shippingoption, name='shipping_options'),
    re_path(r'^vendor/shipping_options/$', vendor_views.shipping_options, name='shipping_options'), 
    re_path(r'^vendor/update_product/$', vendor_views.update_product, name='user_vendor_updateProduct'),
    re_path(r'^vendor/list_products', vendor_views.list_products, name='user_vendor_listProducts'),
    re_path(r'^vendor_profile/(?P<vendor_id>\d+)/', account_views.vendor_profile, name='vendor_profile'),
    re_path(r'^vendor_public_profile/(?P<vendor_id>\d+)/', account_views.vendor_public_profile, name='vendor_public_profile'),
    re_path(r'^vendor/newOrders/$', vendor_views.VendorNewOrderListView.as_view(), name='vendor_list_new_order'),
    re_path(r'^vendor/newOrders/(?P<order_id>\d+)/$', vendor_views.VendorNewOrderDetailView.as_view(), name='vendor_detail_new_order'),
    re_path(r'^vendor/shipOrders/$', vendor_views.VendorShippedOrderListView.as_view(), name='vendor_list_ship_order'),
    re_path(r'^vendor/shipOrders/(?P<order_id>\d+)/$', vendor_views.VendorShippedOrderDetailView.as_view(), name='vendor_detail_ship_order'),
    re_path(r'^vendor/completeOrders/$', vendor_views.VendorCompleteOrderListView.as_view(), name='vendor_list_complete_order'),
    re_path(r'^vendor/completeOrders/(?P<order_id>\d+)/$', vendor_views.VendorCompleteOrderDetailView.as_view(), name='vendor_detail_complete_order'),
    re_path(r'^vendor/cancelOrders/$', vendor_views.VendorCancelOrderListView.as_view(), name='vendor_list_cancel_order'),
    re_path(r'^vendor/cancelOrders/(?P<order_id>\d+)/$', vendor_views.VendorCancelOrderDetailView.as_view(), name='vendor_detail_cancel_order'),
    re_path(r'^vendor/disputeOrders/$', vendor_views.VendorDisputeOrderListView.as_view(), name='vendor_list_dispute_order'),
    re_path(r'^vendor/disputeOrders/(?P<order_id>\d+)/$', vendor_views.VendorDisputeOrderDetailView.as_view(), name='vendor_detail_dispute_order'),
    re_path(r'^vendor/acceptOrder/(?P<order_id>\d+)/$', vendor_views.accept_order, name='vendor_accept_order'),
    re_path(r'^vendor/rejectOrder/(?P<order_id>\d+)/$', vendor_views.reject_order, name='vendor_reject_order'),

    # Search url
    re_path(r'^search/$', product_views.search, name='search'),
    # path('accounts/', include('django.contrib.auth.urls')),

    re_path(r'^messages/$', product_views.UserMessageListView.as_view(), name='message_list'),

    # Inbox url
    re_path(r'^inbox/$', product_views.UserInboxListView.as_view(), name='inbox_list'),
    re_path(r'^inbox/(?P<message_id>\d+)/delete/$', product_views.delete_message, name='inbox_delete_message'),
    re_path(r'^inbox/send/$', product_views.inbox_send, name='inbox_send'),
    re_path(r'^inbox/send/(?P<receiver_id>\d+)/$', product_views.inbox_send, name='inbox_send'),

    path('account/', include('accounts.urls')),
    re_path(r'^accounts/$', RedirectView.as_view(url='/account')),  # Redirects url "/accounts" to "/account"

    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('background/', include('background.urls')),
    path('', include('main.urls')),
    # Star Rating Url
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),

    # Avatar
    re_path(r'^avatar/', include('avatar.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),

                      # For django versions before 2.0:
                      # url(r'^__debug__/', include(debug_toolbar.urls)),

                  ] + urlpatterns
