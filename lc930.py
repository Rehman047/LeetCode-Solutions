class Solution {
public:
    int func(vector<int>& nums, int goal) {
        int l = 0;
        int r = 0;
        int sum = 0;
        int ans = 0;
        while (r < nums.size()) {
            if (nums[r])
                sum++;

            while (sum > goal) {
                if (nums[l])
                    sum--;
                l++;
            }

            ans += r - l + 1;

            r++;
        }
        return ans;
    }
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        if (goal == 0)
            return func(nums, goal);
        else
            return func(nums, goal) - func(nums, goal - 1);
    }
};