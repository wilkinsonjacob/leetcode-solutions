class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> mapping = {
            {')', '('}, 
            {'}', '{'}, 
            {']', '['}
        };
        std::vector<char> valid_openings = {'(', '{', '['};
        std::stack<char> openings;

        for (char c : s) {
            
            if (mapping.contains(c)) {
                if (openings.empty() || openings.top() != mapping.at(c)) {
                    return false;
                }
                openings.pop();
            }
            else {
                openings.push(c);
            }
        }
        return openings.empty();
    }
};
