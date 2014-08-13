# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Encounter'
        db.create_table('map_encounter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(blank=True, max_length=60, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('scene', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['map.Map'])),
        ))
        db.send_create_signal('map', ['Encounter'])

        # Adding M2M table for field characters on 'Encounter'
        m2m_table_name = db.shorten_name('map_encounter_characters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('encounter', models.ForeignKey(orm['map.encounter'], null=False)),
            ('character', models.ForeignKey(orm['map.character'], null=False))
        ))
        db.create_unique(m2m_table_name, ['encounter_id', 'character_id'])


    def backwards(self, orm):
        # Deleting model 'Encounter'
        db.delete_table('map_encounter')

        # Removing M2M table for field characters on 'Encounter'
        db.delete_table(db.shorten_name('map_encounter_characters'))


    models = {
        'map.character': {
            'Meta': {'object_name': 'Character'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'portrait': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'blank': 'True', 'max_length': '60', 'unique': 'True'}),
            'strain': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'strain_threshold': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'wound_threshold': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'wounds': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'map.encounter': {
            'Meta': {'object_name': 'Encounter'},
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['map.Character']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'scene': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['map.Map']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'blank': 'True', 'max_length': '60', 'unique': 'True'})
        },
        'map.map': {
            'Meta': {'object_name': 'Map'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'str_id': ('django.db.models.fields.SlugField', [], {'blank': 'True', 'max_length': '60', 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'})
        }
    }

    complete_apps = ['map']