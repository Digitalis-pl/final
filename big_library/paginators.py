from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class CastPaginator:
    def __init__(self, object_list, per_page, request):
        self.object_list = object_list
        self.per_page = per_page
        self.request = request

    def paginate(self):
        paginator = Paginator(self.object_list, self.per_page)
        page = self.request.GET.get('page')

        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)

        return objects
