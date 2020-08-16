from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course
from .forms import CourseModelForm
# Create your views here.

class CourseObjectMixin(object):
    model = Course
    lookup = 'my_id'
    def get_object(self):
        my_id    = self.kwargs.get(self.lookup)
        obj = None
        if my_id is not None:
            obj = get_object_or_404(self.model, id=my_id)
        return obj

class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'

    def get(self, request, id=None, *args, **kwargs):
        # form = CourseModelForm()
        context = {} 
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = obj
            redirect('/courses/')
        return render(request, self.template_name, context)

class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'

    def get(self, request, id=None, *args, **kwargs):
        # form = CourseModelForm()
        context = {} 
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {"form":form} 
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form":form} 
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset    

    def get(self, request, *args, **kwargs):
        context = {"object_list":self.get_queryset()}
        return render(request, self.template_name, context)

class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'
    def get(self, request, my_id=None, *args, **kwargs):
        obj = self.get_object() #get_object_or_404(Course, id=my_id)
        context = {"object":obj} 
        return render(request, self.template_name, context)

# class CourseView(View):
#     template_name = 'courses/about.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, {})


def my_fbv(request, *args, **kwargs):
    print ('C')
    return render(request, 'courses/about.html', {})