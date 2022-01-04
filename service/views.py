import os
import base64

from django.core.paginator import Paginator
from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.encoding import escape_uri_path
from django.views.decorators.csrf import csrf_exempt

from service.models import Document
import numpy as np  # 矩阵运算 pip install numpy
import cv2  # opencv包 pip install opencv-python


def read_file(file_name, size):
    """分批读取文件"""
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c  # 生成器，相当于一个特殊的迭代器，当运行到这个语句的时候会保存当前的对象；下次再运行到这里的时候会接着上次的对象继续运行。
            else:
                break


def download(request):
    submenu = 'download'
    document_list = Document.objects.all().order_by('-publish_date')
    p = Paginator(document_list, 5)
    if p.num_pages <= 1:
        page_data = ''
    else:
        page = int(request.GET.get('page', 1))
        document_list = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        page_data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }
    return render(
        request, 'service/documentList.html', {
            'active_menu': 'service',
            'sub_menu': submenu,
            'docList': document_list,
            'page_data': page_data,
        })


def getDoc(request, id):
    """下载文件"""
    document = get_object_or_404(Document, id=id)

    update_to, filename = str(document.file).split('/')  # 文件路径和名字
    # 获取文件的路径
    file_path = '%s/media/%s/%s' % (os.getcwd(), update_to, filename)
    print(filename)
    # 将下载文件分批次写入本地磁盘，先不将他们载入文件内存，读取文件，以512B为单位构建迭代器
    response = StreamingHttpResponse(read_file(file_path, 512))

    # 作为文件直接下载到本机，用户再用软件打开
    response['Content-Type'] = 'application/octet-stream'
    # 规定文件名的下载格式，在文件名为中文时，要加上escape_uri_path
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(escape_uri_path(filename))
    return response


def platform(request):
    submenu = 'platform'
    return render(request, 'service/platForm.html', {
        'active_menu': 'service',
        'sub_menu': submenu,
    })
    return HttpResponse(html)


face_detector_path = 'service\\haarcascade_frontalface_default.xml'
face_detector = cv2.CascadeClassifier(face_detector_path)  # 生成人脸检测器


@csrf_exempt  # 用于规避跨站点请求攻击
def facedetect(request):
    result = {}
    # 规定用户用POST的请求上传检测的图片
    if request.method == "POST":
        # 请求中包含图像则以流方式读取图像
        if request.FILES.get("image", None) is not None:
            image = read_image(stream=request.FILES["image"])
        else:
            result.updata({'#faceNum': -1, })
            return JsonResponse(result)

        # cv2检测的时候是以灰度图片检测的
        # 将彩色图片转为灰度

        if image.shape[2] == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 进行人脸检测
        values = face_detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                                flags=cv2.CASCADE_SCALE_IMAGE)

        # 将检测得到的人脸检测关键点封装成坐标
        values = [(int(a), int(b), int(a + c), int(b + d)) for (a, b, c, d) in values]

        result.update({
            '#faceNum': len(values),
            "faces": values,
        })
        return JsonResponse(result)


def read_image(stream=None):
    """以流的形似读取图片"""
    if stream is not None:
        data_temp = stream.read()
    image = np.asanyarray(bytearray(data_temp), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


@csrf_exempt
def facedetectDemo(request):
    result = {}

    if request.method == "POST":
        if request.FILES.get('image') is not None:
            img = read_image(stream=request.FILES["image"])
        else:
            result.update({
                "#faceNum": -1,
            })
            return JsonResponse(result)

        if img.shape[2] == 3:
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 彩色图像转灰度图像
        else:
            imgGray = img

        # 进行人脸检测
        values = face_detector.detectMultiScale(imgGray,
                                                scaleFactor=1.1,
                                                minNeighbors=5,
                                                minSize=(30, 30),
                                                flags=cv2.CASCADE_SCALE_IMAGE)
        # 将检测得到的人脸检测关键点坐标封装
        values = [(int(a), int(b), int(a + c), int(b + d))
                  for (a, b, c, d) in values]

        # 将检测框显示在原图上
        for (w, x, y, z) in values:
            cv2.rectangle(img, (w, x), (y, z), (0, 255, 0), 2)

        retval, buffer_img = cv2.imencode('.jpg', img)  # 在内存中编码为jpg格式
        img64 = base64.b64encode(buffer_img)  # base64编码用于网络传输
        img64 = str(img64, encoding='utf-8')  # bytes转换为str类型
        result["img64"] = img64  # json封装
    return JsonResponse(result)
