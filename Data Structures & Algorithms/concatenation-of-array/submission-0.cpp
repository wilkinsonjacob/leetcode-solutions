class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> res(2 * nums.size());

        for (auto i{0uz}; i < nums.size(); i++) {
            res[i] = nums[i];
            res[i + nums.size()] = nums[i];
        }
        return res;
    }
};