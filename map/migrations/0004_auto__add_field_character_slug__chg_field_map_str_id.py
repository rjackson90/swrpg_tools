# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Character.slug'
        db.add_column('map_character', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', blank=True, unique=True, max_length=60),
                      keep_default=False)


        # Changing field 'Map.str_id'
        db.alter_column('map_map', 'str_id', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=60))

    def backwards(self, orm):
        # Deleting field 'Character.slug'
        db.delete_column('map_character', 'slug')


        # Changing field 'Map.str_id'
        db.alter_column('map_map', 'str_id', self.gf('django.db.models.fields.SlugField')(max_length=30, unique=True))

    models = {
        'map.character': {
            'Meta': {'object_name': 'Character'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'portrait': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'blank': 'True', 'unique': 'True', 'max_length': '60'}),
            'strain': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'strain_threshold': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'wound_threshold': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'wounds': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'map.map': {
            'Meta': {'object_name': 'Map'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'str_id': ('django.db.models.fields.SlugField', [], {'blank': 'True', 'unique': 'True', 'max_length': '60'}),
            'title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'})
        }
    }

    complete_apps = ['map']