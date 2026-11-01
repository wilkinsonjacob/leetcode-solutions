class Solution {
public:
    bool isPalindrome(string s) {
        std::erase_if(s, [](unsigned char c) { 
        return !std::isalnum(c); 
        });

        std::ranges::transform(s, s.begin(), [](unsigned char c) {
        return std::tolower(c);
        });

        std::string reversed_string;
        for (auto i = static_cast<int>(s.size()) - 1; i >= 0; i--) {
            if (std::isalnum(s[i])) {
                reversed_string += s[i];
            }
        }
        std::cout << reversed_string << " == " << s;
        return reversed_string == s;
    }
};
