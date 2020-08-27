from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.titulo = titulo
        self.slug = slug
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video(slug='motivacao', titulo='We are All Going To Die', vimeo_id=292711054),
    Video(slug='super-generic', titulo='Super Generic', vimeo_id=415570097)
]

videos_dct = {v.slug: v for v in videos}


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
