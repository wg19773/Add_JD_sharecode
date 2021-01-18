import requests
import json

#cfdUrl = 'http://api.turinglabs.net/api/v1/jd/jxcfd/create/' #京喜财富岛
zzUrl = 'https://code.chiang.fun/api/v1/jd/jdcash/create/sharecode/' #领现金
zdUrl = 'http://jd.turinglabs.net/api/v2/jd/bean/create/sharecode/' #种豆 
ncUrl = 'http://jd.turinglabs.net/api/v2/jd/farm/create/sharecode/' #农场
mcUrl = 'http://jd.turinglabs.net/api/v2/jd/pet/create/sharecode/'  #萌宠
ddUrl = 'http://jd.turinglabs.net/api/v2/jd/ddfactory/create/sharecode/' #东东工厂
jxUrl = 'http://jd.turinglabs.net/api/v2/jd/jxfactory/create/sharecode/' #京喜工厂
joyUrl = 'https://code.chiang.fun/api/v1/jd/jdcrazyjoy/create/sharecode/' #疯狂的Joy jdcrazyjoy


#Defalt_cfdShareCode= ['Jxcfd_GroupId_143_1099534112113','AUWE56NTjs2BobyK6miEf','ATGcUnqSUyDUNCGE','A0pLfRgoZzDcKCg']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_zzShareCode= ['ZEw2Zeu1Zw', 'eU9YG5XBGKlGliyXjC5G', 'ZEl1beW2Y_wj8W8', '-ry-tUs7Z_4k8w', 'cVlmKrO7Z_RJojA']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_ncShareCode= ['a50e6d7efcd848ca8281cb9de0fc87e4','95fb0d29333e4042b757b9e3d9fa0ab7','f403295ef3624b0bbdc879751516473b','27a5cb040c1d44b58a24d80da61099db','b1638a774d054a05a30a17d3b4d364b8']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_mcShareCode= ['MTAxODc2NTEzMDAwMDAwMDAwNjIzMDM5Nw==','MTAxODc2NTEzNDAwMDAwMDAxNTY3MjY3OQ==','MTAxODc2NTEzMjAwMDAwMDAxNTAxMTg5MQ==','MTE1NDQ5OTIwMDAwMDAwMzkxMzE4NDM=']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_zdShareCode= ['kgaroyrauafivcbp2cpznl3xoa','za6kg6vamtzyyelngvu4egas74','66nvo67oyxpydyknid7gnb5hl64zkefehrpk27q','kxg6vgmnlej6hotdtd4wokqs7m','bt6wkxd3txz7nvdqud4jynzof4']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_ddShareCode= ['P04z54XCjVWnYaS5nJfCWn_2n0','P04z54XCjVWnYaS5uyvgblfVH1Il5w','P04z54XCjVWnYaS5m9cZxeBrgIf9W22TeJwZg','P04z54XCjVWnYaS5nJaSmHx2XlKkLQ4','bt6wkxd3txz7nvdqud4jynzof4']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_jxShareCode= ['bKIstNuvE23fHdtW6HzzZg==','E_5JESV4tsmaifaCH98bSA==','AYRhSDoylQZ60BB8vIxFmA==','EoEhmxJM8mrye4W5lnlEOA==']#读取参数djj_sharecode为空，开始读取默认参数
Defalt_joyShareCode= ['rFdQSg-fMoE=', 'CkZ8cwV57JL9Q4pf3AGYoA==', 'JayfVNVRmUO_He8bfCZV3w==', 'FOXSzvD-nhm7iQCQ91EeXQ==', 'tC3NXEXwLJs_TKGRDxw2WA==']#读取参数djj_sharecode为空，开始读取默认参数

#学习与测试  by 2020.12
def AddhelpCode(Url,Defalt_ShareCode):
   for code in Defalt_ShareCode:
      try:
         AddcodeRes=hongliyu(Url+code+'/')
         print(AddcodeRes)
      
         if AddcodeRes['code']==200:
           print("互助码添加成功✅")
         elif AddcodeRes['code']==400:
           print("互助码已存在")
         else:
           print('互助码添加异常')
      except Exception as e:
          	pass
def hongliyu(url):
   try:
     return json.loads(requests.get(url).text)
   except Exception as e:
      print(f'''初始化函数:''', str(e))
      
AddhelpCode(zzUrl,Defalt_zzShareCode)
AddhelpCode(mcUrl,Defalt_mcShareCode)
AddhelpCode(ncUrl,Defalt_ncShareCode)
AddhelpCode(zdUrl,Defalt_zdShareCode)
AddhelpCode(ddUrl,Defalt_ddShareCode)
AddhelpCode(jxUrl,Defalt_jxShareCode)
AddhelpCode(joyUrl,Defalt_joyShareCode)
