import random


def get_confusables():
    confusables = {}
    confusables['A'] = ['\U0000FF21', '\U0001D400', '\U0001D434',
                        '\U00019468', '\U0001D49C', '\U0001D4D0', '\U0001D504', '\U0001D538', '\U0001D56C',
                        '\U0001D5A0', '\U0001D5D4', '\U0001D608',
                        '\U0001D63C', '\U0001D670', '\U00001D00', '\U00000391', '\U0001D6A8', '\U0001D6E2',
                        '\U0001D71C', '\U0001D756', '\U0001D790',
                        '\U00000410', '\U000013AA', '\U000015C5', '\U0000A4EE', '\U000102A0']

    confusables['B'] = ['\U0000FF22', '\U0000212C', '\U0001D401', '\U0001D435', '\U0001D469', '\U0001D4D1',
                        '\U0001D505',
                        '\U0001D609', '\U0001D63D', '\U0001D671', '\U00000392', '\U0001D6A9', '\U0001D6E3',
                        '\U0001D71D',
                        '\U0001D757', '\U0001D791', '\U00000412', '\U000013F4', '\U000015F7', '\U0000A4D0',
                        '\U00010282',
                        '\U000102A1', '\U00010301', '\U0000A7B4', '\U00000432']

    confusables['C'] = ['\U0001F74C', '\U000118F2', '\U000118E9', '\U0000FF23', '\U0000216D', '\U00002102',
                        '\U0000212D',
                        '\U0001D402', '\U0001D436', '\U0001D46A', '\U0001D49E', '\U0001D4D2', '\U0001D56E',
                        '\U0001D5A2',
                        '\U0001D5D6', '\U0001D60A', '\U0001D63E', '\U0001D672', '\U000003FD', '\U00002CA4',
                        '\U00000421',
                        '\U000013DF', '\U0000A4DA', '\U000102A2', '\U00010302', '\U00010415', '\U0001051C',
                        '\U000000C7',
                        '\U000004AA', '\U00000187']

    confusables['D'] = ['\U0000216E', '\U00002145', '\U0001D403', '\U0001D437', '\U0001D46B', '\U0001D49F',
                        '\U0001D4D3',
                        '\U0001D507', '\U0001D53B', '\U0001D56F', '\U0001D5A3', '\U0001D5D7', '\U0001D60B',
                        '\U0001D63F',
                        '\U0001D673', '\U000013A0', '\U000015DE', '\U000015EA', '\U0000A4D3', '\U00000110',
                        '\U000000D0', '\U00000189']

    confusables['E'] = ['\U000022FF', '\U0000FF25', '\U00002130', '\U0001D404', '\U0001D438', '\U0001D46C',
                        '\U0001D4D4',
                        '\U0001D508', '\U0001D53C', '\U0001D570', '\U0001D5A4', '\U0001D5D8', '\U0001D60C',
                        '\U0001D640',
                        '\U0001D674', '\U00000395', '\U0001D6AC', '\U0001D6E6', '\U0001D720', '\U0001D75A',
                        '\U0001D794',
                        '\U00000415', '\U00002D39', '\U000013AC', '\U0000A4F0', '\U000118A6', '\U000118AE',
                        '\U00010286', '\U0000011A',
                        '\U00000246', '\U00002107', '\U00000510', '\U000013CB', '\U00010401', '\U00000190']

    confusables['F'] = ['\U00002131', '\U0001D405', '\U0001D439', '\U0001D46D', '\U0001D4D5', '\U0001D509',
                        '\U0001D53D',
                        '\U0001D571', '\U0001D5A5', '\U0001D5D9', '\U0001D60D', '\U0001D641', '\U0001D675',
                        '\U0000A798',
                        '\U000003DC', '\U0001D7CA', '\U000015B4', '\U0000A4DD', '\U000118C2', '\U000118A2',
                        '\U00010287',
                        '\U000102A5', '\U00010525', '\U00000191']

    confusables['G'] = ['\U0001D406', '\U0001D43A', '\U0001D46E', '\U0001D4A2', '\U0001D4D6', '\U0001D50A',
                        '\U0001D53E',
                        '\U0001D572', '\U0001D5A6', '\U0001D5DA', '\U0001D60E', '\U0001D642', '\U0001D676',
                        '\U0000050C',
                        '\U000013C0', '\U000013F3', '\U0000A4D6', '\U000001E6', '\U0000011E', '\U000001E4',
                        '\U00000193', '\U00000509']

    confusables['H'] = ['\U0000FF28', '\U0000210B', '\U0000210C', '\U0000210D', '\U0001D407', '\U0001D43B',
                        '\U0001D46F',
                        '\U0001D4D7', '\U0001D573', '\U0001D5A7', '\U0001D5DB', '\U0001D60F', '\U0001D643',
                        '\U0001D677',
                        '\U00000397', '\U0001D6AE', '\U0001D6E8', '\U0001D722', '\U0001D75C', '\U0001D796',
                        '\U00002C8E',
                        '\U0000041D', '\U000013BB', '\U0000157C', '\U0000A4E7', '\U000102CF', '\U00002C67',
                        '\U000004A2',
                        '\U00000126', '\U000004C9', '\U000004C7']

    confusables['I'] = ['\U0000FF29', '\U0001D6B0', '\U0001D62D', '\U00000406', '\U0001D5A8', '\U0001D425',
                        '\U0000FE8D',
                        '\U0000FE8E', '\U0001D529', '\U00002110', '\U00002111', '\U0001028A', '\U00002C92',
                        '\U00010309',
                        '\U00002113', '\U0001D724', '\U00000196', '\U0001D798', '\U00000399', '\U0001D695',
                        '\U0001D7CF',
                        '\U00002223', '\U00000627', '\U0000FF29', '\U0001D5C5', '\U0001D540', '\U00000031',
                        '\U0001D644',
                        '\U0001D4C1', '\U00010320', '\U0001D43C', '\U0001EE00', '\U0001EE80', '\U000005C0',
                        '\U0001D470',
                        '\U000001C0', '\U000004C0', '\U000016C1', '\U0001D7ED', '\U0001D574', '\U000007CA',
                        '\U0000FF4C',
                        '\U0001D6EA', '\U00002D4F', '\U0001D75E', '\U0001D55D', '\U0001D7E3', '\U000005D5',
                        '\U0001E8C7',
                        '\U0001D661', '\U0001D4D8', '\U0001D5DC', '\U0001D7D9', '\U0001D459', '\U000005DF',
                        '\U00002160',
                        '\U0001D610', '\U00000661', '\U0001D48D', '\U0001D591', '\U0000FFE8', '\U0001D408',
                        '\U0000006C',
                        '\U000006F1', '\U0000A4F2', '\U00016F28', '\U0001D678', '\U0001D7F7', '\U0001D4F5',
                        '\U0000007C',
                        '\U0000217C', '\U000023FD', '\U0001D5F9']

    confusables['J'] = ['\U0000FF2A', '\U0001D409', '\U0001D43D', '\U0001D471', '\U0001D4A5', '\U0001D4D9',
                        '\U0001D50D',
                        '\U0001D541', '\U0001D575', '\U0001D5A9', '\U0001D5DD', '\U0001D611', '\U0001D645',
                        '\U0001D679',
                        '\U0000037F', '\U00000408', '\U000013AB', '\U0000148D', '\U0000A4D9', '\U0000A7B2',
                        '\U00000248',
                        '\U00001499', '\U00000575', '\U0001D6A5']

    confusables['K'] = ['\U0000212A', '\U0000FF2B', '\U0001D40A', '\U0001D43E', '\U0001D472', '\U0001D4A6',
                        '\U0001D4DA',
                        '\U0001D50A', '\U0001D542', '\U0001D576', '\U0001D5AA', '\U0001D5DE', '\U0001D612',
                        '\U0001D646',
                        '\U0001D67A', '\U0000039A', '\U0001D6B1', '\U0001D6EB', '\U0001D725', '\U0001D75F',
                        '\U0001D799',
                        '\U00002C94', '\U0000041A', '\U000013E6', '\U000016D5', '\U0000A4D7', '\U00010518',
                        '\U00002C69',
                        '\U0000049A', '\U0000049E', '\U00000198']

    confusables['L'] = ['\U0000216C', '\U00002112', '\U0001D408', '\U0001D43F', '\U0001D473', '\U0001D4DB',
                        '\U0001D50F',
                        '\U0001D543', '\U0001D577', '\U0001D5AB', '\U0001D5DF', '\U0001D613', '\U0001D647',
                        '\U0001D67B',
                        '\U00002CD0', '\U000013DE', '\U000014AA', '\U0000A4E1', '\U000118A3', '\U000118B2',
                        '\U0001041B',
                        '\U00010526', '\U00000141', '\U000014B7', '\U0000013F']

    confusables['M'] = ['\U000F0F2D', '\U0000216F', '\U00002133', '\U0001D40C', '\U0001D440', '\U0001D474',
                        '\U0001D4DC',
                        '\U0001D510', '\U0001D544', '\U0001D578', '\U0001D5AC', '\U0001D5E0', '\U0001D614',
                        '\U0001D648',
                        '\U0001D67C', '\U0000039C', '\U0001D6B3', '\U0001D6ED', '\U0001D727', '\U0001D761',
                        '\U0001D79B',
                        '\U000003FA', '\U00002C98', '\U0000041C', '\U000013B7', '\U000015F0', '\U000016D6',
                        '\U0000A4DF',
                        '\U000102B0', '\U00010311', '\U000004CD']

    confusables['N'] = ['\U0000FF2E', '\U00002115', '\U0001D40D', '\U0001D441', '\U0001D475', '\U0001D4A9',
                        '\U0001D4DD',
                        '\U0001D511', '\U0001D579', '\U0001D5AD', '\U0001D5E1', '\U0001D615', '\U0001D649',
                        '\U0001D67D',
                        '\U0000039D', '\U0001D6B4', '\U0001D6EE', '\U0001D728', '\U0001D762', '\U0001D79C',
                        '\U00002C9A',
                        '\U0000A4E0', '\U00010513', '\U0000019D']

    confusables['O'] = ['\U00000A66', '\U00000AE6', '\U00000BE6', '\U00000C66', '\U00000CE6', '\U00000ED0',
                        '\U00001040',
                        '\U00000030', '\U000007C0', '\U000009E6', '\U00000B66', '\U00003007', '\U000114D0',
                        '\U000118E0',
                        '\U0001D7CE', '\U0001D7D8', '\U0001D7E2', '\U0001D7EC', '\U0001D7F6', '\U0000FF2F',
                        '\U0001D40E',
                        '\U0001D442', '\U0001D476', '\U0001D4AA', '\U0001D4DE', '\U0001D512', '\U0001D546',
                        '\U0001D57A',
                        '\U0001D5AE', '\U0001D5E2', '\U0001D616', '\U0001D64A', '\U0001D67E', '\U0000039F',
                        '\U0001D6B6',
                        '\U0001D6F0', '\U0001D72A', '\U0001D764', '\U0001D79E', '\U00002C9E', '\U0000041E',
                        '\U00000555',
                        '\U00002D54', '\U00000B20', '\U00000D20', '\U0000A4F3', '\U000118B5', '\U00010292',
                        '\U000102AB',
                        '\U00010404', '\U00010516', '\U000001D1', '\U000000D8', '\U00002D41', '\U000001FE',
                        '\U00002296',
                        '\U0000229D', '\U0001F100', '\U0001F101', '\U000001A0', '\U000013A4']

    confusables['P'] = ['\U0000FF30', '\U00002119', '\U0001D40F', '\U0001D443', '\U0001D477', '\U0001D4AB',
                        '\U0001D4DF',
                        '\U0001D513', '\U0001D57B', '\U0001D5AF', '\U0001D5E3', '\U0001D617', '\U0001D64B',
                        '\U0001D67F',
                        '\U000003A1', '\U0001D6B8', '\U0001D6F2', '\U0001D72C', '\U0001D766', '\U0001D7A0',
                        '\U00002CA2',
                        '\U00000420', '\U000013E2', '\U0000146D', '\U0000A4D1', '\U00010295', '\U00001477',
                        '\U00001486', ]

    confusables['Q'] = ['\U0000211A', '\U0001D410', '\U0001D444', '\U0001D478', '\U0001D4AC', '\U0001D4E0',
                        '\U0001D514',
                        '\U0001D57C', '\U0001D5B0', '\U0001D5E4', '\U0001D618', '\U0001D64C', '\U0001D680',
                        '\U00002D55']

    confusables['R'] = ['\U0000211B', '\U0000211C', '\U0000211D', '\U0001D411', '\U0001D445', '\U0001D479',
                        '\U0001D4E1',
                        '\U0001D57D', '\U0001D5B1', '\U0001D5E5', '\U0001D619', '\U0001D64D', '\U0001D681',
                        '\U000001A6',
                        '\U000013A1', '\U000013D2', '\U00001587', '\U0000A4E3']

    confusables['S'] = ['\U0000FF33', '\U0001D412', '\U0001D446', '\U0001D47A', '\U0001D4AE', '\U0001D4E2',
                        '\U0001D516',
                        '\U0001D54A', '\U0001D57E', '\U0001D5B2', '\U0001D5E6', '\U0001D61A', '\U0001D64E',
                        '\U0001D682',
                        '\U00000405', '\U0000054F', '\U000013D5', '\U000013DA', '\U0000A4E2', '\U00010296',
                        '\U00010420']

    confusables['T'] = ['\U000022A4', '\U000027D9', '\U0001F768', '\U0000FF34', '\U0001D413', '\U0001D447',
                        '\U0001D47B',
                        '\U0001D4AF', '\U0001D4E3', '\U0001D517', '\U0001D548', '\U0001D57F', '\U0001D5B3',
                        '\U0001D5E7',
                        '\U0001D61B', '\U0001D64F', '\U0001D683', '\U000003A4', '\U0001D6BB', '\U0001D6F5',
                        '\U0001D72F',
                        '\U0001D769', '\U0001D7A3', '\U00002CA6', '\U00000422', '\U000013A2', '\U0000A4D4',
                        '\U000118BC',
                        '\U00010297', '\U000102B1', '\U00010315', '\U00002361', '\U0000023E', '\U0000021A',
                        '\U000001AE',
                        '\U000004AC', '\U000020AE', '\U00000166']

    confusables['U'] = ['\U0000222A', '\U000022C3', '\U0001D414', '\U0001D448', '\U0001D47C', '\U0001D4B0',
                        '\U0001D4E4',
                        '\U0001D518', '\U0001D54C', '\U0001D580', '\U0001D5B4', '\U0001D5E8', '\U0001D61C',
                        '\U0001D650',
                        '\U0001D684', '\U0000054D', '\U0000144C', '\U0000A4F4', '\U000118B8', '\U000001D3',
                        '\U00000244',
                        '\U000013CC', '\U00001458', '\U00001467', '\U000001B1', '\U0000162E']

    confusables['V'] = ['\U00002228', '\U000022C1', '\U00000667', '\U000006F7', '\U00002164', '\U0001D415',
                        '\U0001D449',
                        '\U0001D47D', '\U0001D4B1', '\U0001D4E5', '\U0001D519', '\U0001D54D', '\U0001D581',
                        '\U0001D5B5',
                        '\U0001D5E9', '\U0001D61D', '\U0001D651', '\U0001D685', '\U00000474', '\U00002D38',
                        '\U000013D9',
                        '\U0000142F', '\U0000A4E6', '\U000118A0', '\U0001051D', '\U0000143B', '\U0001F708']

    confusables['W'] = ['\U000118EF', '\U000118E6', '\U0001D416', '\U0001D44A', '\U0001D47E', '\U0001D4B2',
                        '\U0001D4E6',
                        '\U0001D51A', '\U0001D54E', '\U0001D582', '\U0001D5B6', '\U0001D5EA', '\U0001D61E',
                        '\U0001D652',
                        '\U0001D686', '\U0000051C', '\U000013B3', '\U000013D4', '\U0000A4EA', '\U000020A9']

    confusables['X'] = ['\U0000166D', '\U00002573', '\U00010322', '\U000118EC', '\U0000FF38', '\U00002169',
                        '\U0001D417',
                        '\U0001D44B', '\U0001D47F', '\U0001D4B3', '\U0001D4E7', '\U0001D51B', '\U0001D54F',
                        '\U0001D583',
                        '\U0001D5B7', '\U0001D5EB', '\U0001D61F', '\U0001D653', '\U0001D687', '\U000003A7',
                        '\U0001D6BE',
                        '\U0001D6F8', '\U0001D732', '\U0001D76C', '\U0001D7A6', '\U00002CAC', '\U00000425',
                        '\U00002D5D',
                        '\U00002D5D', '\U000016B7', '\U0000A4EB', '\U00010290', '\U000102B4', '\U00010317',
                        '\U00010527',
                        '\U0000A7B3', '\U000004B2']

    confusables['Y'] = ['\U0000FF39', '\U0001D418', '\U0001D44C', '\U0001D480', '\U0001D4B4', '\U0001D4E8',
                        '\U0001D51C',
                        '\U0001D550', '\U0001D584', '\U0001D5B8', '\U0001D5EC', '\U0001D620', '\U0001D654',
                        '\U0001D688',
                        '\U000003A5', '\U000003D2', '\U0001D6BC', '\U0001D6F6', '\U0001D730', '\U0001D76A',
                        '\U0001D7A4',
                        '\U00002CA8', '\U000004AE', '\U000013A9', '\U000013BD', '\U0000A4EC', '\U000118A4',
                        '\U000102B2',
                        '\U000000A5', '\U0000024E', '\U000004B0']

    confusables['Z'] = ['\U000102F5', '\U000118E5', '\U0000FF3A', '\U00002124', '\U00002128', '\U0001D419',
                        '\U0001D44D',
                        '\U0001D481', '\U0001D4B5', '\U0001D4E9', '\U0001D585', '\U0001D5B9', '\U0001D5ED',
                        '\U0001D621',
                        '\U0001D655', '\U0001D689', '\U00000396', '\U0001D6AD', '\U0001D6E7', '\U0001D721',
                        '\U0001D75B',
                        '\U0001D795', '\U000013C3', '\U0000A4DC', '\U000118A9', '\U000001B5', '\U00000224']

    confusables['a'] = ['\U0000237a', '\U0000FF41', '\U0001D41A', '\U0001D44E', '\U0001D482', '\U0001D4B6',
                        '\U0001D4EA', '\U0001D51E', '\U0001D552', '\U0001D586', '\U0001D5BA', '\U0001D5EE',
                        '\U0001D622', '\U0001D656', '\U0001D68A', '\U00000251', '\U000003B1', '\U0001D6C2',
                        '\U0001D6FC',
                        '\U0001D736', '\U0001D770', '\U0001D7AA', '\U00000430', '\U00002376', '\U00000103',
                        '\U000001CE',
                        '\U00000227', '\U000000E5', '\U00001E9A', '\U00001EA3']

    confusables['b'] = ['\U0001D41B', '\U0001D44F', '\U0001D483', '\U0001D4B7', '\U0001D4EB', '\U0001D51F',
                        '\U0001D553', '\U0001D587', '\U0001D5BB', '\U0001D5EF', '\U0001D623', '\U0001D657',
                        '\U0001D68B', '\U00000184', '\U0000042C', '\U000013CF', '\U000015AF', '\U00000253',
                        '\U00000183',
                        '\U00000411', '\U00000182', '\U00000180', '\U0000048C', '\U0000048D', '\U00000462',
                        '\U00000463']

    confusables['c'] = ['\U0000FF43', '\U0000217D', '\U0001D41C', '\U0001D450', '\U0001D484', '\U0001D4B8',
                        '\U0001D4EC', '\U0001D520', '\U0001D554', '\U0001D588', '\U0001D5BC', '\U0001D5F0',
                        '\U0001D624', '\U0001D658', '\U0001D68C', '\U00001D04', '\U000003F2', '\U00002CA5',
                        '\U00000441',
                        '\U0001043D', '\U000000A2', '\U0000023C', '\U000000E7', '\U000004AB']

    confusables['d'] = ['\U0000217E', '\U00002146', '\U0001D41D', '\U0001D451', '\U0001D485', '\U0001D4B9',
                        '\U0001D4ED', '\U0001D521', '\U0001D555', '\U0001D589', '\U0001D5BD', '\U0001D5F1',
                        '\U0001D625', '\U0001D659', '\U0001D68D', '\U00000501', '\U000013E7', '\U0000146F',
                        '\U0000A4D2',
                        '\U00000257', '\U00000256', '\U00000018', '\U00000111', '\U000020AB', '\U0000147B',
                        '\U00001487']

    confusables['e'] = ['\U0000212E', '\U0000FF45', '\U0000212F', '\U00002147', '\U0001D41E', '\U0001D452',
                        '\U0001D486', '\U0001D4EE', '\U0001D522', '\U0001D556', '\U0001D58A', '\U0001D5BE',
                        '\U0001D5F2', '\U0001D626', '\U0001D65A', '\U0001D68E', '\U0000AB32', '\U00000435',
                        '\U000004BD',
                        '\U0000011B', '\U00000115', '\U00000247', '\U000004BF', '\U000000E9']

    confusables['f'] = ['\U0001D41F', '\U0001D453', '\U0001D487', '\U0001D4BB', '\U0001D4EF', '\U0001D523',
                        '\U0001D557', '\U0001D58B', '\U0001D5BF', '\U0001D5F3', '\U0001D627', '\U0001D65B',
                        '\U0001D68F', '\U0000AB35', '\U0000A799', '\U0000017F', '\U00001E9D', '\U00000584',
                        '\U00000192',
                        '\U0000196E']

    confusables['g'] = ['\U0000FF47', '\U0000210A', '\U0001D420', '\U0001D454', '\U0001D488', '\U0001D4F0',
                        '\U0001D524', '\U0001D558', '\U0001D58C', '\U0001D5C0', '\U0001D5F4', '\U0001D628',
                        '\U0001D65C', '\U0001D690', '\U00000261', '\U00001D83', '\U0000018D', '\U00000581',
                        '\U00000260',
                        '\U000001E7', '\U000001F5', '\U000001E5']

    confusables['h'] = ['\U0000FF48', '\U0000210E', '\U0001D421', '\U0001D489', '\U0001D4BD', '\U0001D4F1',
                        '\U0001D525', '\U0001D559', '\U0001D58D', '\U0001D5C1', '\U0001D5F5', '\U0001D629',
                        '\U0001D65D', '\U0001D691', '\U000004BB', '\U00000570', '\U000013C2', '\U00000266',
                        '\U0000A695',
                        '\U000013F2', '\U00000127', '\U0000210F', '\U0000045B']

    confusables['i'] = ['\U000002DB', '\U00002373', '\U0000FF49', '\U00002170', '\U00002139', '\U00002148',
                        '\U0001D422', '\U0001D456', '\U0001D48A', '\U0001D4BE', '\U0001D4F2', '\U0001D526',
                        '\U0001D55A', '\U0001D58E', '\U0001D5C2', '\U0001D5F6', '\U0001D62A', '\U0001D65E',
                        '\U0001D692', '\U00000131', '\U0001D6A4', '\U0000026A', '\U00000269', '\U000003B9',
                        '\U00001FBE',
                        '\U0000037A', '\U0001D6CA', '\U0001D704', '\U0001D73E', '\U0001D778', '\U0001D7B2',
                        '\U00000456',
                        '\U0000A647', '\U000004CF', '\U000013A5', '\U000118C3', '\U00002378', '\U000001D0',
                        '\U00000268',
                        '\U00001D7C']

    confusables['j'] = ['\U0000FF4A', '\U00002149', '\U0001D423', '\U0001D457', '\U0001D48B', '\U0001D4BF',
                        '\U0001D4F3', '\U0001D527', '\U0001D55B', '\U0001D58F', '\U0001D5C3', '\U0001D5F7',
                        '\U0001D62B', '\U0001D65F', '\U0001D693', '\U000003F3', '\U00000458', '\U00000249',
                        '\U0001D6A5',
                        '\U00000237', '\U00000575']

    confusables['k'] = ['\U0001D424', '\U0000FF4B', '\U0001D458', '\U0001D48C', '\U0001D4C0', '\U0001D4F4',
                        '\U0001D528', '\U0001D55C', '\U0001D590', '\U0001D5C4', '\U0001D4F8', '\U0001D62C',
                        '\U0001D660', '\U0001D694', '\U00001D0B', '\U00000138', '\U000003BA', '\U000003F0',
                        '\U0001D6CB',
                        '\U0001D6DE', '\U0001D705', '\U0001D718', '\U0001D73F', '\U0001D752', '\U0001D779',
                        '\U0001D78C', '\U0001D7B3', '\U0001D7C6', '\U00002C95', '\U0000043A', '\U00000199',
                        '\U0000049B']

    confusables['l'] = ['\U0000FF4C', '\U000005C0', '\U0000007C', '\U00002223', '\U0000FFE8', '\U00000031',
                        '\U00000661', '\U000006F1', '\U00010320', '\U0001E8C7', '\U0001D7CF', '\U0001D7D9',
                        '\U0001D7F7', '\U00000049', '\U0000FF29', '\U00002160', '\U00002110', '\U00002111',
                        '\U0001D408',
                        '\U0001D43C', '\U0001D470', '\U0001D4D8', '\U0001D540', '\U0001D574', '\U0001D5A8',
                        '\U0001D5DC', '\U0001D610', '\U0001D644', '\U0001D678', '\U00000196', '\U0000217C',
                        '\U00002113',
                        '\U0001D425', '\U0001D459', '\U0001D48D', '\U0001D4C1', '\U0001D4F5', '\U0001D529',
                        '\U0001D55D', '\U0001D591', '\U0001D5C5', '\U0001D5F9', '\U0001D62D', '\U0001D661',
                        '\U0001D695', '\U000001C0', '\U00000399', '\U0001D6B0', '\U0001D6EA', '\U0001D724',
                        '\U0001D75E',
                        '\U0001D798', '\U00002C92', '\U00000406', '\U000004C0', '\U000005D5', '\U000005DF',
                        '\U00000627',
                        '\U0001EE00', '\U0001EE80', '\U0000FE8E', '\U0000FE8D', '\U000007CA', '\U00002D4F',
                        '\U000016C1',
                        '\U0000A4F2', '\U0001028A', '\U00010309', '\U00000142', '\U0000026D', '\U0000019A',
                        '\U0000026B',
                        '\U00000625', '\U0000FE88', '\U0000FE87', '\U00000673', '\U00002488', '\U00000623',
                        '\U0000FE84',
                        '\U0000FE83', '\U00000672', '\U00000675']

    confusables['m'] = ['\U00011700', '\U0000FF4D', '\U0001D48E', '\U0001D62E', '\U000118E3', '\U0001D592',
                        '\U0001D426', '\U0001D5C6', '\U0001D52A', '\U0001D55E', '\U0001D4C2', '\U0001D662',
                        '\U0001D4F6', '\U0001D696', '\U0001D45A', '\U0001D5FA', '\U0000217F']

    confusables['n'] = ['\U0000FF4E', '\U0001D427', '\U0001D45B', '\U0001D48F', '\U0001D4C3', '\U0001D4F7',
                        '\U0001D52B', '\U0001D55F', '\U0001D593', '\U0001D5C7', '\U0001D5FB', '\U0001D62F',
                        '\U0001D663', '\U0001D697', '\U000003C0', '\U000003D6', '\U0000213C', '\U0001D6D1',
                        '\U0001D6E1',
                        '\U0001D70B', '\U0001D71B', '\U0001D745', '\U0001D755', '\U0001D77F', '\U0001D78F',
                        '\U0001D7B9', '\U0001D7C9', '\U00001D28', '\U0000043F', '\U00000578', '\U0000057C',
                        '\U00000273',
                        '\U0000019E', '\U000003B7', '\U0001D6C8', '\U0001D702', '\U0001D73C', '\U0001D776',
                        '\U0001D7B0',
                        '\U00001D70', '\U00000146', '\U00000272', '\U0000014B']

    confusables['o'] = ['\U00000C02', '\U00000C82', '\U00000D02', '\U00000D82', '\U00000966', '\U00000A66',
                        '\U00000AE6', '\U00000BE6', '\U00000C66', '\U00000CE6', '\U00000D66', '\U00000E50',
                        '\U00000ED0',
                        '\U00001040', '\U0000FF4F', '\U00002134', '\U0001D428', '\U0001D45C', '\U0001D490',
                        '\U0001D4F8',
                        '\U0001D52C', '\U0001D490', '\U0001D4F8', '\U0001D52C', '\U0001D560', '\U0001D594',
                        '\U0001D5C8', '\U0001D5FC', '\U0001D630', '\U0001D664', '\U0001D698', '\U00001D0F',
                        '\U00001D11',
                        '\U0000AB3D', '\U000003BF', '\U0001D6D0', '\U0001D70A', '\U0001D744', '\U0001D77E',
                        '\U0001D7B8',
                        '\U000003C3', '\U0001D6D4', '\U0001D70E', '\U0001D748', '\U0001D782', '\U0001D7BC',
                        '\U00002C9F',
                        '\U0000043E', '\U000010FF', '\U00005085', '\U000005E1', '\U00000647', '\U0001EE24',
                        '\U0001EE64',
                        '\U0001EE84', '\U0000FEEB', '\U0000FEEC', '\U0000FEEA', '\U0000FEE9', '\U000006BE',
                        '\U0000FBAC',
                        '\U0000FBAD', '\U0000FBAB', '\U0000FBAA', '\U000006C1', '\U0000FBA8', '\U0000FBA9',
                        '\U0000FBA7',
                        '\U0000FBA6', '\U000006D5', '\U0000101D', '\U000118C8', '\U000118D7', '\U0001042C',
                        '\U000007C0',
                        '\U000009E6', '\U000001D2', '\U000000F8', '\U0000AB3E', '\U00000275', '\U0000A74B',
                        '\U000004E9',
                        '\U00000473', '\U00002296', '\U0000229D', '\U0000FCD9', '\U000001A1']

    confusables['p'] = ['\U00002374', '\U0000FF50', '\U0001D429', '\U0001D45D', '\U0001D491', '\U0001D4C5',
                        '\U0001D4F9', '\U0001D52D', '\U0001D561', '\U0001D595', '\U0001D5C9', '\U0001D5FD',
                        '\U0001D631', '\U0001D665', '\U0001D699', '\U000003C1', '\U000003F1', '\U0001D6D2',
                        '\U0001D6E0',
                        '\U0001D70C', '\U0001D71A', '\U0001D746', '\U0001D754', '\U0001D780', '\U0001D78E',
                        '\U0001D7BA', '\U0001D7C8', '\U00002CA3', '\U00000440', '\U000001A5', '\U00001D7D']

    confusables['q'] = ['\U0001D42A', '\U0001D45E', '\U0000FF51', '\U0001D492', '\U0001D4C6', '\U0001D4FA',
                        '\U0001D52E', '\U0001D562', '\U0001D596', '\U0001D5CA', '\U0001D5FE', '\U0001D632',
                        '\U0001D666', '\U0001D69A', '\U0000051B', '\U00000563', '\U00000566', '\U000002A0',
                        '\U00001D90',
                        '\U0000024B']

    confusables['r'] = ['\U0001D42B', '\U0000FF52', '\U0001D45F', '\U0001D493', '\U0001D4C7', '\U0001D4FB',
                        '\U0001D52F', '\U0001D563', '\U0001D597', '\U0001D5CB', '\U0001D5FF', '\U0001D633',
                        '\U0001D667', '\U0001D69B', '\U0000AB47', '\U0000AB48', '\U00001D26', '\U00002C85',
                        '\U00000433',
                        '\U0000027D', '\U0000027C', '\U0000024D', '\U00000493', '\U00001D72', '\U00000491']

    confusables['s'] = ['\U0000FF53', '\U0001D42C', '\U0001D460', '\U0001D494', '\U0001D4C8', '\U0001D4FC',
                        '\U0001D530', '\U0001D564', '\U0001D598', '\U0001D5CC', '\U0001D600', '\U0001D634',
                        '\U0001D668', '\U0001D69C', '\U0000A731', '\U000001BD', '\U00000455', '\U000118C1',
                        '\U00010448',
                        '\U00000282', '\U00001D74']

    confusables['t'] = ['\U0000FF54', '\U0001D42D', '\U0001D461', '\U0001D495', '\U0001D4C9', '\U0001D4FD',
                        '\U0001D531', '\U0001D565', '\U0001D599', '\U0001D5CD', '\U0001D601', '\U0001D635',
                        '\U0001D669', '\U0001D69D', '\U00001D1B', '\U000003C4', '\U0001D6D5', '\U0001D70F',
                        '\U0001D749',
                        '\U0001D783', '\U0001D7BD', '\U00000442', '\U000001AD', '\U000004AD', '\U00000167',
                        '\U00000163',
                        '\U0000021b']

    confusables['u'] = ['\U0000FF55', '\U0001D42E', '\U0001D462', '\U0001D496', '\U0001D4CA', '\U0001D4FE',
                        '\U0001D532', '\U0001D566', '\U0001D59A', '\U0001D5CE', '\U0001D602', '\U0001D636',
                        '\U0001D66A', '\U0001D69E', '\U0000A79F', '\U00001D1C', '\U0000AB4E', '\U00001B52',
                        '\U0000028B',
                        '\U000003C5', '\U0001D6D6', '\U0001D710', '\U0001D74A', '\U0001D784', '\U0001D7BE',
                        '\U00000446',
                        '\U0000057D', '\U000118D8', '\U000001D4', '\U0000197E', '\U0000028A']

    confusables['v'] = ['\U00002228', '\U000022C1', '\U0000FF56', '\U00002174', '\U0001D42F', '\U0001D463',
                        '\U0001D497', '\U0001D4CB', '\U0001D4FF', '\U0001D533', '\U0001D567', '\U0001D59B',
                        '\U0001D5CF', '\U0001D603', '\U0001D637', '\U0001D66B', '\U0001D69F', '\U00001D20',
                        '\U000003BD',
                        '\U0001D6CE', '\U0001D708', '\U0001D742', '\U0001D77C', '\U0001D7B6', '\U00000475',
                        '\U000005DB',
                        '\U000118C0']

    confusables['w'] = ['\U0000FF57', '\U0001D430', '\U0001D5D0', '\U00001D21', '\U00000461', '\U00000561',
                        '\U0000AB83', '\U0001D534', '\U0001D568', '\U0001D4CC', '\U0001D66C', '\U0000026F',
                        '\U0001D500',
                        '\U0001D6A0', '\U0001170F', '\U0001170E', '\U0001D464', '\U0001D604', '\U0001D498',
                        '\U0001D638', '\U0001D59C', '\U0000051D', '\U0001170A']

    confusables['x'] = ['\U0000166E', '\U000000D7', '\U0000292B', '\U0000292C', '\U00002A2F', '\U0000FF58',
                        '\U00002179', '\U0001D431', '\U0001D465', '\U0001D499', '\U0001D4CD', '\U0001D501',
                        '\U0001D535', '\U0001D569', '\U0001D59D', '\U0001D5D1', '\U0001D605', '\U0001D639',
                        '\U0001D66D', '\U0001D6A1', '\U00000445', '\U00001541', '\U0000157D', '\U00002A30']

    confusables['y'] = ['\U000002C3', '\U00001D8C', '\U0000FF59', '\U0001D432', '\U0001D466', '\U0001D49A',
                        '\U0001D4CE', '\U0001D502', '\U0001D536', '\U0001D56A', '\U0001D59E', '\U0001D5D2',
                        '\U0001D606', '\U0001D63A', '\U0001D66E', '\U0001D6A2', '\U0000028F', '\U00001EFF',
                        '\U0000AB5A',
                        '\U000003B3', '\U0000213D', '\U0001D6C4', '\U0001D6FE', '\U0001D738', '\U0001D772',
                        '\U0001D7AC',
                        '\U00000443', '\U000004AF', '\U000010E7', '\U000118DC', '\U000001B4', '\U0000024F',
                        '\U000004B1']

    confusables['z'] = ['\U0001D433', '\U0000FF5A', '\U0001D467', '\U0001D49B', '\U0001D4CF', '\U0001D503',
                        '\U0001D537', '\U0001D56B', '\U0001D59F', '\U0001D5D3', '\U0001D607', '\U0001D63B',
                        '\U0001D66F', '\U0001D6A3', '\U00001D22', '\U000118C4', '\U00000290', '\U000001B6',
                        '\U00000225',
                        '\U00001D76']

    return confusables


def get_homograph(input):
    confusables = get_confusables()
    output = ''
    for input_char in input:
        if input_char in confusables:
            next_confusables = confusables[input_char]
            selected_char = random.randint(0, len(input_char))
            output += next_confusables[selected_char]
        else:
            output += input_char

    return output


def expand(homograph, reverse_confusables, current, results):
    if len(homograph) == 0:
        results.add(current)
    else:
        if ord(homograph[0]) in reverse_confusables:
            for j in reverse_confusables[ord(homograph[0])]:
                expand(homograph[1:], reverse_confusables, current+j,results)
        else:
            expand(homograph[1:], reverse_confusables, current + homograph[0], results)


def convert_to_ascii(homograph):
    confusables = get_confusables()
    reverse_confusables = {}
    for i in confusables:
        for j in confusables[i]:
            if ord(j) not in reverse_confusables:
                reverse_confusables[ord(j)] = set()

            reverse_confusables[ord(j)].add(i)

    results = set()
    expand(homograph, reverse_confusables, '', results)
    return results


def generate_table():
    confusables = get_confusables()
    output = "<table>\n"

    for i in confusables:
        output += "\t<tr>\n\t\t<td><ul id=\"char{}\">\n".format(i)
        for j in confusables[i]:
            output += "<li class=\"li{}\" title=\"{}\">{}</li>".format(i, 'html code: &amp;#' + str(ord(j)),
                                                                       '&#' + str(ord(j)))

        output += "\n\t\t</ul></td>\n\t</tr>\n"
    output += "\n</table>"

    return output
