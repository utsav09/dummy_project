class Router(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'database_3':
            return 'database_3'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'database_3':
            return 'database_3'
        return None

    def allow_syncdb(self, db, model):

        if db == 'database_3':
            return model._meta.app_label == 'database_3'
        elif model._meta.app_label == 'database_3':
            return False
        return None
