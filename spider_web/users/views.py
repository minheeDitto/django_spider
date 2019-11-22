from django.shortcuts import render,HttpResponse
from django.http import JsonResponse,QueryDict
from django.views.generic.base import View
import json
from django.views.decorators.csrf import csrf_protect
from .models import FileContent
from utils.encrypt import get_encrpt
import zipfile



# Create your views here.


class Login(View):



    def post(self,request):
        d = {"token":"admin-token"}
        return HttpResponse(json.dumps(d), content_type="application/json")


class Files(View):

    def post(self,request):
        """

        :param request:
        :return:
        """
        file = request.FILES.get("file")

        name = file.name.split(".")[0]

        files = FileContent.objects.filter(display_name=name)
        # if len(files):
        #     return JsonResponse({
        #     "status":"error",
        #     "error":"zip exist",
        #     "message":"fail",})
        # else:

        file_id = get_encrpt(name)

        display_name = name
        File_save = FileContent.objects.create(
            file_zip=file,
            cmd="",
            display_name=display_name,
            file_id=file_id
        )
        File_save.save()
        return HttpResponse(json.dumps({
            "status":"ok",
            "error":"",
            "message":"success",


        }),content_type="application/json")


class SpiderOperate(View):

    def get(self, request):
        spideLIst = FileContent.objects.all()
        datas = {
            "status":"ok",
            "message":"success",
            "data":{"list":[]},
            "total": len(spideLIst),
            "error":"",
        }
        for spider in spideLIst:
            spider_data = {}
            spider_data["cmd"] = spider.cmd
            spider_data["display_name"] = spider.display_name
            spider_data["_id"] = spider.file_id
            datas["data"]["list"].append(spider_data)
        return JsonResponse(datas)


class SpiderInfo(View):

    def get(self, request, id):
         spider = FileContent.objects.filter(file_id=id)

         data_dict = {
             "status":"ok",
             "message":"success",
             "data":{
                 "_id":id,
                 "name":spider[0].display_name,

                 "cmd":spider[0].cmd
             }

         }
         return JsonResponse(data_dict)

    def post(self, request, id):
        spider = FileContent.objects.filter(file_id=id)
        data_dict = json.loads(request.body.decode())
        if len(spider):
            spider = spider[0]
            spider.cmd = data_dict["cmd"]
            spider.display_name = data_dict["name"]
            spider.save()
        return JsonResponse({"status":"ok"})

    def delete(self, request, id):
        spider = FileContent.objects.filter(file_id=id)
        if spider:
            spider.delete()
            return JsonResponse({"status":"ok","message":"success"})


class SpiderFile(View):

    def get(self, request, id):
        pass









