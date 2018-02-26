from django.utils.translation import ugettext_lazy as _
from django.db import models


class Menu(models.Model):
    name = models.CharField(
        _(u'Name'),
        max_length=100
        )

    slug = models.SlugField(
        _(u'Slug')
        )

    base_url = models.CharField(
        _(u'Base URL'),
        max_length=100,
        blank=True,
        null=True
        )

    description = models.TextField(
        _(u'Description'),
        blank=True,
        null=True
        )

    class Meta:
        verbose_name = _(u'menu')
        verbose_name_plural = _(u'menus')

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return self.__unicode__()

    def save(self, *args, **kwargs):
        """
        Re-order all items from 10 upwards, at intervals of 10.
        This makes it easy to insert new items in the middle of
        existing items without having to manually shuffle
        them all around.
        """
        super(Menu, self).save(*args, **kwargs)

        current = 10
        for item in MenuItem.objects.filter(menu=self).order_by('order'):
            item.order = current
            item.save()
            current += 10


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        verbose_name=_(u'Name'),
        on_delete=models.CASCADE,
        )

    order = models.IntegerField(
        _(u'Order'),
        default=500
        )

    link_url = models.CharField(
        _(u'Link URL'),
        max_length=100,
        help_text=_(u'URL or URI to the content, eg /about/ or http://foo.com/')
        )

    title = models.CharField(
        _(u'Title'),
        max_length=100
        )

    login_required = models.BooleanField(
        _(u'Login required'),
        blank=True,
        default=False,
        help_text=_(u'Should this item only be shown to authenticated users?')
        )

    anonymous_only = models.BooleanField(
        _(u'Anonymous only'),
        blank=True,
        default=False,
        help_text=_(u'Should this item only be shown to non-logged-in users?')
        )

    class Meta:
        verbose_name = _(u'menu item')
        verbose_name_plural = _(u'menu items')

    def __unicode__(self):
        return u"%s %s. %s" % (self.menu.slug, self.order, self.title)
