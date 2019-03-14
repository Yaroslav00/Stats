from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView,Response
from .serializers import UserSerializer, GroupSerializer, PointSerializer
from .statistic_algorithms import simple_linear_regretion
from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class linear_regretion(APIView):


    def get(self,request):
        points = request.GET.get('test_points')
        test_points = []
        for i in points:
            point = PointSerializer(points[i])
            test_points.append(point)
        new_point = request.GET.get('new_points')
        test_points.sort()
        alpha, beta, y = simple_linear_regretion.main(test_points, new_point)
        chart_x = [beta*point.x + alpha for point in test_points]
        chart_y = [point.y for point in test_points]
        prediction_y = y
        return Response({'chart_x': chart_x, 'chart_y': chart_y, 'prediction_y': prediction_y})


class main_page(APIView):


    def get(self,request):

        return render(request,'../templates/Index.html')






