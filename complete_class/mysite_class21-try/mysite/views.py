import datetime
from django.shortcuts import render_to_response,get_object_or_404  #不使用render，改使用render_to_response
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from read_statistics.utils import get_seven_days_read_data
from blog.models import Blog

def get_days_hot_blogs(delta_with_startday_deadline,delta_with_deadline_today):
    today = timezone.now().date()
    deadline = today - datetime.timedelta(days=delta_with_deadline_today)
    startday = deadline - datetime.timedelta(days=delta_with_startday_deadline)
    blogs = Blog.objects \
                .filter(read_details__date__gte=startday, read_details__date__lte=deadline) \
                .values('id', 'title') \
                .annotate(read_num_sum=Sum('read_details__read_num')) \
                .order_by('-read_num_sum')
    return blogs[:7]

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    context['today_hot_data'] = get_days_hot_blogs(0,0)
    #context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_days_hot_blogs(0,1)
    context['hot_blogs_for_7_days'] = get_days_hot_blogs(7,0)
    return render_to_response('home.html',context)