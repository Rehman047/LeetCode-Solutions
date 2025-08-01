class Solution {
public:
    int func(vector<int>& nums, int k) {
        int l = 0;
        int r = 0;
        int ans = 0;
        int num = 0;
        while (r < nums.size()) {
            if (nums[r] % 2 != 0) {
                num++;
            }
            while (num > k) {
                if (nums[l] % 2 != 0)
                    num--;

                l++;
            }
            ans += r-l  + 1;
            r++;
        }
        return ans;
    }
    int numberOfSubarrays(vector<int>& nums, int k) {
        if (k == 0)
            return func(nums, k);
        else
            return func(nums, k) - func(nums, k - 1);
    }
};
