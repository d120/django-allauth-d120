from django.apps import AppConfig


class D120ProviderConfig(AppConfig):
    name = 'allauth_d120_provider'
    verbose_name = 'Allauth D120 Auth Provider'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from .signals import sig_sync_user_to_groups
