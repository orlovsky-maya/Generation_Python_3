def get_biggest(numbers):
    if len(numbers) == 0:
        return -1
    else:
        numbers = list(map(str, numbers))
        n = len(numbers)

        for i in range(n - 1):
            for j in range(n - 1 - i):
                if numbers[j] + numbers[j + 1] < numbers[j + 1] + numbers[j]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        return int("".join(numbers))


# INPUT DATA:

# TEST_1:
print(get_biggest([1, 2, 3]))

# TEST_2:
print(get_biggest([61, 228, 9, 3, 11]))

# TEST_3:
print(get_biggest([7, 71, 72]))

# TEST_4:
print(get_biggest([]))

# TEST_5:
print(get_biggest([0, 0, 0, 0, 0, 0]))

# TEST_6:
print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))

# TEST_7:
print(get_biggest([7, 7, 7, 7, 7, 7, 7, 7, 7]))

# TEST_8:
print(get_biggest([62, 626]))

# TEST_9:
print(get_biggest(
    [3347, 3737, 4919, 6296, 4984, 424, 8837, 2482, 6264, 6361, 3769, 650, 1334, 3100, 9107, 8723, 2048, 6495, 2018,
     7716, 3747, 8417, 4632, 4684, 55, 4620, 7705, 9603, 6597, 5398, 9621, 1953, 2689, 6023, 6835, 1745, 5187, 3628,
     5533, 4911, 8934, 4624, 1705, 8767, 1188, 2228, 4462, 1006, 816, 4053, 3929, 4843, 596, 5239, 8833, 8660, 4267,
     4379, 6171, 452, 392, 1974, 1573, 6755, 8926, 1338, 460, 9346, 3882, 4892, 2511, 600, 5126, 3866, 587, 3048, 998,
     9455, 5556, 256, 8237, 9719, 5465, 2138, 8552, 9341, 4208, 7938, 1231, 8413, 3903, 6151, 7235, 7176, 8073, 6097,
     7686, 6092, 9191, 6215, 9788, 2327, 8652, 6473, 2667, 3497, 1768, 3481, 3561, 7, 1254, 9560, 3636, 5827, 7451,
     1354, 6151, 3608, 274, 935, 3632, 4659, 2423, 5806, 6891, 953, 4975, 1754, 5085, 5735, 2568, 6914, 190, 6953, 9034,
     6069, 5355, 1617, 5575, 895, 9132, 2472, 9157, 5168, 6368, 5223, 6233, 2890, 1576, 9845, 1859, 7012, 3782, 5471,
     5736, 6735, 8970, 3417, 7009, 3253, 4603, 7697, 6277, 9123, 3318, 2794, 6772, 1390, 5061, 5404, 271, 7298, 2484,
     8890, 4006, 5132, 109, 9721, 1650, 9107, 5224, 8546, 349, 7497, 7778, 3461, 4198, 317, 7795, 3201, 1797, 6991,
     9766, 5076, 6813, 6279, 7919, 3224, 8526, 7608, 1355, 9022, 5912, 8750, 2592, 9506, 7882, 5375, 7718, 1922, 5528,
     4260, 3957, 9232, 7827, 1919, 3690, 3314, 2631, 1328, 4655, 1092, 3643, 6231, 7947, 7826, 6380, 9664, 9522, 6950,
     8748, 5205, 2907, 1208, 4326, 6354, 5978, 1115, 2462, 8308, 4642, 6724, 4698, 3925, 4175, 3136, 9880, 5696, 6034,
     9164, 5627, 7139, 3784, 2271, 8815, 2458, 3154, 3632, 3867, 3150, 8358, 6684, 527, 2981, 6390, 5844, 1695, 2442,
     9400, 780, 4342, 427, 431, 1551, 1055, 4468, 4800, 6835, 7639, 49, 4236, 4160, 4186, 7101, 2987, 2986, 3014, 3375,
     2225, 8035, 8622, 4093, 5318, 9421, 5068, 3454, 6592, 9317, 72, 4509, 254, 790, 3696, 7037, 1549, 6636, 9421, 4426,
     122, 1068, 7330, 2472, 2018, 3095, 6369, 4561, 9826, 6903, 1507, 9056, 6108, 9288, 7502, 8199, 6555, 1342, 5558,
     8082, 5898, 4380, 2591, 3254, 6331, 1256, 6654, 2745, 2011, 7152, 1615, 7634, 4955, 8721, 2741, 8868, 8848, 2507,
     5985, 6656, 2958, 5149, 4533, 127, 5501, 8083, 3884, 9059, 8872, 9129, 1481, 9508, 9227, 1731, 5072, 5471, 9247,
     8914, 3438, 7241, 4124, 4404, 1857, 2342, 1431, 4694, 8976, 7477, 1112, 2224, 7161, 1694, 267, 461, 9369, 8151,
     3218, 7553, 4649, 2528, 4011, 7829, 193, 4560, 2272, 8146, 5015, 8287, 4084, 7, 3284, 4317, 9662, 3664, 5272, 5228,
     2731, 3308, 674, 8167, 8494, 5199, 6611, 7604, 1111, 3511, 3063, 1339, 93, 2750, 3512, 3703, 9034, 2874, 7955,
     7212, 6525, 6281, 2810, 5829, 8520, 2199, 6584, 749, 8931, 7837, 3094, 1877, 3618, 7155, 4304, 6198, 5882, 7293,
     4155, 7736, 9399, 9201, 8826, 2330, 2958, 8818, 2675, 2391, 9039, 1758, 4533, 6056, 32, 8358, 4360, 483, 1699,
     2258, 5923, 8499, 4242, 4734, 5415, 2259, 3927, 4359, 2588, 3176, 670, 4881, 5225, 5248, 9221, 1003, 4366, 9297,
     271, 6746, 3145, 776, 7119, 3890, 2078, 7523, 4656, 4310, 7360, 5929, 2997, 2044, 8771, 5628, 2969, 4641, 9623,
     8922, 1599, 1751, 3402, 7839, 4633, 831, 3786, 3689, 5682, 669, 3623, 5507, 1966, 1721, 4898, 4009, 2165, 4612,
     6111, 6055, 1344, 1302, 2222, 8951, 6959, 1053, 6557, 2663, 4302, 959, 7295, 9859, 6596, 4223, 4561, 5991, 8244,
     6288, 5057, 8838, 3190, 9050, 2761, 7887, 5699, 5551, 8506, 8187, 5459, 1339, 7254, 6411, 9317, 3296, 2129, 6525,
     3155, 4928, 4721, 8831, 3757, 3830, 7763, 2358, 9777, 6390, 5006, 5318, 1000, 4252, 6186, 1822, 4035, 7743, 5301,
     5307, 5644, 3786, 3849, 6107, 291, 7293, 7042, 8, 7230, 3384, 6489, 2843, 5470, 672, 3542, 1323, 6970, 1526, 6830,
     3447, 4064, 5022, 5661, 4089, 3451, 9130, 6595, 4421, 9671, 2984, 4729, 7831, 1273, 6664, 9150, 3860, 7822, 7311,
     210, 3485, 2768, 7496, 6626, 3497, 3451, 3344, 4722, 8970, 4135, 4192, 59, 8915, 3156, 5772, 2270, 5470, 698, 3499,
     8913, 4751, 2021, 7675, 7805, 8397, 3839, 4082, 4473, 5730, 2531, 6596, 3345, 7005, 241, 5955, 1121, 1086, 96,
     9866, 9490, 5677, 7607, 3245, 5981, 3351, 5977, 1012, 2169, 8621, 682, 8118, 7569, 4084, 262, 2401, 5456, 3215,
     6176, 5505, 2350, 3969, 6816, 8879, 7466, 9115, 4100, 4897, 8076, 257, 1206, 9811, 5708, 8506, 7850, 9186, 9784,
     6435, 1081, 8889, 1845, 6186, 9255, 4800, 603, 686, 6825, 6208, 2576, 3164, 6004, 6772, 1349, 9390, 9223, 6977,
     1496, 2789, 4242, 5296, 2394, 3647, 418, 9407, 7220, 8445, 2006, 6344, 5246, 5527, 9026, 5064, 2720, 3574, 4573,
     5492, 9564, 9686, 812, 4654, 96, 9508, 8288, 1709, 8335, 2058, 5580, 4273, 8275, 9207, 6067, 5728, 9627, 1721,
     7646, 4329, 5611, 3633, 7030, 4510, 440, 1010, 3588, 5922, 1929, 3569, 3922, 774, 9705, 5125, 7623, 47, 3655, 1368,
     7259, 1610, 9745, 2989, 6114, 7204, 5592, 1621, 8001, 221, 7880, 4039, 3346, 89, 2280, 3101, 1243, 448, 54, 2699,
     3365, 3495, 1356, 1443, 9323, 3903, 9028, 4461, 6249, 1577, 7964, 4207, 7341, 4994, 4219, 2277, 259, 1777, 3854,
     7420, 552, 484, 737, 579, 4239, 560, 9693, 5864, 4975, 8747, 1427, 3140, 2335, 1833, 3755, 9187, 8806, 6581, 4222,
     7480, 1086, 6893, 9048, 6917, 7203, 1345, 3546, 8320, 6601, 4428, 948, 3026, 4025, 465, 2150, 9022, 7663, 6272,
     3850, 278, 2871, 6329, 7092, 1512, 5253, 7717, 8354, 6835, 8399, 3231, 1713, 2007, 2520, 4431, 8876, 2153, 4877,
     919, 1269, 6148, 5435, 1779, 167, 681, 7862, 1831, 1823, 9842, 7388, 9460, 8960, 8526, 5478, 9078, 732, 7169, 6455,
     6876, 2734, 6767, 2817, 9283, 1191, 750, 7165, 4954, 897, 2780, 8087, 3425, 4358, 8984, 7637, 1314, 5515, 2941,
     4859, 1106, 1444, 4753, 975, 1166, 2131, 135, 3580, 7062, 1273, 772, 4447, 4997, 8833, 4467, 8311, 6052, 1191,
     4625, 3608, 8167, 2954, 610, 5292, 3431, 8630, 372, 4019, 9926, 6147, 2792, 3708, 7372, 7150, 5164, 2756, 7936,
     1250, 5748, 3992, 4838, 7166, 9811, 2227, 7492, 5954, 8611, 5067, 394, 9576, 9622, 9195, 295, 4965, 3321, 8770,
     613, 2212, 9534, 6627, 9046, 9176, 7129, 645, 3512, 6205, 5283, 6171, 3639, 283, 3565, 1026, 4717, 2259, 4695,
     7274, 6952, 623, 9193, 6457, 4436, 7953, 4708, 6022, 4771, 9419, 1416, 3485, 2514, 1378, 3676, 841, 6370, 8570,
     507]))

# TEST_10:
print(get_biggest([9, 6, 3, 0, 3, 6, 9]))

# TEST_11:
print(get_biggest([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

# TEST_12:
print(get_biggest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

# TEST_13:
print(get_biggest([1, 2, 3, 5, 4, 6, 7, 8, 9, 10]))

# TEST_14:
print(get_biggest([3]))

# TEST_15:
print(get_biggest(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
     31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
     60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
     89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
     114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136,
     137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159,
     160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182,
     183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205,
     206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228,
     229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251,
     252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274,
     275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297,
     298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320,
     321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343,
     344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366,
     367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389,
     390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412,
     413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435,
     436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458,
     459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481,
     482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504,
     505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527,
     528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550,
     551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573,
     574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596,
     597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619,
     620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642,
     643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665,
     666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688,
     689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711,
     712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734,
     735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757,
     758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780,
     781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803,
     804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826,
     827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849,
     850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872,
     873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895,
     896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918,
     919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941,
     942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964,
     965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987,
     988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999]))

#
# # OUTPUT DATA:
#
# # TEST_1:
# 321
#
# # TEST_2:
# 961322811
#
# # TEST_3:
# 77271
#
# # TEST_4:
# -1
#
# # TEST_5:
# 0
#
# # TEST_6:
# 78554656558534233433222211311
#
# # TEST_7:
# 777777777
#
# # TEST_8:
# 62662
#
# # TEST_9:
# 998992698809866985998459842982698119811978897849777976697597459721971997059696969396869671966496629627962396229621960395995769564956095395349522950895089506949094894609455942194219419940794009399939390936993593469341932393179317929792889283925592479232922792239221920792019199195919391919187918691769164915791509132913091299123911591079107907890599056905090489046903990349034902890269022902289898489789768970897089608958951893489318926892289158914891388908889888798876887288688848883888378833883388318826881888158806877187708767875087488747872387218660865286308622862186118570855285468526852685208506850684998494844584184178413839983978358835883548335832083183118308828882878275824482378199818781681678167815181468128118808780838082807680738035800179647955795379477938793679197907887788278807862785078397837783178297827782678227807805779577787777677637747743773677277187717771677057697768676757663764676397637763476237608760776047569755375237507502749774974967492748074777466745174207388737737273607341733073273117298729572937293727472725972547241723572307220721272047203717671697166716571617155715271507139712971197101709270627042703770307012700970056991698697769706959695369526950691769146903689368916876686683568356835683068268256816816681367726772676767556746746673567267246706696684666466566654663666276626661166016597659665966595659265846581655765556525652565064956489647364576456455643564116390639063806370636963686361635463446331632962966288628162796277627262646249623623362316215620862056198618661866176617161716151615161486147613611461116108610761060976092606960676056605560526036034602360226006004599159855981597859775965959555954592959235922591258985882587586458445829582758065795772574857365735573057285708569956965682567756615644562856275611560559255805575555855565555515533552855275525515550755055501549254785471547154705470546554595456545435541554045398537553555318531853075301529652925283527527252535248524652395228522552245223520551995187516851645149513251265125508550765075072506850675064506150575022501550064997499449844975497549654955495449492849194911489848974892488148774859484484348384834800480047714753475147473447294722472147174708469846954694468446594656465546546544649464246414633463246254624462046146124604603457345614561456045334533452451045094484473446844674462446144474436443144284426442144044404380437943664360435943584342432943264317431431043044302427427342674260425242442424242423942364223422242194208420741984192418641841754160415541354124410040934089408440844082406440534039403540254019401140094006399239693957394392939273925392392239033903389038843882386738663860385438503849383938303786378637843782376937573755374737373723708370336963690368936763664365536473643363936363633363236323628362336183608360835883580357435693565356135463542351235123511349934973497349534934853485348134613454345134513447343834313425341734023384337533653351334733463345334433213318331433083296328432543253324532323132243218321532013190317631731643156315531543150314531403136310131003095309430633048302630142997298929872986298429812969295829582954295294129129072890287428712843283281728102794279227892782780276827612756275027452742741273427312720271271269926892675267266726632631262259259225912588257625725682562542531252825202514251125072484248224722472246224582442242324124012394239123582350234223352330232722802277227222712270225922592258222822272225222422222212221219921692165215321502138213121292102078205820482044202120182018201120072006197419661953193192919221919190187718591857184518331831182318221797177917771768175817541751174517311721172117131709170516991695169416716501621161716151610159915771576157315511549152615121507149614811444144314311427141613901378136813561355135413513491345134413421339133913381334132813231314130212731273127126912561254125012431231122120812061191119111881166112111151112111111061092109108610861081106810551053102610121010100610031000
#
# # TEST_10:
# 9966330
#
# # TEST_11:
# 9876543210
#
# # TEST_12:
# 987654321100
#
# # TEST_13:
# 98765432110
#
# # TEST_14:
# 3
#
# # TEST_15:
# 9999999989979969959949939929919909899898898798698598498398298198097997978977976975974973972971970969969689679669659649639629619609599595895795695595495395295195094994948947946945944943942941940939939389379369359349339329319309299292892792692592492392292192091991918917916915914913912911910909909089079069059049039029019008998989889789689589489389289189088988888888788688588488388288188087987887877876875874873872871870869868868678668658648638628618608598588585785685585485385285185084984884847846845844843842841840839838838378368358348338328318308298288282782682582482382282182081981881817816815814813812811810809808808078068058048038028018007997987979779679579479379279179078978878787786785784783782781780779778777777776775774773772771770769768767767667657647637627617607597587577575675575475375275175074974874774746745744743742741740739738737737367357347337327317307297287277272672572472372272172071971871771716715714713712711710709708707707067057047037027017006996986976969669569469369269169068968868768686685684683682681680679678677676766756746736726716706696686676666666656646636626616606596586576566565565465365265165064964864764664645644643642641640639638637636636356346336326316306296286276266262562462362262162061961861761661615614613612611610609608607606606056046036026016005995985975965959559459359259159058958858758658585584583582581580579578577576575755745735725715705695685675665656556456356256156055955855755655555555455355255155054954854754654554544543542541540539538537536535535345335325315305295285275265255252452352252152051951851751651551514513512511510509508507506505505045035025015004994984974964954949449349249149048948848748648548484483482481480479478477476475474744734724714704694684674664654646446346246146045945845745645545454453452451450449448447446445444444443442441440439438437436435434434334324314304294284274264254244242342242142041941841741641541441413412411410409408407406405404404034024014003993983973963953943939339239139038938838738638538438383382381380379378377376375374373733723713703693683673663653643636336236136035935835735635535435353352351350349348347346345344343433423413403393383373363353343333333323313303293283273263253243233232232132031931831731631531431331312311310309308307306305304303303023013002992982972962952942932929229129028928828728628528428328282281280279278277276275274273272722712702692682672662652642632626226126025925825725625525425325252251250249248247246245244243242422412402392382372362352342332323223123022922822722622522422322222222122021921821721621521421321221211210209208207206205204203202202012001991981971961951941931921919119018918818718618518418318218181180179178177176175174173172171711701691681671661651641631621616116015915815715615515415315215151150149148147146145144143142141411401391381371361351341331321313113012912812712612512412312212121120119118117116115114113112111111110109108107106105104103102101101000