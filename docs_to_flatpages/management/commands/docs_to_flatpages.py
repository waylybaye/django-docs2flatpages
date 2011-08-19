from optparse import make_option
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    args = ""
    help = ""

    option_list = BaseCommand.option_list + (
        make_option("--base_dir", default=None, dest="base_dir",
            help="Specifies the basedir name"),
        make_option("--base_url", default="/", dest="base_url",
            help="Specifies the base url, default '/' "),
        make_option("--enable-comments", "-c", action="store_true", dest="enable_comments",
            help="Enable comments"),
        make_option("--registration-required", "-r", action="store_true", dest="registration_required",
            help="Registration Required")
    )
    
    def handle(self, *args, **options):
        """ """
        print args
        print options
        print "**"*20
        for path in args:
            os.path.walk(path, generate_flatpage, options)



def generate_flatpage(options, dirname, names):
    """
    """
    for file_full_name in names:
        file_name, ext = os.path.splitext(file_full_name)
        _dirname = dirname
        if _dirname.startswith(options['base_dir']):
            _dirname = _dirname[len(options['base_dir']):]
        url = os.path.join(options['base_url'], _dirname, file_name + '/')
        
        title = file_name
        content = open(os.path.join(dirname, file_full_name)).read()
        site = Site.objects.get(id=settings.SITE_ID)

        if FlatPage.objects.filter(url=url).count() > 0:
            FlatPage.objects.filter(url=url).delete()

        flatpage = FlatPage.objects.create(
            url = url,
            title = title,
            content = content,
            enable_comments = bool(options['enable_comments']),
            registration_required = bool(options['registration_required']),
        )
        flatpage.sites = [site]
        print "generate flatpage from", dirname, file_full_name, "url: ", flatpage.url
