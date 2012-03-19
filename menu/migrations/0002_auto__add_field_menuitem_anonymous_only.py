# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'MenuItem.anonymous_only'
        db.add_column('menu_menuitem', 'anonymous_only', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'MenuItem.anonymous_only'
        db.delete_column('menu_menuitem', 'anonymous_only')


    models = {
        'menu.menu': {
            'Meta': {'object_name': 'Menu'},
            'base_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'menu.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'anonymous_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['menu.Menu']"}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['menu']
