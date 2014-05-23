from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple 
from django.contrib.auth.models import User as djangouser, Group as djangogroup
from django.contrib.sites.models import Site as djangosite
import logging.config, logging, logging.handlers

#customized module
import models
import admin_ip, admin_user, admin_auth

#admin.site.unregister(djangouser)
#admin.site.unregister(djangogroup)
#admin.site.unregister(djangosite)

from models import *




class TemplatesForm(forms.ModelForm):
    class Meta:
        model = templates
    ips = forms.ModelMultipleChoiceField(
        queryset=IP.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name= ('Ip list'),
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(TemplatesForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['ips'].initial = self.instance.ip_set.all()

    def save(self, commit=True):
        groupmachine = super(TemplatesForm, self).save(commit=False)  
        if commit:
            groupmachine.save()
        if groupmachine.pk:
            groupmachine.ip_set = self.cleaned_data['ips']
            self.save_m2m()
        return groupmachine


class TemplatesAdmin(admin.ModelAdmin):
	form = TemplatesForm

    #list_display = ('name',)

    #filter_horizontal = ('service_list','groups','hosts','graph_list')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'check_interval')
    filter_horizontal = ('item_list',)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'monitor_type','key','data_type','enabled')


class LogAdmin(admin.ModelAdmin):
    list_display = ('user','ip','event_type','cmd','event_log','result','track_mark')

class OpsLogAdmin(admin.ModelAdmin):
    list_display = ('log_type','finish_date','log_type','tri_user','run_user','cmd','total_task','success_num','failed_num','track_mark','note')

class StatusAdmin(admin.ModelAdmin):
    search_fields = ('host','host_status')
    list_display = ('host','host_status','ping_status','availability','host_uptime','breakdown_count','up_count','attempt_count')

class QuickLinkAdmin(admin.ModelAdmin):
	list_display = ('link_name','url','color')
#class GroupAdmin(admin.ModelAdmin):
#    form = GroupForm
admin.site.register(Idc)
admin.site.register(IP, admin_ip.IpAdmin)
admin.site.register(Group, admin_ip.GroupAdmin)
admin.site.register(RemoteUser, admin_user.RemoteUserAdmin)
admin.site.register(TriaquaeUser, admin_user.TriaquaeUserAdmin)
admin.site.register(AuthByIpAndRemoteUser, admin_auth.AuthByIpAndRemoteUserAdmin)
admin.site.register(ServerStatus,StatusAdmin)

admin.site.register(templates,TemplatesAdmin)
admin.site.register(services,ServicesAdmin)
admin.site.register(items,ItemsAdmin)
admin.site.register(triggers)
admin.site.register(graphs)
admin.site.register(operations)
admin.site.register(conditions)
admin.site.register(actions)

admin.site.register(OpsLogTemp,LogAdmin)
admin.site.register(OpsLog,OpsLogAdmin)
admin.site.register(QuickLink,QuickLinkAdmin)
