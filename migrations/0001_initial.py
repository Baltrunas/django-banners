# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'URL'
        db.create_table('banners_url', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('regex', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('banners', ['URL'])

        # Adding M2M table for field sites on 'URL'
        m2m_table_name = db.shorten_name('banners_url_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('url', models.ForeignKey(orm['banners.url'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique(m2m_table_name, ['url_id', 'site_id'])

        # Adding model 'BannerGroup'
        db.create_table('banners_bannergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('speed', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2000)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('banners', ['BannerGroup'])

        # Adding model 'Banner'
        db.create_table('banners_banner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('img', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='banners', to=orm['banners.BannerGroup'])),
            ('often', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('hrml', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flash', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('banners', ['Banner'])

        # Adding M2M table for field urls on 'Banner'
        m2m_table_name = db.shorten_name('banners_banner_urls')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('banner', models.ForeignKey(orm['banners.banner'], null=False)),
            ('url', models.ForeignKey(orm['banners.url'], null=False))
        ))
        db.create_unique(m2m_table_name, ['banner_id', 'url_id'])

        # Adding model 'Log'
        db.create_table('banners_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='banner_logs', to=orm['banners.Banner'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='group_logs', blank=True, to=orm['banners.BannerGroup'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='users', null=True, to=orm['auth.User'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('page', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=1)),
        ))
        db.send_create_signal('banners', ['Log'])

        # Adding M2M table for field urls on 'Log'
        m2m_table_name = db.shorten_name('banners_log_urls')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('log', models.ForeignKey(orm['banners.log'], null=False)),
            ('url', models.ForeignKey(orm['banners.url'], null=False))
        ))
        db.create_unique(m2m_table_name, ['log_id', 'url_id'])

        # Adding model 'LogStat'
        db.create_table('banners_logstat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='banner_stat', blank=True, to=orm['banners.Banner'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='group_stat', blank=True, to=orm['banners.BannerGroup'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('view', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('click', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('unique_click', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('unique_view', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('banners', ['LogStat'])

        # Adding M2M table for field urls on 'LogStat'
        m2m_table_name = db.shorten_name('banners_logstat_urls')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('logstat', models.ForeignKey(orm['banners.logstat'], null=False)),
            ('url', models.ForeignKey(orm['banners.url'], null=False))
        ))
        db.create_unique(m2m_table_name, ['logstat_id', 'url_id'])


    def backwards(self, orm):
        # Deleting model 'URL'
        db.delete_table('banners_url')

        # Removing M2M table for field sites on 'URL'
        db.delete_table(db.shorten_name('banners_url_sites'))

        # Deleting model 'BannerGroup'
        db.delete_table('banners_bannergroup')

        # Deleting model 'Banner'
        db.delete_table('banners_banner')

        # Removing M2M table for field urls on 'Banner'
        db.delete_table(db.shorten_name('banners_banner_urls'))

        # Deleting model 'Log'
        db.delete_table('banners_log')

        # Removing M2M table for field urls on 'Log'
        db.delete_table(db.shorten_name('banners_log_urls'))

        # Deleting model 'LogStat'
        db.delete_table('banners_logstat')

        # Removing M2M table for field urls on 'LogStat'
        db.delete_table(db.shorten_name('banners_logstat_urls'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'banners.banner': {
            'Meta': {'object_name': 'Banner'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'flash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'banners'", 'to': "orm['banners.BannerGroup']"}),
            'hrml': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'often': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'urls': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'url_banners'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['banners.URL']"})
        },
        'banners.bannergroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'BannerGroup'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'speed': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2000'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'banners.log': {
            'Meta': {'object_name': 'Log'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'banner_logs'", 'to': "orm['banners.Banner']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_logs'", 'blank': 'True', 'to': "orm['banners.BannerGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '1'}),
            'urls': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'url_logs'", 'blank': 'True', 'to': "orm['banners.URL']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'users'", 'null': 'True', 'to': "orm['auth.User']"}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        },
        'banners.logstat': {
            'Meta': {'object_name': 'LogStat'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'banner_stat'", 'blank': 'True', 'to': "orm['banners.Banner']"}),
            'click': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_stat'", 'blank': 'True', 'to': "orm['banners.BannerGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unique_click': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unique_view': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'urls': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'url_bloks'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['banners.URL']"}),
            'view': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'banners.url': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'URL'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'regex': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'site_urls'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sites.Site']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['banners']