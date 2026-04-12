class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> output(n, 1);
        
        // Calculate the left products
        int left_prod = 1;
        for (int i = 0; i < n; i++) {
            output[i] = left_prod;
            left_prod *= nums[i];
        }
        
        // Calculate the right products and multiply with the left products
        int right_prod = 1;
        for (int i = n - 1; i >= 0; i--) {
            output[i] *= right_prod;
            right_prod *= nums[i];
        }
        
        return output;
    }
};