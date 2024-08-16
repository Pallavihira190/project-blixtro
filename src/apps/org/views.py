from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from apps.org.models import Org, Department
from apps.purchases.models import Vendor
from apps.core.models import UserProfile
from apps.org.forms import DepartmentCreateAndUpdateForm


class DepartmentListView(generic.DetailView):
    template_name = 'org/dept-list.html'
    model = Org
    
    def get_object(self, queryset=None):
        org_id = self.kwargs['org_id']
        queryset = self.get_queryset()
        return queryset.get(pk=org_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        org_id = self.kwargs["org_id"]
        org = Org.objects.get(pk=org_id)
        context["departments"] = Department.objects.filter(org=org)
        return context


class DepartmentCreateView(generic.CreateView):
    template_name = "org/dept-create.html"
    model = Department
    form_class = DepartmentCreateAndUpdateForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["org_id"] = self.kwargs["org_id"]
        return context
    
    def form_valid(self, form):
        dept = form.save(commit=False)
        org = self.request.user.profile.org
        dept.org = org
        dept.save()
        department_head = dept.head
        department_head.dept = dept
        department_head.is_dept_incharge = True
        department_head.save()
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["head"].queryset = UserProfile.objects.filter(org=self.request.user.profile.org, is_dept_incharge=True)
        return form
    
    def get_success_url(self):
        org_id = self.kwargs['org_id']
        return reverse('org:dept-list', kwargs={'org_id':org_id})


class OrgPeopleListView(generic.ListView):
    model = UserProfile
    template_name = 'core/org-people-list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        org = Org.objects.get(pk = self.kwargs["org_id"])
        org_people = UserProfile.objects.filter(org=org)
        context["org_people"] = org_people
        context["org"] = org
        return context


class DepartmentUpdateView(generic.UpdateView):
    model = Department
    template_name = 'org/dept-update.html'
    form_class = DepartmentCreateAndUpdateForm
    
    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        return queryset.get(pk=self.kwargs["dept_id"])
    
    def get_success_url(self):
        org_id = self.request.user.profile.org.pk
        return reverse('org:dept-list', kwargs={'org_id':org_id})


class DepartmentDeleteView(generic.DeleteView):
    model = Department

    def get(self, *args, **kwargs):
        dept = get_object_or_404(Department, pk=self.kwargs["dept_id"])
        dept.delete()
        org_id = self.request.user.profile.org.pk
        return HttpResponsePermanentRedirect(
            reverse(
                'org:dept-list', 
                kwargs={
                    'org_id':org_id
                    }
                )
            )


class AdminVendorsListView(generic.ListView):
    model = Vendor
    template_name = 'org/vendors-list.html'
    context_object_name = 'vendors'
    
    def get_queryset(self):
        return Vendor.objects.filter(org=self.request.user.profile.org)
    