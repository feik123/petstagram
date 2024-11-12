from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.template.defaulttags import comment
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoAddForm, PhotoEditForm, PhotoDeleteForm
from petstagram.photos.models import Photo


class PhotoAddPage(CreateView):
    model = Photo
    form_class = PhotoAddForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home')

# def photo_add_page(request):
#     form = PhotoAddForm(request.POST or None, request.FILES or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'photos/photo-add-page.html', context)


class PhotoEditPage(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self,):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})

# def photo_edit_page(request, pk:int):
#     photo = Photo.objects.get(pk=pk)
#     form = PhotoEditForm(request.POST or None, instance=photo)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('photo-details', pk)
#
#     context = {
#         'form': form,
#         'photo': photo,
#     }
#
#     return render(request, 'photos/photo-edit-page.html', context)

class PhotoDetailsPage(DeleteView):
    model = Photo
    form_class = PhotoDeleteForm
    template_name = 'photos/photo-details-page.html'

    # context_object_name = 'photo' # default is photo or/and object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['likes'] = self.object.like_set.all()
        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = CommentForm()

        return context

    # def photo_details_page(request, pk:int):
    #     photo = Photo.objects.get(pk=pk)
    #     likes = photo.like_set.all()
    #     comments = photo.comment_set.all()
    #
    #     comment_form = CommentForm()
    #
    #     context = {
    #         'photo': photo,
    #         'likes': likes,
    #         'comments': comments,
    #         'comment_form': comment_form,
    #     }
    #
    #     return render(request, 'photos/photo-details-page.html', context=context)


def photo_delete_page(request, pk:int):
    Photo.objects.get(pk=pk).delete()
    return redirect('home')
