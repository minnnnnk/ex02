######################################
## 사전
######################################

print("=딕선어리(사전) 생성 ==================")
a = {} #생성방법 {}

a["r38"] = "빅데이타"
a["r32"] = "c언어"

print(a)

print("=딕선어리(사전) 생성 ==================")
d = {"야구": 5, "축구": 11, "농구":9}
print(d, type(d))
print(len(d))
print("야구" in d)
print("배구" in d)
print("배구" not in d)

print(d["축구"])
print(d.get("축구"))

del(d["야구"])
print(d)

d = {}
print(d)

d = {"야구": 5, "축구": 11, "농구":9 }
keys = d.keys()
print(keys)
print(type(keys))

"""for key in keys:
    print(key, d[key])"""



for key in keys:
    print('{0}:{1}'.format(key, d[key]))

