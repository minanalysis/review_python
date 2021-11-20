# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] id="edUALcY5dX5F"
# ## 딕셔너리의 결과가 아래와 같이 나오도록 아래의 문자열을 변경해 보세요.
# ```
# {'경기': '031',
# '강원': '033',
# '충남': '041',
# '충북': '043',
# '경북': '054',
# '경남': '055',
# '전남': '061',
# '전북': '063'}
# ```

# +
phone = " >경기 031 >강원 033 >충남 041 >충북 043 >경북 054 >경남 055 >전남 061 >전북 063" 

print(phone.split(">"))

s_phone=phone.split(">")

dict_phone={}

for i in s_phone:
    if i != ' ':
        ss_phone=i.split()
        key=ss_phone[0]
        value=ss_phone[1]
        dict_phone[key]=value
        
dict_phone
    






# +
phone = ">경기 031 >강원 033 >충남 041 >충북 043 >경북 054 >경남 055 >전남 061 >전북 063"

phone_dict={}
phone_split = phone.split('>')
# phone_split = ['','경기 031','강원 033', ... , '전북 063']

for i in phone_split:
    i_list = i.split( ) 
    if i_list != [] : 
        a = i_list[0]
        b = i_list[1]
        phone_dict[a] = b
        
phone_dict 

#     a_list = phone_split.split( )
    
#     print(a_list)
# #     if phone_split != [' '] : 
# #         key = phone_split[0]
# #         val = phone_split[1]
#         phone_dict[key] = val

# phone_dict
# -


