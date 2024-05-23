import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.my_landing_page.controller.landing_page import MyController

class MyLandingPagePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'my_landing_page')

    def before_map(self, map):
        map.connect('home', '/', controller='ckanext.my_landing_page.controller.landing_page:MyController', action='index')
        return map

    def get_helpers(self):
        return {
            'my_group_list': self.my_group_list
        }

    def my_group_list(self, limit=20):
        context = {'user': toolkit.c.user}
        data_dict = {'all_fields': True, 'limit': limit}
        return toolkit.get_action('group_list')(context, data_dict)
