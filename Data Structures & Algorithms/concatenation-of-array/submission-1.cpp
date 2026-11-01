class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        size_t initial_num_size = nums.size();

        for (size_t i{0}; i < initial_num_size; i++) {
            nums.push_back(nums[i]);
        }
        return nums;
    }
};