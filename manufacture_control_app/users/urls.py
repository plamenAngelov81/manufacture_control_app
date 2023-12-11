
from django.urls import path, include

from manufacture_control_app.users.views import AccountRegisterView, AccountLogin, AccountLogOut, AccountDetailsView, \
    AccountEditView, AccountDeleteView, ChangeAccPasswordView, PassChanged, PasswordResetDone, PasswordReset, \
    PasswordResetConfirm, PasswordResetComplete

urlpatterns = [
    path('profile/', include([
        path('register/', AccountRegisterView.as_view(), name='account register'),
        path('login/', AccountLogin.as_view(), name='account login'),
        path('logout/', AccountLogOut.as_view(), name='account logout'),
        path('<int:pk>/', AccountDetailsView.as_view(), name='account details'),
        path('edit/<int:pk>/', AccountEditView.as_view(), name='account edit'),
        path('delete/<int:pk>/', AccountDeleteView.as_view(), name='account delete'),

        path('<int:pk>/change-password', ChangeAccPasswordView.as_view(), name='change password'),
        path('pass-changed/', PassChanged.as_view(), name='password_change_done'),

        path('pass-reset/', PasswordReset.as_view(), name='reset_password'),
        path('pass-reset-send/', PasswordResetDone.as_view(), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
        path('pass-reset-complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
    ])),
]