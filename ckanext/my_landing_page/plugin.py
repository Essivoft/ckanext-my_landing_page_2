import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class MyLandingPagePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'my_landing_page')

    def before_map(self, map):
        map.connect('home', '/', controller='ckanext.my_landing_page.controller:MyController', action='index')
        return map
