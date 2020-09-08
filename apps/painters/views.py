from django.shortcuts import render
from django.views.generic import TemplateView

from apps.accounts.mixins import LoggedInRequiredMixin
from .models import Painter
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from .forms import UploadFileForm
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.messages import get_messages
from django.contrib import messages
import json


# Create your views here.
class PainterCreate(LoggedInRequiredMixin, TemplateView):
    # template_name = 'painter.html'
    template_name = 'editor_painter.html'

    def get_context_data(self, **kwargs):
        context = super(PainterCreate, self).get_context_data(**kwargs)
        projects = Painter.get_all(self.request)
        context['projects'] = projects

        storage = get_messages(self.request)
        kv = None
        for message in storage:
            kv = message
            break
        # parse
        if kv:
            kv = kv.message
            kv_dict = json.loads(kv)
            context.update(kv_dict)
        return context


class CreateProject(LoggedInRequiredMixin, CreateView):

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        if not name:
            return HttpResponseBadRequest()
        try:
            user = request.user
            p = Painter(name=name, user=user)
            p.save()
        except:
            import traceback
            return HttpResponseServerError(traceback.format_exc())

        return HttpResponse(content='Created project `{0}`.'.format(name))


class UploadFile(LoggedInRequiredMixin, FormView):
    template_name = 'editor_painter.html'

    def post(self, request, *args, **kwargs):
        content = request.FILES['file']
        filename = request.FILES['file'].name
        with open(filename, 'wb') as f:
            for chunk in content.chunks():
                f.write(chunk)
        context = {
            'upload_success': True,
            'hide_upload_dialog': True,
        }
        messages.add_message(request, messages.INFO, json.dumps(context))
        return redirect('/painters/painter/')
