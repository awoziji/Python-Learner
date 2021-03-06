 # -*- coding:utf-8 -*-


'''
python编译器无法严格保证private字段的私密性。

不要盲目地将属性设为private，而是应该一开始就做好规划，并允许子类更多的访问超类的内部API

应该多用protected属性，并在文档中把这些字段的合理用法告诉子类的开发者，而不要试图用private属性来限制子类访问这些字段。

只有当子类不受控制时，才可以考虑用private属性来避免名称冲突。
'''
