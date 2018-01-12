# -*- coding: utf-8 -*-
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
 
    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)
 
#__metaclass__ = upper_attr  #  这会作用到这个模块中的所有类
 
class Foo(object, metaclass=upper_attr):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'