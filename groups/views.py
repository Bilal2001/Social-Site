from audioop import reverse
from email import message
from tokenize import group
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, RedirectView
from .models import Group, GroupMember
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages

# Create your views here.
class GroupList(ListView):
    model = Group

class GroupCreate(LoginRequiredMixin, CreateView):
    fields = ["name", "desc"]
    model = Group

class GroupDetail(DetailView):
    model = Group

class GroupJoin(LoginRequiredMixin, RedirectView):
    # model = Group
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:detail', kwargs={'slug' : self.kwargs.get('slug')})
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug = self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user = self.request.user, group = group)
        except:
            messages.warning(request, message = f'{self.request.user} is Already a Member')
        else:
            messages.success(request, message = f'{self.request.user} is Added Successfully')
        return super().get(request, args, kwargs)

class GroupLeave(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:detail', kwargs={'slug' : self.kwargs.get('slug')})
    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(user = self.request.user, group__slug = self.kwargs.get('slug')).get()
        except:
            messages.warning(request, message = f'{self.request.user} is Not a Member')
        else:
            membership.delete()
            messages.success(request, message = f'{self.request.user} is Removed Successfully')
        return super().get(request, args, kwargs)