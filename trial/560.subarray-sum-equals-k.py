#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
import collections
# @lc code=start
class Solution:
    '''
    ハッシュマップを使って各要素の累積和を記録し、同じ累積和何回現れたかを数えることで、「k」に等しい部分配列の数をカウントする方法で実装
    各要素に対して以下のことを実行
    1, 累積和を更新する（cumulative_sum += num）

    2, 現在の累積和から「k」を引いた値（cumulative_sum - k）がハッシュマップ内に存在するかをチェックする。もし存在すれば、そのキーに対応する値（その累積和が何回現れたか）を部分配列数（subarray_count）に加える

    3, 現在の累積和がハッシュマップ内に存在するかをチェックする。もし存在すれば、そのキーに対応する値（その累積和が何回現れたか）をインクリメントします。存在しなければ、そのキー（累積和）に1をセットする

    この方法では、各要素を通じて累積和が「k」に等しい部分配列の数を求めることができ、最終的に、部分配列数（subarray_count）を返す
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = 0
        sum_count = {0: 1} # 最初の要素からサブアレイが始まる場合を処理するため
        subarray_count = 0
        for num in nums:
            cumulative_sum += num
            # 最後に累積したものから対象の値を引いて、残った累積和が過去にあれば最後に累積した部分(引いた部分)は、部分配列となる
            if cumulative_sum - k in sum_count:
                subarray_count += sum_count[cumulative_sum - k]
            if cumulative_sum in sum_count:
                sum_count[cumulative_sum] += 1
            else:
                sum_count[cumulative_sum] = 1
        print(sum_count)
        return subarray_count


# @lc code=end
