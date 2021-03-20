import datetime
import json

from django.db.models import F, Case, When
from django.http import HttpResponse, JsonResponse
from NavigationApp.models import NavigationRecord, Vehicle

# Create your views here.

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_last_points(request):
    if request.method == 'POST':
        return JsonResponse({}, status=405)

    date_from = datetime.datetime.now() - datetime.timedelta(days=2)
    vehicles = Vehicle.objects.all()
    navigation_record_list = []
    for v in vehicles:
        navigation_record = NavigationRecord.objects.filter(datetime__gte=date_from, vehicle=v).order_by(
            '-datetime').values(
            'latitude', 'longitude', 'datetime', vehicle_plate=F('vehicle__plate')).first()

        if navigation_record:
            navigation_record_list.append(navigation_record)
    if len(navigation_record_list):
        return JsonResponse({"last_points": list(navigation_record_list)})
    return JsonResponse({}, status=204)


@csrf_exempt
def bulk_create_vehicles(request):
    if request.method != 'POST':
        return JsonResponse({}, status=405)
    data = json.loads(request.body)

    if "vehicles" not in data:
        return JsonResponse({"error": "Request body should contain vehicles array!"}, status=400)

    for v in data["vehicles"]:
        try:
            Vehicle.objects.get_or_create(plate=v["plate"])
        except Exception as e:
            return JsonResponse({"error": repr(e)}, status=400)
    return JsonResponse({}, status=200)


@csrf_exempt
def bulk_create_navigation_record(request):
    if request.method != 'POST':
        return JsonResponse({}, status=405)
    data = json.loads(request.body)

    if "navigation_records" not in data:
        return JsonResponse({"error": "Request body should contain navigation_records array!"}, status=400)

    errors = []
    created = []
    for v in data["navigation_records"]:
        try:
            vehicle = Vehicle.objects.get(plate=v["vehicle_plate"])
            navigation_record = NavigationRecord.objects.create(latitude=v["latitude"],
                                                                longitude=v["longitude"],
                                                                vehicle=vehicle,
                                                                datetime=v["datetime"]
                                                                )
            created.append({"latitude": navigation_record.latitude, "longitude": navigation_record.longitude,
                            "datetime": navigation_record.datetime,
                            "vehicle_plate": navigation_record.vehicle.plate})

        except Vehicle.DoesNotExist as e:
            errors.append({
                "message": repr(e),
                "data": v["vehicle_plate"]
            })
        except Exception as e:
            errors.append({
                "message": repr(e),
                "data": v
            })
    return JsonResponse({"created": created, "errors": errors}, status=200)
