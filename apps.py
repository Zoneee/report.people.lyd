import requests

deptids = {
    '选择部门': 0, 'B_不动产登记中心': 993, 'C_财政局': 31, 'C_残联': 111, 'C_瀍河区': 18, 'C_城乡建投集团': 1004, 'C_城市管理局': 90, 'C_城投集团': 1007, 'D_档案馆': 113, 'F_发改委': 36, 'F_防震减灾中心': 33, 'G_高新区': 108, 'G_高新热力公司': 4, 'G_公安局': 39, 'G_供电公司': 6, 'G_公交集团': 1, 'G_工商银行': 95, 'G_供销社': 43, 'G_工信局': 65, 'G_光大银行': 101, 'G_轨道集团': 994, 'G_国宏集团': 1001, 'G_国资委': 42, 'H_恒丰银行': 995, 'H_弘义集团': 1005, 'H_绿色能源资源发展服务中心': 48, 'J_建设银行': 98, 'J_涧西区': 15, 'J_交通局': 51, 'J_交通银行': 99, 'J_教育局': 50, 'J_交运集团': 1014, 'J_节会服务中心': 67, 'J_机关事务管理局': 79, 'J_金融工作局': 53, 'K_科技局': 54, 'L_老城区': 17, 'L_粮食和物资储备局': 57, 'L_林业局': 56, 'L_龙门园区管委会': 59, 'L_栾川县': 27, 'L_河南省陆浑水库运行中心': 997, 'L_洛龙区': 19, 'L_洛宁县': 25, 'L_洛阳城燃热力': 996, 'L_洛阳海关': 60, 'L_洛阳民航': 8, 'L_洛阳暖鑫热力': 998, 'L_洛阳火车站': 7, 'L_洛阳市城乡一体化示范区管委会办公室': 193, 'L_洛阳市新冠病毒感染疫情防控指挥部': 1010, 'L_文旅集团': 1002, 'M_孟津区': 24, 'M_民生银行': 104, 'M_民政局': 64, 'M_民族宗教事务局': 63, 'N_农发集团': 1006, 'N_农业农村局': 69, 'N_农业银行': 96, 'Q_气象局': 71, 'R_热力公司': 3, 'R_人保财险公司': 988, 'R_人防办': 74, 'R_人力资源和社会保障局': 55, 'R_人寿保险公司': 989, 'R_润奥供电': 1013, 'R_汝阳县': 26, 'S_商务局': 77, 'S_生态环境局': 47, 'S_审计局': 78, 'S_市场发展服务中心': 80, 'S_市场监督管理局': 81, 'S_市政设施管理中心': 992, 'S_水利局': 76, 'S_水务集团': 2, 'S_税务局': 34, 'S_司法局': 75, 'S_嵩县': 29, 'S_水务集团新区热力分公司': 106, 'T_太平洋财产保险公司': 990, 'T_太平洋人寿保险公司': 991, 'T_体育局': 82, 'T_统计局': 83, 'T_退役军人事务局': 999, 'W_市政府外事办公室': 87, 'W_卫健委': 86, 'W_文保集团': 1003, 'W_文化广电和旅游局（文化）': 84, 'W_文物局': 85, 'W_文化广电和旅游局（旅游）': 58, 'X_乡村振兴局': 37, 'X_消防救援支队': 196, 'X_西工区': 16, 'X_新安县': 22, 'X_新奥华油燃气公司': 5, 'X_兴业银行': 103, 'Y_烟草局': 91, 'Y_偃师区': 21, 'Y_伊滨区': 115, 'Y_伊川县': 23, 'Y_医疗保障局': 1000, 'Y_应急管理局': 30, 'Y_银保监分局': 62, 'Y_宜阳县': 28, 'Y_有线电视网络': 110, 'Y_邮政储蓄银行': 105, 'Y_邮政管理局': 195, 'Y_中国邮政': 9, 'Z_政务服务中心': 89, 'Z_中国电信': 12, 'Z_中国联通': 11, 'Z_中国移动': 10, 'Z_中国银行': 97, 'Z_中石化': 13, 'Z_中石油': 14, 'Z_中信银行': 102, 'Z_中原银行': 100, 'Z_住房保障和房产服务中心': 38, 'Z_住房公积金管理中心': 93, 'Z_住房和城乡建设局': 49, 'Z_自然资源和规划局': 44
}

areaids = {
    '选择区域': 0, '涧西区': 1, '西工区': 2, '老城区': 3, '瀍河区': 4, '洛龙区': 5, '高新区': 7, '偃师区': 8, '新安县': 9, '伊川县': 10, '孟津区': 11, '洛宁县': 12, '宜阳县': 13, '嵩县': 14, '伊滨区': 16, '汝阳县': 17, '栾川县': 18
}

phone = ''
name = ''


def main():
    while True:
        description = getuserinput()
        if description == '':
            print('输入内容')
            continue
        geneContent(description)
        isOK = getusercheck()
        if isOK:
            isSuccess = submitreport()
            if isSuccess:
                showSuccess()
            else:
                showError()
    pass


def getuserinput():
    description = input('输入您的问题描述')
    return description


def geneContent(description):
    return ''


def getusercheck():
    isOK = input('是否提交：yes/no')
    return isOK == 'yes'


def submitreport():
    # 定义代理设置
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'https://127.0.0.1:8888'
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
    }

    # 定义要发送的数据
    data = {
        'no': '',
        'webid': '',
        'title': '投诉',
        'content': '',
        'shoppic': '',
        'typeid': '1',
        'isopen': '1',
        'deptid': '',
        'areaid': '',
        'petname': '',
        'phone': '',
        'contact_open': '',
        'email': '',
    }

    # 定义目标 URL
    url = 'https://people.lyd.com.cn/que_do.php?action=addque'

    # 发送 POST 请求
    response = requests.post(
        url, data=data, proxies=proxies, timeout=3, verify="./FiddlerRoot.pem")
    pass


def showSuccess():
    print('提交成功')


def showError():
    print('提交失败')


# main()

submitreport()
