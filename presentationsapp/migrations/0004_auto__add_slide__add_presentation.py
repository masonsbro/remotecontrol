# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table(u'presentationsapp_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('next', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['presentationsapp.Slide'], null=True)),
        ))
        db.send_create_signal(u'presentationsapp', ['Slide'])

        # Adding model 'Presentation'
        db.create_table(u'presentationsapp_presentation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['presentationsapp.User'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('first_slide', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['presentationsapp.Slide'], null=True)),
        ))
        db.send_create_signal(u'presentationsapp', ['Presentation'])


    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table(u'presentationsapp_slide')

        # Deleting model 'Presentation'
        db.delete_table(u'presentationsapp_presentation')


    models = {
        u'presentationsapp.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['presentationsapp.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'first_slide': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['presentationsapp.Slide']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'presentationsapp.slide': {
            'Meta': {'object_name': 'Slide'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'next': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['presentationsapp.Slide']", 'null': 'True'})
        },
        u'presentationsapp.user': {
            'Meta': {'object_name': 'User'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'password_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'reset_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['presentationsapp']