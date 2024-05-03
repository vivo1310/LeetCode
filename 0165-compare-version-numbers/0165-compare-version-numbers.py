class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        
        # print(ver1, ver2)
#         longer add 0
        diff = abs(len(ver1) - len(ver2))
        if len(ver1) > len(ver2):
            for i in range(diff):
                ver2.append('0')
        elif len(ver1) < len(ver2):
            for i in range(diff):
                ver1.append('0'*diff)
        # print(diff, ver1, ver2)
#         now 2 array has same length

        for i in range(len(ver1)):
            if int(ver1[i]) < int(ver2[i]):
                return -1
            elif int(ver1[i]) > int(ver2[i]):
                return 1
        return 0
