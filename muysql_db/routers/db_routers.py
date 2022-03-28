class UserRouter:
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user_info'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'user_info'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label in self.route_app_labels or
                obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'user_info'
        return None


class StudentRouter:
    route_app_labels = {'student'}  # should be the app name - my app name is "user_app"

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'akshay'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'akshay'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'akshay'
        return None


class TeacherRouter:
    route_app_labels = {'teacher'}  # should be the app name - my app name is "user_app"

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'manu'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'manu'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'manu'
        return None
