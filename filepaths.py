import os
current_dir = os.path.dirname(__file__)

sjec = [current_dir + '/金庸/書劍恩仇錄/dic_%02d'
        % i for i in range(1, 21)]
bxj = [current_dir + '/金庸/碧血劍/dic_%02d'
        % i for i in range(1, 21)]
sdyx = [current_dir + '/金庸/射雕英雄傳/dic_%02d'
        % i for i in range(1, 41)]
xsfh = [current_dir + '/金庸/雪山飛狐/dic_%02d'
        % i for i in range(1, 11)]
sdxl = [current_dir + '/金庸/神雕俠侶/dic_%02d'
        % i for i in range(1, 41)]
fhwz = [current_dir + '/金庸/飛狐外傳/dic_%02d'
        % i for i in range(1, 21)]
bmxx = [current_dir + '/金庸/白馬嘯西風/dic_%02d'
        % i for i in range(1, 12)]
bmyb = [current_dir + '/金庸/白馬嘯西風/原版/dic_%02d'
        % i for i in range(1, 10)]
yyd = [current_dir + '/金庸/鴛鴦刀/dic']
yttl = [current_dir + '/金庸/倚天屠龍記/dic_%02d'
        % i for i in range(1, 41)]
lcj = [current_dir + '/金庸/連城訣/dic_%02d'
        % i for i in range(1, 13)]
tlbb = [current_dir + '/金庸/天龍八部/dic_%02d'
        % i for i in range(1, 51)]
xkx = [current_dir + '/金庸/俠客行/dic_%02d'
        % i for i in range(1, 22)]
xajh = [current_dir + '/金庸/笑傲江湖/dic_%02d'
        % i for i in range(1, 41)]
ldj = [current_dir + '/金庸/鹿鼎記/dic_%02d'
        % i for i in range(1, 51)]
ynj = [current_dir + '/金庸/越女劍/dic']

qxj = [current_dir + '/其他/七星劍/dic_%02d'
        % i for i in range(1, 29)]
jhqx = [current_dir + '/其他/江湖奇俠傳/dic_%02d'
        % i for i in range(1, 44)]
jdsj = [current_dir + '/古龍/絕代雙驕/dic_%03d'
        % i for i in range(1,127)]

hlm = [current_dir + '/其他/紅樓夢/dic_%03d'
        % i for i in range(1,121)]
bc = [current_dir + '/其他/邊城/dic_%02d'
        % i for i in range(1, 22)]

lhdj = [current_dir + '/梁羽生/龍虎鬥京華/dic_%02d'
        % i for i in range(0, 13)]
cmls = [current_dir + '/梁羽生/草莽龍蛇傳/dic_%02d'
        % i for i in range(1, 13)]
swqx = [current_dir + '/梁羽生/塞外奇俠傳/dic_%02d'
        % i for i in range(1, 29)]
qjxt = [current_dir + '/梁羽生/七劍下天山/dic_%02d'
        % i for i in range(1,31)]
jhsn = [current_dir + '/梁羽生/江湖三女俠/dic_%02d'
        % i for i in range(1, 49)]
bfmn = [current_dir + '/梁羽生/白髮魔女傳/dic_%02d'
        % i for i in range(1, 33)]
pzxy = [current_dir + '/梁羽生/萍蹤俠影錄/dic_%02d'
        % i for i in range(1, 33)]
bctn = [current_dir + '/梁羽生/冰川天女傳/dic_%02d'
        % i for i in range(1, 41)]
hjqq = [current_dir + '/梁羽生/還劍奇情錄/dic_%02d'
        % i for i in range(1, 15)]
shnx = [current_dir + '/梁羽生/散花女俠/dic_%02d'
        % i for i in range(1, 37)]
ndqy = [current_dir + '/梁羽生/女帝奇英傳/dic_%02d'
        % i for i in range(1, 33)]
kxtj = [current_dir + '/梁羽生/狂俠天驕魔女/dic_%03d'
        % i for i in range(1, 121)]
fyld = [current_dir + '/梁羽生/風雲雷電/dic_%02d'
        % i for i in range(1, 67)]
mylx = [current_dir + '/梁羽生/牧野流星/dic_%02d'
        % i for i in range(1, 65)]
tzjl = [current_dir + '/梁羽生/彈指驚雷/dic_%02d'
        % i for i in range(1, 21)]
wltj = [current_dir + '/梁羽生/武林天驕/dic_%02d'
        % i for i in range(1, 18)]

jinyong_all = [
        sjec, bxj, sdyx, xsfh, sdxl, fhwz, bmxx, bmyb, 
        yyd, yttl, lcj, tlbb, xkx, xajh, ldj, ynj
]
jinyong_all_name = [
        '書劍恩仇錄', '碧血劍', '射雕英雄傳', '雪山飛狐',
        '神鵰俠侶', '飛狐外傳', '白馬嘯西風', '白馬原版',
        '鴛鴦刀', '倚天屠龍記', '連城訣', '天龍八部',
        '俠客行', '笑傲江湖', '鹿鼎記', '越女劍'
]
jinyong_long_work = [
        sjec, bxj, sdyx, sdxl, fhwz, yttl, tlbb, xajh, ldj
]
yusheng_all = [
        lhdj, cmls, swqx, qjxt,
        jhsn, bfmn, pzxy, bctn,
        hjqq, shnx, ndqy, kxtj,
        fyld, mylx, tzjl, wltj
]
yusheng_all_name = [
        '龍虎鬥京華', '草莽龍蛇傳', '塞外奇俠傳', '七劍下天山',
        '江湖三女俠', '白髮魔女傳', '萍蹤俠影錄', '冰川天女傳',
        '還劍奇情錄', '散花女俠', '女帝奇英傳', '狂俠天驕魔女',
        '風雲雷電', '牧野流星', '彈指驚雷', '武林天驕'
]
other_martials = [
        qxj, jhqx, jdsj
]
other_martials_name = [
        '七星劍', '江湖奇俠傳', '絕代雙驕'
]
other_types = [
        hlm, bc
]
other_types_name = [
        '紅樓夢', '邊城'
]

