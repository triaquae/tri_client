# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'trunk_servers'
        db.create_table(u'triWeb_trunk_servers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('port', self.gf('django.db.models.fields.IntegerField')(default=9998)),
        ))
        db.send_create_signal(u'triWeb', ['trunk_servers'])

        # Adding field 'IP.belongs_to'
        db.add_column(u'triWeb_ip', 'belongs_to',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['triWeb.trunk_servers'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'trunk_servers'
        db.delete_table(u'triWeb_trunk_servers')

        # Deleting field 'IP.belongs_to'
        db.delete_column(u'triWeb_ip', 'belongs_to_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'triWeb.actions': {
            'Meta': {'object_name': 'actions'},
            'condition_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.conditions']", 'symmetrical': 'False'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'operation_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.operations']", 'symmetrical': 'False'}),
            'recovery_message': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'recovery_notice': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'recovery_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'triWeb.authbyipandremoteuser': {
            'Meta': {'unique_together': "(('ip', 'remoteUser'),)", 'object_name': 'AuthByIpAndRemoteUser'},
            'authtype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['triWeb.IP']", 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'remoteUser': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['triWeb.RemoteUser']", 'null': 'True', 'blank': 'True'})
        },
        u'triWeb.conditions': {
            'Meta': {'object_name': 'conditions'},
            'condition_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'operator': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'triWeb.graphs': {
            'Meta': {'object_name': 'graphs'},
            'datasets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.items']", 'symmetrical': 'False'}),
            'graph_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'triWeb.group': {
            'Meta': {'object_name': 'Group'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'template_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.templates']", 'symmetrical': 'False'})
        },
        u'triWeb.idc': {
            'Meta': {'object_name': 'Idc'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'triWeb.ip': {
            'Meta': {'object_name': 'IP'},
            'belongs_to': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['triWeb.trunk_servers']", 'null': 'True', 'blank': 'True'}),
            'custom_services': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.services']", 'symmetrical': 'False'}),
            'display_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['triWeb.Group']", 'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['triWeb.Idc']", 'null': 'True', 'blank': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'unique': 'True', 'max_length': '15'}),
            'os': ('django.db.models.fields.CharField', [], {'default': "'linux'", 'max_length': '20'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': "'22'"}),
            'snmp_auth_protocol': ('django.db.models.fields.CharField', [], {'default': "'MD5'", 'max_length': '50'}),
            'snmp_community_name': ('django.db.models.fields.CharField', [], {'default': "'public'", 'max_length': '50'}),
            'snmp_on': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'snmp_pass': ('django.db.models.fields.CharField', [], {'default': "'my_pass'", 'max_length': '50'}),
            'snmp_security_level': ('django.db.models.fields.CharField', [], {'default': "'auth'", 'max_length': '50'}),
            'snmp_user': ('django.db.models.fields.CharField', [], {'default': "'triaquae_snmp'", 'max_length': '50'}),
            'snmp_version': ('django.db.models.fields.CharField', [], {'default': "'2c'", 'max_length': '10'}),
            'status_monitor_on': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'template_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.templates']", 'symmetrical': 'False'})
        },
        u'triWeb.items': {
            'Meta': {'object_name': 'items'},
            'data_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'unit': ('django.db.models.fields.CharField', [], {'default': "'%'", 'max_length': '30'})
        },
        u'triWeb.operations': {
            'Meta': {'object_name': 'operations'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notice_interval': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'notice_times': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'send_to_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.Group']", 'symmetrical': 'False'}),
            'send_to_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.TriaquaeUser']", 'symmetrical': 'False'}),
            'send_via': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'triWeb.opslog': {
            'Meta': {'object_name': 'OpsLog'},
            'cmd': ('django.db.models.fields.TextField', [], {}),
            'failed_num': ('django.db.models.fields.IntegerField', [], {}),
            'finish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'run_user': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'success_num': ('django.db.models.fields.IntegerField', [], {}),
            'total_task': ('django.db.models.fields.IntegerField', [], {}),
            'track_mark': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'tri_user': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'triWeb.opslogtemp': {
            'Meta': {'object_name': 'OpsLogTemp'},
            'cmd': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event_log': ('django.db.models.fields.TextField', [], {}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'default': "'unknown'", 'max_length': '30'}),
            'track_mark': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'triWeb.plugins': {
            'Meta': {'object_name': 'plugins'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'plugin_file_name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'triWeb.quicklink': {
            'Meta': {'object_name': 'QuickLink'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'triWeb.remoteuser': {
            'Meta': {'object_name': 'RemoteUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'triWeb.serverstatus': {
            'Meta': {'object_name': 'ServerStatus'},
            'attempt_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'availability': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '20'}),
            'breakdown_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'host': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'primary_key': 'True'}),
            'host_status': ('django.db.models.fields.CharField', [], {'default': "'Unkown'", 'max_length': '10'}),
            'host_uptime': ('django.db.models.fields.CharField', [], {'default': "'Unkown'", 'max_length': '50'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_check': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '100'}),
            'ping_status': ('django.db.models.fields.CharField', [], {'default': "'Unkown'", 'max_length': '100'}),
            'snmp_alert_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'triWeb.services': {
            'Meta': {'object_name': 'services'},
            'check_interval': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.items']", 'symmetrical': 'False'}),
            'monitor_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'plugin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['triWeb.plugins']"}),
            'trigger_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.triggers']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'triWeb.templates': {
            'Meta': {'object_name': 'templates'},
            'graph_list': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['triWeb.graphs']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'service_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.services']", 'symmetrical': 'False'})
        },
        u'triWeb.triaquaeuser': {
            'Meta': {'object_name': 'TriaquaeUser'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['triWeb.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['triWeb.IP']", 'null': 'True', 'blank': 'True'}),
            'remoteuser': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['triWeb.RemoteUser']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'triWeb.triggers': {
            'Meta': {'object_name': 'triggers'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'expression': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'serverity': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'triWeb.trunk_servers': {
            'Meta': {'object_name': 'trunk_servers'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '9998'})
        }
    }

    complete_apps = ['triWeb']