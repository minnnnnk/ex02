#list
print("=리스트 기본========================")
tList = [1, 2, "Python"]
#tList = [],
#tList = list()


print(tList[0], tList[1], tList[2], tList[-2], tList[-1])
print(tList[1:3])
print(tList * 2)
print(tList + [3, 4, 5])

print(len(tList))
print(2 in tList)

#del(tList[0)
del tList[0]

print(tList)

print("=리스트 수정방법==================")
tList[0] = "일"
print(tList)

bList = ['apple', 'banana', 10, 20]
bList[2] = bList[2] + 90
print(bList)

print("=리스트 수정방법===============")
cList =[1,12,123,1234]
cList[0:2] = [10, 20]
print(cList)

cList[0:2] = [10]
print(cList)

cList[1:2] = [20]
print(cList)
print("=리스트 수정방법===============")
dList = [1, 12, 123, 1234]
dList[1:2] = []
print(dList)

dList[0:2] = []
print(dList)

print("=리스트 수정방법===============")
eList = [1, 12, 123, 1234]

#eList[1:2] = "a" 변경
eList[1:1] = "a" #같은 숫자이면 추가
print(eList)

eList[5:] = [12345]
print(eList)

eList[:0] = [12, -1, 0]
print(eList[0])

print("=리스트 수정방법===============")
a = [1, 12, 123, "hello", 3.14, 1000]
print(a)

a.append(5)
print(a)

a.insert(3, 1000)
print(a)

#제거
a.remove(1000)
print(a)

a.pop(2)
print(a)

print("=리스트 함수 ====================")
b = [1, 123, 1000, 12, 1000]
print(b)

#b[5:] = [1, 2, 3]
#b.insert(5, [1, 2, 3])
#print(b[5])

#카운트
print(len(b))
print(b.count(1000))

#뒤집기
b.reverse()
print(b)

#정렬
b.sort()
print(b)

#index
print(b.index(1000))