from django.urls import re_path, include
from . import views

app_name = 'support'

urlpatterns =[

    re_path(r'^$', views.support_list, name='support_list'),
    re_path(r'^customer_chat/$', views.customer_chat, name='customer_chat'),
    re_path(r'^customer_ticket_list/$', views.customer_ticket_list, name='customer_ticket_list'),
    re_path(r'^customer_ticket/(?P<c_id>\d+)', views.customer_ticket, name='customer_ticket'),
    re_path(r'^create_ticket/$', views.create_ticket, name='create_ticket'),
    re_path(r'^chat_post_message/$', views.chat_post_message, name='chat_post_message'),
    re_path(r'^customer_post_ticket/$', views.customer_post_ticket, name='customer_post_ticket'),
    re_path(r'^customer_ticket_reply/$', views.customer_ticket_reply, name='customer_ticket_reply'),
    re_path(r'^ticket_state_change/(?P<state>\d+)/(?P<ticket_id>\d+)/(?P<is_admin>\d+)', views.ticket_state_change, name='ticket_state_change'),

    re_path(r'^admin_chat/$', views.admin_chat, name='admin_chat'),
    re_path(r'^admin_chat/(?P<c_id>\d+)', views.admin_chat, name='admin_chat'),
    re_path(r'^admin_ticket_list/$', views.admin_ticket_list, name='admin_ticket_list'),
    re_path(r'^admin_ticket/(?P<c_id>\d+)', views.admin_ticket, name='admin_ticket'),
    re_path(r'^admin_ticket_reply/$', views.admin_ticket_reply, name='admin_ticket_reply'),
]
