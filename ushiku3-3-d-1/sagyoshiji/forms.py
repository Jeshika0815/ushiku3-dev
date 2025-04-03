from django import forms
from django.forms.models import inlineformset_factory
from .models import WorkOrder, WorkOrderProgress

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = [
            'work_order_number', 'release_date', 'work_number', 'work_trenum', 'subject', 
            'process_pattern', 'manager', 'work_group', 'work_hours', 
            'next_process', 'start_date', 'end_date', 'work_type', 'work_range', 'planed_value',
            'syounin_check', 'publish_check', 'workset_check', 'buy_check', 'recive_check',
        ]
        labels = {
            'work_order_number': '作業指示票番号 <必須>',
            'release_date': '発行日 <必須>',
            'work_number': '工番 <必須>',
            'work_trenum': '枝番 <必須>',
            'subject': '件名 <必須>',
            'process_pattern': '製造工程パタン <必須>',
            'manager': '製造管理担当者 <必須>',
            'work_group': '製作グループ <必須>',
            'work_hours': '作業工数時間 <必須>',
            'next_process': '次工程 <必須>',
            'start_date': '作業開始日 <必須>',
            'end_date': '終了予定日 <必須>',
            'work_type': 'FB・PL <必須>',
            'work_range': '作業範囲 <必須>',
            'planed_value': '計画数 <必須>',
            'syounin_check': '承認',
            'publish_check': '作成',
            'workset_check': '工数設定',
            'buy_check': '購買確認',
            'recive_check': '受け取り確認',
        }
        widgets = {
            'release_date': forms.TextInput(attrs={'type': 'date'}),
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'end_date': forms.TextInput(attrs={'type': 'date'}),
            'work_range': forms.Textarea(attrs={'resize':'none'}),
            'syounin_check' : forms.TextInput(attrs={'placeholder': '例) 2025/3/10 吉川 将暉'}),
            'publish_check' : forms.TextInput(attrs={'placeholder': '例) 2025/3/11 吉川 将暉'}),
            'workset_check' : forms.TextInput(attrs={'placeholder': '例) 2025/3/12 吉川 将暉'}),
            'buy_check' : forms.TextInput(attrs={'placeholder': '例) 2025/3/13 吉川 将暉'}),
            'recive_check' : forms.TextInput(attrs={'placeholder': '例) 2025/3/14 吉川 将暉'}),
            'work_order_number' : forms.TextInput(attrs={'class': 'sel'}),
            'work_hours' : forms.TextInput(attrs={'class':'sel'}),
        }




# 作業進捗用のフォームßセット
WorkOrderProgressFormSet = inlineformset_factory(
    WorkOrder, WorkOrderProgress,
    fields=('work_date', 'daily_result', ),
    widgets={
        'work_date': forms.TextInput(attrs={'type': 'date'}),
    },
    extra=12,  # 12個分のフォームを表示
    max_num=12,
    can_delete=False
)
