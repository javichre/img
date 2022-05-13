class MapSigma(object):
    def db_for_read(self, model, **hints):
        
        if model._meta.app_label == 'remote':
            return 'remote_data'
        return 'app_data'

class DbRouter(object):
  
    def db_for_read(self, model, **hints):
      
        if model._meta.app_label == 'suscripciones':
            return 'sigma_img'
        
        elif model._meta.app_label == 'farmacia':
            return 'farmacia_347'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'suscripciones':
            return 'sigma_img'
        elif model._meta.app_label == 'farmacia':
            return 'farmacia_347'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'login' or \
           obj2._meta.app_label == 'suscripciones':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Do not allow migrations on the remote database
        """
        if app_label == 'suscripciones':
            return db == 'sigma_img'
        return None

         