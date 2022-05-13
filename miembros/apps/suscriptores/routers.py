class MapSigma(object):
    def db_for_read(self, model, **hints):
        
        if model._meta.app_label == 'puntos':
            return 'sigma_img'
        return 'app_data'



class DbRouter(object):
  
    def db_for_read(self, model, **hints):
      
        if model._meta.app_label == 'puntos':
            return 'sigma_img'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'puntos':
            return 'sigma_img'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'login' or \
           obj2._meta.app_label == 'puntos':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Do not allow migrations on the remote database
        """
        if app_label == 'puntos':
            return db == 'sigma_img'
        return None
