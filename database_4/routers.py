class Router(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'database_4':
            return 'database_4'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'database_4':
            return 'database_4'
        return None

    def allow_syncdb(self, db, model):

        if db == 'database_4':
            return model._meta.app_label == 'database_4'
        elif model._meta.app_label == 'database_4':
            return False
        return None
