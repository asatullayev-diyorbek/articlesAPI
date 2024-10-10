from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Hotel, Class, Travel
from .serializers import HotelSerializer, ClassSerializer, TravelSerializer


class HotelListView(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        hotels_serializer = HotelSerializer(hotels, many=True, context={'request': request})
        return Response({'hotels': hotels_serializer.data})

    def post(self, request):
        hotel_serializer = HotelSerializer(data=request.data)
        if hotel_serializer.is_valid():
            new_hotel = hotel_serializer.create(hotel_serializer.validated_data)
            return Response({'status': 'success', 'message': 'Ma\'lumot qo\'shildi', 'data': ClassSerializer(new_hotel).data})
        else:
            return Response(hotel_serializer.errors, status=400)


class HotelDetailView(APIView):
    def get(self, request, pk=None):
        try:
            hotel = Hotel.objects.get(id=pk)
            hotel_serializer = HotelSerializer(hotel, context={'request': request})
            return Response(hotel_serializer.data)
        except Hotel.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def put(self, request, pk=None):
        try:
            hotel = Hotel.objects.get(id=pk)
            hotel_serializer = HotelSerializer(hotel, data=request.data, partial=True, context={'request': request})
            if hotel_serializer.is_valid():
                hotel_serializer.update(hotel, hotel_serializer.validated_data)
                return Response({'status': 'success', 'message': 'Ma\'lumot yangilandi', 'data': hotel_serializer.data})
            else:
                return Response({'status': 'error', 'message': hotel_serializer.errors}, status=400)
        except Hotel.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def delete(self, request, pk=None):
        try:
            hotel = Hotel.objects.get(id=pk)
            hotel.delete()
            return Response({'status': 'success', 'message': 'Ma\'lumot o\'chirildi'})
        except Hotel.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)


class ClassListView(APIView):
    def get(self, request):
        classes = Class.objects.all()
        classes_serializer = ClassSerializer(classes, many=True)
        return Response(classes_serializer.data)

    def post(self, request):
        class_serializer = ClassSerializer(data=request.data)
        if class_serializer.is_valid():
            new_class = class_serializer.create(class_serializer.validated_data)
            return Response({'status': 'success', 'message': 'Ma\'lumot qo\'shildi', 'data': ClassSerializer(new_class).data})
        else:
            return Response(class_serializer.errors, status=400)


class ClassDetailView(APIView):
    def get(self, request, pk=None):
        try:
            class_ = Class.objects.get(id=pk)
            class_serializer = ClassSerializer(class_)
            return Response(class_serializer.data)
        except Class.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def put(self, request, pk=None):
        try:
            class_ = Class.objects.get(id=pk)
            class_serializer = ClassSerializer(class_, data=request.data, partial=True)
            if class_serializer.is_valid():
                class_serializer.update(class_, class_serializer.validated_data)
                return Response({'status': 'success', 'message': 'Ma\'lumot yangilandi', 'data': class_serializer.data})
            else:
                return Response({'status': 'error', 'message': class_serializer.errors}, status=400)
        except Class.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def delete(self, request, pk=None):
        try:
            class_ = Class.objects.get(id=pk)
            class_.delete()
            return Response({'status': 'success', 'message': 'Ma\'lumot o\'chirildi'})
        except Class.DoesNotExist:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)


class TravelListView(APIView):
    def get(self, request):
        travels = Travel.objects.all()
        travels_serializer = TravelSerializer(travels, many=True, context={'request': request})
        return Response(travels_serializer.data)

    def post(self, request):
        travel_serializer = TravelSerializer(data=request.data)
        if travel_serializer.is_valid():
            new_travel = travel_serializer.create(travel_serializer.validated_data)
            return Response({'status': 'success', 'message': 'Ma\'lumot qo\'shildi', 'data': TravelSerializer(new_travel).data})
        else:
            return Response(travel_serializer.errors, status=400)


class TravelDetailView(APIView):
    def get(self, request, pk=None):
        try:
            travel = Travel.objects.get(id=pk)
            travel_serializer = TravelSerializer(travel)
            return Response(travel_serializer.data)
        except:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

    def put(self, request, pk=None):
        try:
            travel_serializer = TravelSerializer(data=request.data)
            if travel_serializer.is_valid():
                travel = Travel.objects.get(id=pk)
                travel_serializer.update(travel, travel_serializer.validated_data)
                return Response({'status': 'success', 'message': 'Ma\'lumot yangilandi', 'data': TravelSerializer(travel).data})
            return Response({'status': 'error', 'message': travel_serializer.errors}, status=400)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=404)

    def delete(self, request, pk=None):
        try:
            travel = Travel.objects.get(id=pk)
            travel.delete()
            return Response({'status': 'success', 'message': 'Ma\'lumot o\'chirildi'})
        except:
            return Response({'status': 'error', 'message': 'Ma\'lumot topilmadi'}, status=404)

