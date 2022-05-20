from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
import logging
from json import JSONDecodeError

log = logging.getLogger(__name__)


def index(request):
    return HttpResponse('<h1>Welcome To First API Project </h1>')


def show_data(request):
    if request.method == "GET":
        print(request.body) 
        try:
            data = json.loads(request.body)["data"]
            print(data)
            if not data:
                return JsonResponse({"msg": "Data not provided"}, status=400)
            for key in ["message", "Fmt"]:
                if not data[key]:
                    return JsonResponse({"msg": "{} must not be empty".format(key)}, status=400)
            if (data["Fmt"]).lower() == "true":
                print(data['Fmt'])
                return JsonResponse({'success': True, 'message': 'ok'})
            else:
                with open('test.csv', 'w') as f:
                    for key in data.keys():
                        f.write("%s,%s\n" % (key, data[key]))
                f.close()
                return JsonResponse({'success': False, 'message': 'data added into the csv'})
        except KeyError as exc:
            log.info(exc, exc_info=True)
            return JsonResponse({"msg":"{} not provided".format(str(exc))}, status=400)
        except JSONDecodeError as exc:
            log.info(exc, exc_info=True)
            return JsonResponse({"msg":"Provided data is not in json format."}, status=400)

