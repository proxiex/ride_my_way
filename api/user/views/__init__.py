from api.user.views.create_user import RegisterAPI
from api.user.views.login_user import LoginAPI


class UserView(
    RegisterAPI,
    LoginAPI
):
    pass


user_view = UserView()
