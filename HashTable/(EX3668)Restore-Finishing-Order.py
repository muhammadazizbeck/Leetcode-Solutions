class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        # result = []
        # for item in order:
        #     if item in friends:
        #         result.append(item)

        # return result

        position = {id_:index for index, id_ in enumerate(order)}

        friends.sort(key=lambda x:position[x])

        return friends