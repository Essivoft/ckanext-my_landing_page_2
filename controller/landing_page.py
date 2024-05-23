import ckan.plugins.toolkit as toolkit

class MyController(toolkit.BaseController):
    def index(self):
        return toolkit.render('home/landing_page.html')
