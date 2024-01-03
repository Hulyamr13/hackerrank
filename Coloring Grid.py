import os, sys, json

DATA = {(2, 2): [0, 1000000004, 6, 1000000003, 1], (3, 2): [0, 999999998, 27, 999999974, 21, 1000000000, 1], (3, 3): [0, 79, 999999684, 594, 999999359, 459, 999999791, 66, 999999995, 1], (4, 2): [0, 999999980, 108, 999999818, 189, 999999890, 45, 999999997, 1], (4, 3): [0, 999999316, 3586, 999991301, 13109, 999986402, 10207, 999994365, 2296, 999999333, 136, 999999990, 1], (4, 4): [0, 999982514, 112275, 999653733, 682349, 999039380, 1022204, 999151951, 557782, 999707124, 122662, 999959393, 10437, 999997992, 276, 999999983, 1], (5, 2): [0, 999999926, 405, 999999089, 1242, 999998900, 675, 999999725, 78, 999999994, 1], (5, 3): [0, 6041, 999961995, 114174, 999782604, 293138, 999704216, 230070, 999860026, 66889, 999975041, 7163, 999998475, 231, 999999985, 1], (5, 4): [0, 999558242, 3382139, 987385609, 30502219, 946406520, 72626994, 921382029, 69473457, 949204278, 30965801, 984210493, 6729039, 997614488, 697035, 999834632, 31129, 999995524, 465, 999999976, 1], (5, 5): [0, 32126211, 709564232, 292190136, 232029122, 82227215, 439209057, 473119430, 67725133, 54961856, 570790382, 594826019, 917128404, 754018465, 273041111, 688444232, 763044069, 69997383, 982409096, 3714180, 999352655, 90798, 999990143, 780, 999999967, 1], (6, 2): [0, 999999764, 1458, 999995957, 6885, 999992042, 6588, 999996029, 1755, 999999452, 120, 999999991, 1], (6, 3): [0, 999947198, 390541, 998604889, 3199931, 994723790, 6631221, 993428507, 5239732, 996599955, 1804417, 999217296, 275815, 999922037, 17310, 999997092, 351, 999999980, 1], (6, 4): [0, 988850024, 99187684, 566695025, 237553259, 407136163, 236565742, 398233346, 139205885, 333111696, 453635838, 998914196, 741090291, 128917264, 375602399, 860818448, 44085868, 988161799, 2662611, 999506990, 73290, 999991586, 703, 999999969, 1], (6, 5): [0, 667603002, 330159148, 368206607, 774308385, 222693266, 617152576, 633053952, 560175074, 824756668, 790624647, 146465957, 588427372, 90431435, 951092774, 496118870, 63469467, 949638336, 369659433, 901718610, 170621543, 130546007, 423734088, 917354965, 13680406, 998113823, 210956, 999981603, 1176, 999999958, 1], (6, 6): [0, 699132224, 813991468, 881667439, 428431154, 5407595, 488320146, 164388651, 2127073, 498182989, 886595559, 373775878, 43387463, 438122017, 45722653, 238937973, 392388417, 338927316, 438566589, 613881757, 522570186, 9304468, 370336305, 406066060, 113889977, 668020107, 878825566, 116644446, 454371681, 623652153, 49332660, 994578395, 486210, 999965812, 1770, 999999947, 1], (7, 2): [0, 999999278, 5103, 999983240, 34263, 999951407, 50544, 999960344, 23787, 999989099, 3780, 999999044, 171, 999999988, 1], (7, 3): [0, 461639, 996076814, 16228195, 956545009, 84443921, 873511537, 151404076, 851834734, 120295965, 918230987, 46756884, 977481221, 9114580, 996917452, 862410, 999803503, 35612, 999995059, 496, 999999975, 1], (7, 4): [0, 718615376, 852134720, 731014800, 919199714, 151384412, 910540726, 925708493, 108743858, 377798070, 896885414, 327523101, 289321710, 536364782, 865906077, 190040048, 224140548, 886891025, 717066999, 206869522, 200354194, 956629170, 7938573, 998793746, 148239, 999985835, 990, 999999962, 1], (7, 5): [0, 247800214, 754058346, 97389315, 216782521, 214846682, 618511486, 59441771, 11452638, 5438850, 48037249, 628914555, 261981156, 527799287, 896226159, 383745217, 955535102, 521097451, 876778742, 56074783, 938737246, 40995157, 70497221, 749334842, 817285883, 383578110, 40797671, 833672296, 707496902, 39845994, 995453531, 422950, 999969175, 1653, 999999949, 1], (7, 6): [0, 864173627, 749449876, 442624612, 762952113, 132078013, 787745686, 116634751, 312355005, 434856166, 459688502, 4429088, 652274938, 188155549, 958099, 537561026, 383503680, 525768064, 323208651, 824811676, 407592736, 504292463, 459345679, 979297842, 839126110, 229156607, 147779401, 358184107, 688395228, 361647378, 993445619, 637976021, 948273414, 790761215, 327305310, 694512604, 141715954, 987048438, 969595, 999942882, 2485, 999999936, 1], (7, 7): [0, 97370719, 92213503, 730766796, 225856082, 452227038, 125117711, 834937384, 144644580, 99198187, 900997296, 371574906, 451748830, 648975092, 289154120, 23431919, 845157246, 621228558, 599596781, 468575796, 867750619, 15131983, 539608538, 86638756, 332942094, 261739568, 680927464, 974955834, 189876787, 156938257, 460605073, 224020321, 508390023, 300355761, 592731452, 398691538, 214343298, 862909598, 487667902, 742562978, 498812059, 674657884, 530479784, 403410654, 969244631, 1926585, 999904759, 3486, 999999923, 1], (8, 2): [0, 999997820, 17496, 999933668, 158193, 999734651, 331695, 999680786, 240894, 999856259, 67851, 999974870, 7182, 999998474, 231, 999999985, 1], (8, 3): [0, 995964516, 38746592, 817977392, 556665714, 756622227, 156743307, 984390057, 482504115, 623420929, 779539778, 43093297, 183511594, 383973831, 275851175, 894018467, 34754589, 990350984, 2241099, 999571964, 65569, 999992251, 666, 999999970, 1], (8, 4): [0, 899101279, 783313775, 847766933, 495571720, 817492412, 674780114, 590913221, 999502287, 690971146, 170061259, 295374993, 775900545, 992440106, 396466313, 659125330, 669737080, 151135494, 324140271, 545730460, 176377583, 781491255, 50185818, 611408630, 712710432, 870655195, 19971826, 997425743, 269696, 999977928, 1326, 999999955, 1], (8, 5): [0, 663377559, 641711110, 304770778, 454399437, 769271861, 200715913, 559697831, 95591635, 576285573, 164922125, 116868769, 193045246, 388659193, 667458799, 212314210, 684602569, 949958563, 525798577, 982858794, 920880543, 58697882, 50682160, 552964105, 804720659, 552753117, 352914618, 609985469, 638453940, 633029704, 797170128, 328006824, 309565896, 148119287, 98629482, 990398807, 764688, 999952130, 2211, 999999940, 1], (8, 6): [0, 842333234, 610982688, 833995456, 111540512, 359759542, 30241094, 169477934, 817727315, 649024502, 215637591, 698781606, 551738016, 937303858, 955819070, 541430307, 304346759, 722715603, 558614827, 191600588, 633988744, 347435426, 726642219, 958478985, 435785150, 437401449, 673503352, 729345700, 364549380, 939053403, 163493315, 827909445, 516288345, 66839085, 779115112, 632292710, 422366218, 595271383, 585308161, 634847466, 854350909, 250785551, 347394642, 972822506, 1746295, 999911482, 3321, 999999925, 1], (8, 7): [0, 926432121, 11939523, 645854206, 740761708, 834661425, 139213522, 46800478, 719303385, 33048430, 453747898, 707149262, 904096717, 378904378, 544386710, 157434681, 364066552, 208289930, 654946473, 132590876, 143384232, 884395237, 252159582, 164863201, 744076902, 208460450, 401462338, 685789303, 750349238, 789573572, 15070558, 69410734, 860706301, 711251748, 288629906, 720307587, 384512927, 287124541, 495516217, 130051735, 554612381, 889115038, 72633156, 535584693, 265841875, 861301377, 860167878, 948351910, 218308255, 281760028, 982543381, 935737565, 3460892, 999852609, 4656, 999999910, 1], (8, 8): [0, 670668286, 693474490, 542685095, 438050885, 801277705, 380599710, 989804685, 216408447, 737457948, 123766027, 590242652, 941208356, 318580116, 829794788, 67902703, 284197211, 42524299, 787379026, 462989440, 988524930, 936267058, 885063637, 235497203, 965109093, 663636951, 242367513, 896774992, 86876566, 499269737, 453294416, 397072528, 23079787, 436780351, 228301256, 788397410, 321545092, 905829671, 550984546, 542885647, 634426008, 295508535, 854981298, 527965637, 250334125, 957695717, 20270160, 174463300, 901999528, 941293243, 5638104, 417243417, 893810590, 855187853, 794653927, 436118252, 773015176, 44584419, 382122260, 866134709, 6205479, 999772136, 6216, 999999895, 1]}

MOD = 1000000007

def poly_eval(p, x):
    s = 0
    for c in reversed(p):
        s = (x*s + c)%MOD
    return s

def mod_power(x, k):
    if k == 0:
        return 1
    if k == 1:
        return x%MOD
    p = x
    for _ in range(k-1):
        p = (p * x)%MOD
    return p

def ncolorings(n, m, k):
    if k <= 0 or n <= 0 or m <= 0:
        return 0
    if n < m:
        n,m = m,n
    if n == 1:
        return k%MOD
    if m == 1:
        return (k*mod_power(k-1, n-1))%MOD
    else:
        p = DATA[(n,m)]
        return poly_eval(p, k)

def main():
    T = int(sys.stdin.readline())
    cases = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
    for n,m,k in cases:
        y = ncolorings(n, m, k)
        print(y)

main()