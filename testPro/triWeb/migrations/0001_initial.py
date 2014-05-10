# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Idc'
        db.create_table(u'triWeb_idc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'triWeb', ['Idc'])

        # Adding model 'Group'
        db.create_table(u'triWeb_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'triWeb', ['Group'])

        # Adding M2M table for field template_list on 'Group'
        m2m_table_name = db.shorten_name(u'triWeb_group_template_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm[u'triWeb.group'], null=False)),
            ('templates', models.ForeignKey(orm[u'triWeb.templates'], null=False))
        ))
        db.create_unique(m2m_table_name, ['group_id', 'templates_id'])

        # Adding model 'IP'
        db.create_table(u'triWeb_ip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('display_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(unique=True, max_length=15)),
            ('idc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['triWeb.Idc'], null=True, blank=True)),
            ('port', self.gf('django.db.models.fields.IntegerField')(default='22')),
            ('os', self.gf('django.db.models.fields.CharField')(default='linux', max_length=20)),
            ('alert_limit', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('snmp_alert_limit', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('asset_collection', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('status_monitor_on', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('snmp_on', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('snmp_version', self.gf('django.db.models.fields.CharField')(default='2c', max_length=10)),
            ('snmp_community_name', self.gf('django.db.models.fields.CharField')(default='public', max_length=50)),
            ('snmp_security_level', self.gf('django.db.models.fields.CharField')(default='auth', max_length=50)),
            ('snmp_auth_protocol', self.gf('django.db.models.fields.CharField')(default='MD5', max_length=50)),
            ('snmp_user', self.gf('django.db.models.fields.CharField')(default='triaquae_snmp', max_length=50)),
            ('snmp_pass', self.gf('django.db.models.fields.CharField')(default='my_pass', max_length=50)),
            ('system_load_warning', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('system_load_critical', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('cpu_idle_warning', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('cpu_idle_critical', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('mem_usage_warning', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('mem_usage_critical', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'triWeb', ['IP'])

        # Adding M2M table for field group on 'IP'
        m2m_table_name = db.shorten_name(u'triWeb_ip_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ip', models.ForeignKey(orm[u'triWeb.ip'], null=False)),
            ('group', models.ForeignKey(orm[u'triWeb.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ip_id', 'group_id'])

        # Adding M2M table for field template_list on 'IP'
        m2m_table_name = db.shorten_name(u'triWeb_ip_template_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ip', models.ForeignKey(orm[u'triWeb.ip'], null=False)),
            ('templates', models.ForeignKey(orm[u'triWeb.templates'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ip_id', 'templates_id'])

        # Adding model 'RemoteUser'
        db.create_table(u'triWeb_remoteuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'triWeb', ['RemoteUser'])

        # Adding model 'TriaquaeUser'
        db.create_table(u'triWeb_triaquaeuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'triWeb', ['TriaquaeUser'])

        # Adding M2M table for field remoteuser on 'TriaquaeUser'
        m2m_table_name = db.shorten_name(u'triWeb_triaquaeuser_remoteuser')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('triaquaeuser', models.ForeignKey(orm[u'triWeb.triaquaeuser'], null=False)),
            ('remoteuser', models.ForeignKey(orm[u'triWeb.remoteuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['triaquaeuser_id', 'remoteuser_id'])

        # Adding M2M table for field group on 'TriaquaeUser'
        m2m_table_name = db.shorten_name(u'triWeb_triaquaeuser_group')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('triaquaeuser', models.ForeignKey(orm[u'triWeb.triaquaeuser'], null=False)),
            ('group', models.ForeignKey(orm[u'triWeb.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['triaquaeuser_id', 'group_id'])

        # Adding M2M table for field ip on 'TriaquaeUser'
        m2m_table_name = db.shorten_name(u'triWeb_triaquaeuser_ip')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('triaquaeuser', models.ForeignKey(orm[u'triWeb.triaquaeuser'], null=False)),
            ('ip', models.ForeignKey(orm[u'triWeb.ip'], null=False))
        ))
        db.create_unique(m2m_table_name, ['triaquaeuser_id', 'ip_id'])

        # Adding model 'AuthByIpAndRemoteUser'
        db.create_table(u'triWeb_authbyipandremoteuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('authtype', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['triWeb.IP'], null=True, blank=True)),
            ('remoteUser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['triWeb.RemoteUser'], null=True, blank=True)),
        ))
        db.send_create_signal(u'triWeb', ['AuthByIpAndRemoteUser'])

        # Adding unique constraint on 'AuthByIpAndRemoteUser', fields ['ip', 'remoteUser']
        db.create_unique(u'triWeb_authbyipandremoteuser', ['ip_id', 'remoteUser_id'])

        # Adding model 'ServerStatus'
        db.create_table(u'triWeb_serverstatus', (
            ('host', self.gf('django.db.models.fields.IPAddressField')(max_length=15, primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('host_status', self.gf('django.db.models.fields.CharField')(default='Unkown', max_length=10)),
            ('ping_status', self.gf('django.db.models.fields.CharField')(default='Unkown', max_length=100)),
            ('last_check', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=100)),
            ('host_uptime', self.gf('django.db.models.fields.CharField')(default='Unkown', max_length=50)),
            ('attempt_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('breakdown_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('up_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('snmp_alert_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('availability', self.gf('django.db.models.fields.CharField')(default=0, max_length=20)),
        ))
        db.send_create_signal(u'triWeb', ['ServerStatus'])

        # Adding model 'OpsLog'
        db.create_table(u'triWeb_opslog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('finish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('log_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tri_user', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('run_user', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cmd', self.gf('django.db.models.fields.TextField')()),
            ('total_task', self.gf('django.db.models.fields.IntegerField')()),
            ('success_num', self.gf('django.db.models.fields.IntegerField')()),
            ('failed_num', self.gf('django.db.models.fields.IntegerField')()),
            ('track_mark', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'triWeb', ['OpsLog'])

        # Adding model 'OpsLogTemp'
        db.create_table(u'triWeb_opslogtemp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cmd', self.gf('django.db.models.fields.TextField')()),
            ('event_log', self.gf('django.db.models.fields.TextField')()),
            ('result', self.gf('django.db.models.fields.CharField')(default='unknown', max_length=30)),
            ('track_mark', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'triWeb', ['OpsLogTemp'])

        # Adding model 'QuickLink'
        db.create_table(u'triWeb_quicklink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'triWeb', ['QuickLink'])

        # Adding model 'templates'
        db.create_table(u'triWeb_templates', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'triWeb', ['templates'])

        # Adding M2M table for field service_list on 'templates'
        m2m_table_name = db.shorten_name(u'triWeb_templates_service_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('templates', models.ForeignKey(orm[u'triWeb.templates'], null=False)),
            ('services', models.ForeignKey(orm[u'triWeb.services'], null=False))
        ))
        db.create_unique(m2m_table_name, ['templates_id', 'services_id'])

        # Adding M2M table for field graph_list on 'templates'
        m2m_table_name = db.shorten_name(u'triWeb_templates_graph_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('templates', models.ForeignKey(orm[u'triWeb.templates'], null=False)),
            ('graphs', models.ForeignKey(orm[u'triWeb.graphs'], null=False))
        ))
        db.create_unique(m2m_table_name, ['templates_id', 'graphs_id'])

        # Adding model 'services'
        db.create_table(u'triWeb_services', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('check_interval', self.gf('django.db.models.fields.IntegerField')(default=300)),
        ))
        db.send_create_signal(u'triWeb', ['services'])

        # Adding M2M table for field item_list on 'services'
        m2m_table_name = db.shorten_name(u'triWeb_services_item_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('services', models.ForeignKey(orm[u'triWeb.services'], null=False)),
            ('items', models.ForeignKey(orm[u'triWeb.items'], null=False))
        ))
        db.create_unique(m2m_table_name, ['services_id', 'items_id'])

        # Adding model 'items'
        db.create_table(u'triWeb_items', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('monitor_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('data_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('unit', self.gf('django.db.models.fields.CharField')(default='%', max_length=30)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'triWeb', ['items'])

        # Adding model 'triggers'
        db.create_table(u'triWeb_triggers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('expression', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('serverity', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'triWeb', ['triggers'])

        # Adding model 'graphs'
        db.create_table(u'triWeb_graphs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('graph_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'triWeb', ['graphs'])

        # Adding M2M table for field datasets on 'graphs'
        m2m_table_name = db.shorten_name(u'triWeb_graphs_datasets')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('graphs', models.ForeignKey(orm[u'triWeb.graphs'], null=False)),
            ('items', models.ForeignKey(orm[u'triWeb.items'], null=False))
        ))
        db.create_unique(m2m_table_name, ['graphs_id', 'items_id'])

        # Adding model 'actions'
        db.create_table(u'triWeb_actions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('recovery_notice', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('recovery_subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('recovery_message', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'triWeb', ['actions'])

        # Adding M2M table for field condition_list on 'actions'
        m2m_table_name = db.shorten_name(u'triWeb_actions_condition_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actions', models.ForeignKey(orm[u'triWeb.actions'], null=False)),
            ('conditions', models.ForeignKey(orm[u'triWeb.conditions'], null=False))
        ))
        db.create_unique(m2m_table_name, ['actions_id', 'conditions_id'])

        # Adding M2M table for field operation_list on 'actions'
        m2m_table_name = db.shorten_name(u'triWeb_actions_operation_list')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actions', models.ForeignKey(orm[u'triWeb.actions'], null=False)),
            ('operations', models.ForeignKey(orm[u'triWeb.operations'], null=False))
        ))
        db.create_unique(m2m_table_name, ['actions_id', 'operations_id'])

        # Adding model 'conditions'
        db.create_table(u'triWeb_conditions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('condition_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('operator', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'triWeb', ['conditions'])

        # Adding model 'operations'
        db.create_table(u'triWeb_operations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('send_via', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('notice_times', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('notice_interval', self.gf('django.db.models.fields.IntegerField')(default=300)),
        ))
        db.send_create_signal(u'triWeb', ['operations'])

        # Adding M2M table for field send_to_users on 'operations'
        m2m_table_name = db.shorten_name(u'triWeb_operations_send_to_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('operations', models.ForeignKey(orm[u'triWeb.operations'], null=False)),
            ('triaquaeuser', models.ForeignKey(orm[u'triWeb.triaquaeuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['operations_id', 'triaquaeuser_id'])

        # Adding M2M table for field send_to_groups on 'operations'
        m2m_table_name = db.shorten_name(u'triWeb_operations_send_to_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('operations', models.ForeignKey(orm[u'triWeb.operations'], null=False)),
            ('group', models.ForeignKey(orm[u'triWeb.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['operations_id', 'group_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'AuthByIpAndRemoteUser', fields ['ip', 'remoteUser']
        db.delete_unique(u'triWeb_authbyipandremoteuser', ['ip_id', 'remoteUser_id'])

        # Deleting model 'Idc'
        db.delete_table(u'triWeb_idc')

        # Deleting model 'Group'
        db.delete_table(u'triWeb_group')

        # Removing M2M table for field template_list on 'Group'
        db.delete_table(db.shorten_name(u'triWeb_group_template_list'))

        # Deleting model 'IP'
        db.delete_table(u'triWeb_ip')

        # Removing M2M table for field group on 'IP'
        db.delete_table(db.shorten_name(u'triWeb_ip_group'))

        # Removing M2M table for field template_list on 'IP'
        db.delete_table(db.shorten_name(u'triWeb_ip_template_list'))

        # Deleting model 'RemoteUser'
        db.delete_table(u'triWeb_remoteuser')

        # Deleting model 'TriaquaeUser'
        db.delete_table(u'triWeb_triaquaeuser')

        # Removing M2M table for field remoteuser on 'TriaquaeUser'
        db.delete_table(db.shorten_name(u'triWeb_triaquaeuser_remoteuser'))

        # Removing M2M table for field group on 'TriaquaeUser'
        db.delete_table(db.shorten_name(u'triWeb_triaquaeuser_group'))

        # Removing M2M table for field ip on 'TriaquaeUser'
        db.delete_table(db.shorten_name(u'triWeb_triaquaeuser_ip'))

        # Deleting model 'AuthByIpAndRemoteUser'
        db.delete_table(u'triWeb_authbyipandremoteuser')

        # Deleting model 'ServerStatus'
        db.delete_table(u'triWeb_serverstatus')

        # Deleting model 'OpsLog'
        db.delete_table(u'triWeb_opslog')

        # Deleting model 'OpsLogTemp'
        db.delete_table(u'triWeb_opslogtemp')

        # Deleting model 'QuickLink'
        db.delete_table(u'triWeb_quicklink')

        # Deleting model 'templates'
        db.delete_table(u'triWeb_templates')

        # Removing M2M table for field service_list on 'templates'
        db.delete_table(db.shorten_name(u'triWeb_templates_service_list'))

        # Removing M2M table for field graph_list on 'templates'
        db.delete_table(db.shorten_name(u'triWeb_templates_graph_list'))

        # Deleting model 'services'
        db.delete_table(u'triWeb_services')

        # Removing M2M table for field item_list on 'services'
        db.delete_table(db.shorten_name(u'triWeb_services_item_list'))

        # Deleting model 'items'
        db.delete_table(u'triWeb_items')

        # Deleting model 'triggers'
        db.delete_table(u'triWeb_triggers')

        # Deleting model 'graphs'
        db.delete_table(u'triWeb_graphs')

        # Removing M2M table for field datasets on 'graphs'
        db.delete_table(db.shorten_name(u'triWeb_graphs_datasets'))

        # Deleting model 'actions'
        db.delete_table(u'triWeb_actions')

        # Removing M2M table for field condition_list on 'actions'
        db.delete_table(db.shorten_name(u'triWeb_actions_condition_list'))

        # Removing M2M table for field operation_list on 'actions'
        db.delete_table(db.shorten_name(u'triWeb_actions_operation_list'))

        # Deleting model 'conditions'
        db.delete_table(u'triWeb_conditions')

        # Deleting model 'operations'
        db.delete_table(u'triWeb_operations')

        # Removing M2M table for field send_to_users on 'operations'
        db.delete_table(db.shorten_name(u'triWeb_operations_send_to_users'))

        # Removing M2M table for field send_to_groups on 'operations'
        db.delete_table(db.shorten_name(u'triWeb_operations_send_to_groups'))


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
            'alert_limit': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'asset_collection': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cpu_idle_critical': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'cpu_idle_warning': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['triWeb.Group']", 'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['triWeb.Idc']", 'null': 'True', 'blank': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'unique': 'True', 'max_length': '15'}),
            'mem_usage_critical': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'mem_usage_warning': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'os': ('django.db.models.fields.CharField', [], {'default': "'linux'", 'max_length': '20'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': "'22'"}),
            'snmp_alert_limit': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'snmp_auth_protocol': ('django.db.models.fields.CharField', [], {'default': "'MD5'", 'max_length': '50'}),
            'snmp_community_name': ('django.db.models.fields.CharField', [], {'default': "'public'", 'max_length': '50'}),
            'snmp_on': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'snmp_pass': ('django.db.models.fields.CharField', [], {'default': "'my_pass'", 'max_length': '50'}),
            'snmp_security_level': ('django.db.models.fields.CharField', [], {'default': "'auth'", 'max_length': '50'}),
            'snmp_user': ('django.db.models.fields.CharField', [], {'default': "'triaquae_snmp'", 'max_length': '50'}),
            'snmp_version': ('django.db.models.fields.CharField', [], {'default': "'2c'", 'max_length': '10'}),
            'status_monitor_on': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'system_load_critical': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'system_load_warning': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'template_list': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['triWeb.templates']", 'symmetrical': 'False'})
        },
        u'triWeb.items': {
            'Meta': {'object_name': 'items'},
            'data_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'monitor_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
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
        }
    }

    complete_apps = ['triWeb']