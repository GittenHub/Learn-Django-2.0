from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput) # HiddenInput在前端隐藏显示
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(widget=CKEditorWidget(config_name='comment_ckeditor'),
                           error_messages={'required':'评论内容不能为空'})

    # 继承forms.Form进行实例化，在这个类中隐藏一个初始化的方法
    def __init__(self, *args, **kwargs):  # *args表示任意类型的参数；**kwargs表示任意关键字的参数
        if 'user' in kwargs: # 如果'user'在kwargs中做以下操作
            self.user = kwargs.pop('user') # pop()表示将'user'的内容从kwargs中拿出来剔除，放入self.user中，防止在super初始化时有参数报错
        super(CommentForm, self).__init__(*args, **kwargs) # 继承初始化的方法

    def clean(self):
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登录')
        #评论对象验证
        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        try:
            model_class = ContentType.objects.get(model=content_type).model_class()
            # 使用ContentType进行处理，根据'content_type'得到blog等对象类型,ContentType.objects.get获得一个外键关联的具体的blog对象
            # 使用model_class方法，可以得到具体的模型的class, 也就是得到Blog；使用model_class方法，可以根据一个具体的object对象，返回这个对象所属的class类
            model_obj = model_class.objects.get(pk=object_id)
            self.cleaned_data['content_object'] = model_obj
        except ObjectDoesNotExist:
            raise forms.ValidationError('评论不存在')
        return self.cleaned_data