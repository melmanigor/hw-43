import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed,HttpResponseBadRequest 
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from clothing.models import ClothingModel

@method_decorator(csrf_exempt, name='dispatch')
class ClothingListAPIView(View):
    
    def get(self, request):
        clothes = list(ClothingModel.objects.all())
        data=[]
        for item in clothes:
            data.append({
                'id':item.id,
                'name':item.name,
                'manufacturer':item.manufacturer,
                'price':item.price,
                'type':item.type.name
            })

        return JsonResponse(data,safe=False)
    def post(self, request):
        try:
            data = json.loads(request.body)
            item=ClothingModel.objects.create(
                name=data['name'],
                manufacturer=data['manufacturer'],
                price=data['price'],
                type_id=data['type_id']
            )

            return JsonResponse(
                {"id": item.id,
                 "name": item.name,
                 "manufacturer": item.manufacturer,
                 "price": item.price,                 
                 "type": item.type.name
                 
                 },
                status=201
                )


        except Exception as e:
            return HttpResponseBadRequest(json.dumps({"error": str(e)}), content_type='application/json')
@method_decorator(csrf_exempt, name='dispatch')
class ClothingDetailAPIView(View):
    def get(self, request, pk):
        try:
            item = ClothingModel.objects.get(pk=pk)
            return JsonResponse(
                {
                    "id": item.id,
                    "name": item.name,
                    "manufacturer": item.manufacturer,
                    "price": item.price,
                    "type": item.type.name
                }
            )
        except ClothingModel.DoesNotExist:
            return JsonResponse(
                {"error": "Item not found"},
                status=404
            )  

    def put(self, request, pk):
        try:
            data = json.loads(request.body)
            item = ClothingModel.objects.get(pk=pk)
            item.name = data['name']
            item.manufacturer = data['manufacturer']
            item.price = data['price']
            item.type_id = data['type_id']
            item.save() 
            return JsonResponse({"massage": "Item updated successfully"})
        except ClothingModel.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404) 
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({"error": str(e)}), content_type='application/json')

    def delete(self, request, pk):
        try:
            item = ClothingModel.objects.get(pk=pk)
            item.delete()
            return JsonResponse({"massage": "Item deleted successfully"})
        except ClothingModel.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404)