from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm
from setting.models import Setting
from django.contrib import messages


# Create your views here.

class ContactUs(CreateView):
    template_name = 'contact/contact_us.html'
    model = Contact
    form_class = ContactForm
    setting = Setting.objects.last()
    extra_context = {
        'setting': setting,
    }

    success_url = reverse_lazy('shop:home')

    def form_valid(self, form):
        messages.success(self.request, 'پیام شما با موفقیت ارسال شد', 'success')
        return super(ContactUs, self).form_valid(form)