# import os
# import pythoncom
#
# from django.core.mail import send_mail
# from django.db.models.signals import post_init, post_save
# from django.dispatch import receiver
# from docx.shared import Mm
# from docxtpl import DocxTemplate, InlineImage
#
# from contactApp.models import Resume
# from docx2pdf import convert
#
#
# # 触发器
# @receiver(post_init, sender=Resume)
# def before_save_resume(sender, instance, **kwargs):
#     """触发器，post_init表示在管理员单击“保存前”触发，post_save表示在管理员单击“保存后”触发.
#         @receiver中第一个参数表示信号类型，第二个表示监控的模型类"""
#     instance.__original_status = instance.status  # 记录点击前的状态
#
#
# @receiver(post_save, sender=Resume)
# def post_save_resume(sender, instance, **kwargs):
#     """触发器，当管理员修改面试成绩“通过”之后触发，@receiver第一个参数为管理员单击“保存后”触发"""
#     send_status = 0
#     # print(instance.__original_status)  # 点击之前状态
#     # print(instance.status)  # 点击之后状态
#     email = instance.email  # 获取到应聘者邮箱
#     EMAIL_FROM = 'z1915270314@163.com'  # 发送者邮箱
#     if instance.__original_status == 1 and instance.status == 2:
#         email_title = '恒达科技有限公司招聘初试结果'
#         email_body = '恭喜您通过本企业的初试，请您本周六到公司进行第二次面试！'
#         send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
#
#         # 生成动态word
#         template_path = os.getcwd() + "/media/contact/recruit.docx"  # 模板文件路径
#         print(template_path)
#         # 调用模板
#         template = DocxTemplate(template_path)
#         # 从实例中获取当前的字段
#         name = instance.name
#         personID = instance.personID
#         sex = instance.sex
#         email = instance.email
#         birth = instance.birth
#         edu = instance.edu
#         school = instance.school
#         major = instance.major
#         position = instance.position
#         experience = instance.experience
#         photo = instance.photo
#
#         context = {
#             'name': name,
#             'personID': personID,
#             'sex': sex,
#             'email': email,
#             'birth': birth,
#             'edu': edu,
#             'school': school,
#             'major': major,
#             'position': position,
#             'experience': experience,
#             'photo': InlineImage(template, photo, width=Mm(30), height=Mm(40)),
#         }
#         template.render(context)
#         # 存储文件的路径
#         filename = "%s/media/contact/recruit/%s_%d.docx" % (os.getcwd(), instance.name, instance.id)
#         template.save(filename)
#
#         # 调用CoInitialize创建pdf文档
#         pythoncom.CoInitialize()
#         # word转pdf
#         if os.path.exists(filename):# 判断是否存在该word文件
#             pdf_filename = "%s/media/contact/recruit/%s_%d.pdf" % (os.getcwd(), instance.name, instance.id)
#             convert(filename, pdf_filename)  # 将word转为pdf
#         else:
#             print("word文件不存在")
#
#     elif instance.__original_status == 1 and instance.status == 3:
#         email_title = '恒达科技有限公司招聘初试结果'
#         email_body = '很遗憾，您未能通过本企业的初试，感谢您的关注！'
#         send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
#     print(send_status)
