# def q0(i):
#     if num[i] == '*':
#         return q1(i - 1)
#
# def q1(i):
#     if num[i] == '1':
#         num[i] = '2'
#         return q2(i)
#     elif num[i] == '2':
#         num[i] = '0'
#         return q1(i - 1)
#
# def q2(i):
#     if num[i] == '*':
#         return num
#     elif num[i] == '0':
#         num[i] = '1'
#         return q2(i - 1)
#     elif num[i] == '1':
#         return q1(i - 1)
#     else:
#         return q2(i - 1)
#
