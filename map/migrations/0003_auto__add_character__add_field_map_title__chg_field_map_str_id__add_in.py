# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Character'
        db.create_table('map_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('portrait', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('wound_threshold', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('strain_threshold', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('wounds', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('strain', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('map', ['Character'])

        # Adding field 'Map.title'
        db.add_column('map_map', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=60, default='', blank=True),
                      keep_default=False)


        # Changing field 'Map.str_id'
        db.alter_column('map_map', 'str_id', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=30))
        # Adding index on 'Map', fields ['str_id']
        db.create_index('map_map', ['str_id'])


    def backwards(self, orm):
        # Removing index on 'Map', fields ['str_id']
        db.delete_index('map_map', ['str_id'])

        # Deleting model 'Character'
        db.delete_table('map_character')

        # Deleting field 'Map.title'
        db.delete_column('map_map', 'title')


        # Changing field 'Map.str_id'
        db.alter_column('map_map', 'str_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30))

    models = {
        'map.character': {
            'Meta': {'object_name': 'Character'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'portrait': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'strain': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'strain_threshold': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'wound_threshold': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'wounds': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'map.map': {
            'Meta': {'object_name': 'Map'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'str_id': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        }
    }

    complete_apps = ['map']