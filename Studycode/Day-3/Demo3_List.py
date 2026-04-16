"""
用列表方法对列表进行简单的操作2
Version:1.0
Author:x鑫
"""
# 用列表方法找元素下标和统计一个元素出现的次数
languages = ["Python", "C++", "C#", "Java", "Go", "Python"]
print(languages.index("Python"))
print(languages.index("Python", 1))  # 从下标1开始找“Python”
print(languages.count("Python"))
print(languages.count("oy++"))
# 排序和反转（升序、降序）
item1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item1.sort()
print(item1)
item1.reverse()
print(item1)
print("----------------------------------------------")

"""
# 在 Python 中，列表还可以通过一种特殊的字面量语法来创建，这种语法叫做生成式
# 优点:用列表生成式创建列表不仅代码简单优雅，而且性能上也优于使用for-in循环和append方法向空列表中追加元素的方式
"""
# 例一、创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
item2 = []
for i in range(1,100):
    if i % 3 == 0 or i % 5 ==0:
        item2.append(i)
print(item2)
item3 = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(item3)
# 有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = []
for num in nums1:
    nums2.append(num ** 2)
print(nums2)
nums3 = [num ** 2 for num in nums1]
print(nums3)
# 有一个整数列表nums1，创建一个新的列表nums2，将nums1中大于50的元素放到nums2中。
nums1 = [1, 15, 3, 555, 75, 66, 7, 89, 94]
nums2 = []
for num in nums1:
    if num > 50:
        nums2.append(num)
print(nums2)
nums3 = [num for num in nums1 if num > 50]
print(nums3)
