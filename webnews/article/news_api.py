# from .models import Aritcle,Reporter
# from .serializers import AritcleSerializer
# from .serializers import ReporterSerializer
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# @api_view(['GET'])
# def display_view(request):
#     obj=Aritcle.objects.all()
#     if obj:
#         serializer=AritcleSerializer(obj,many=True)
#         return Response(serializer.data)
#     else:
#         return Response({"message":"not found anything"})


from .models import Aritcle,Reporter
from .serializers import AritcleSerializer
from .serializers import ReporterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

@api_view(['GET'])
def api_get_one_article(request):
    obj = Aritcle.objects.first()

    if obj:
    	serializer = AritcleSerializer(obj)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Article Not Foud'})

@api_view(['GET'])
def api_all_articles(request):
    all_articles = Aritcle.objects.all()
    if all_articles:
    	serializer = AritcleSerializer(all_articles, many=True)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Article Not Foud'})


@api_view(['GET'])
def api_get_article_id(request, _id):

    obj = Aritcle.objects.filter(id = _id)[0]
    if obj:
    	serializer = AritcleSerializer(obj)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Article Not Foud'})

@api_view(['GET'])
def api_get_articles_range(request, _range):
    print('===================>',_range)

    if ',' in _range:
        ids = [int(x) for x in _range.split(',')]
        all_articles = Aritcle.objects.filter(id__in=ids)
        print(ids, len(all_articles))
    else:
        start, end = [int(x) for x in _range.split('-')]
        all_articles = Aritcle.objects.filter(Q(id__lte = end) & Q(id__gte = start))


    if all_articles:
    	serializer = AritcleSerializer(all_articles, many=True)
    	return Response(serializer.data)
    else:
    	return Response({"Message": 'Article Not Foud'})
    


@api_view(['POST'])
def api_add_article(request):
    heading = request.POST.get("heading", None)
    body = request.POST.get("body", None)
    reporter_id = request.POST.get("reporter_id", None)
    article = Aritcle.objects.create(heading=heading,
                                     body=body,
                                     reporter_id = reporter_id,
                                     image=request.FILES['image'])

    return Response({'message': 'article {:d} created'.format(article.id)}, status=301)



            




