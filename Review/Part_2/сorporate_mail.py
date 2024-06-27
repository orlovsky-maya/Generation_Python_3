old_employees = {input() for _ in range(int(input()))}
new_employees = [input() for _ in range(int(input()))]



for name in new_employees:
    i = 0
    new_mail = f"{name}@beegeek.bzz"

    # search unique name
    while new_mail in old_employees:
        i += 1
        new_mail = f"{name}{i}@beegeek.bzz"

    # add found name
    old_employees.add(new_mail)
    print(new_mail)



# # INPUT DATA:
#
# # TEST_1:
# 6
# ivan-petrov@beegeek.bzz
# petr-ivanov@beegeek.bzz
# ivan-petrov1@beegeek.bzz
# ivan-ivanov@beegeek.bzz
# ivan-ivanov1@beegeek.bzz
# ivan-ivanov2@beegeek.bzz
# 3
# ivan-ivanov
# petr-petrov
# petr-ivanov
#
# # TEST_2:
# 2
# timyr-guev2@beegeek.bzz
# anri-tabuev@beegeek.bzz
# 3
# timyr-guev
# timyr-guev
# anri-tabuev
#
# # TEST_3:
# 3
# timyr-guev2@beegeek.bzz
# ruslan-chaniev1@beegeek.bzz
# ruslan-chaniev@beegeek.bzz
# 5
# timyr-guev
# timyr-guev
# timyr-guev
# ruslan-chaniev
# ruslan-chaniev
#
# # TEST_4:
# 1
# timyr-guev@beegeek.bzz
# 5
# timyr-guev
# timyr-guev
# timyr-guev
# timyr-guev
# timyr-guev
#
# # TEST_5:
# 3
# timyr-guev1@beegeek.bzz
# anri-tabuev@beegeek.bzz
# ivan-petrov10@beegeek.bzz
# 5
# ivan-petrov
# ivan-petrov
# ivan-petrov
# timyr-guev
# timyr-guev
#
# # TEST_6:
# 2
# anri-tabuev1@beegeek.bzz
# arthur-kharisov3@beegeek.bzz
# 7
# anri-tabuev
# anri-tabuev
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
#
# # TEST_7:
# 2
# anri-tabuev1@beegeek.bzz
# arthur-kharisov3@beegeek.bzz
# 15
# anri-tabuev
# anri-tabuev
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov
# arthur-kharisov


# # OUTPUT DATA:
#
# # TEST_1:
# ivan-ivanov3@beegeek.bzz
# petr-petrov@beegeek.bzz
# petr-ivanov1@beegeek.bzz
#
# # TEST_2:
# timyr-guev@beegeek.bzz
# timyr-guev1@beegeek.bzz
# anri-tabuev1@beegeek.bzz
#
# # TEST_3:
# timyr-guev@beegeek.bzz
# timyr-guev1@beegeek.bzz
# timyr-guev3@beegeek.bzz
# ruslan-chaniev2@beegeek.bzz
# ruslan-chaniev3@beegeek.bzz
#
# # TEST_4:
# timyr-guev1@beegeek.bzz
# timyr-guev2@beegeek.bzz
# timyr-guev3@beegeek.bzz
# timyr-guev4@beegeek.bzz
# timyr-guev5@beegeek.bzz
#
# # TEST_5:
# ivan-petrov@beegeek.bzz
# ivan-petrov1@beegeek.bzz
# ivan-petrov2@beegeek.bzz
# timyr-guev@beegeek.bzz
# timyr-guev2@beegeek.bzz
#
# # TEST_6:
# anri-tabuev@beegeek.bzz
# anri-tabuev2@beegeek.bzz
# arthur-kharisov@beegeek.bzz
# arthur-kharisov1@beegeek.bzz
# arthur-kharisov2@beegeek.bzz
# arthur-kharisov4@beegeek.bzz
# arthur-kharisov5@beegeek.bzz
#
# # TEST_7:
# anri-tabuev@beegeek.bzz
# anri-tabuev2@beegeek.bzz
# arthur-kharisov@beegeek.bzz
# arthur-kharisov1@beegeek.bzz
# arthur-kharisov2@beegeek.bzz
# arthur-kharisov4@beegeek.bzz
# arthur-kharisov5@beegeek.bzz
# arthur-kharisov6@beegeek.bzz
# arthur-kharisov7@beegeek.bzz
# arthur-kharisov8@beegeek.bzz
# arthur-kharisov9@beegeek.bzz
# arthur-kharisov10@beegeek.bzz
# arthur-kharisov11@beegeek.bzz
# arthur-kharisov12@beegeek.bzz
# arthur-kharisov13@beegeek.bzz