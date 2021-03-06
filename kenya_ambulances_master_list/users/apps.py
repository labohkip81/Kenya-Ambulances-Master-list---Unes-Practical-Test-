from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "kenya_ambulances_master_list.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import kenya_ambulances_master_list.users.signals  # noqa F401
        except ImportError:
            pass
