class Solution {
public:
    bool isPalindrome(string s) {

        // lambda to turn lowercase
        std::transform(s.begin(), s.end(), s.begin(), [](unsigned char c)
            {return std::tolower(c); }); 

        // lambda to remove nonalphanumerics
        s.erase(std::remove_if(s.begin(), s.end(), [](unsigned char c) 
            {return !std::isalnum(c);}), s.end());  

        //creating a reverse copy of s
        std::string sReversed(s.rbegin(), s.rend());

        if (s ==""){return true;} //true if empty

        else if (s == sReversed){return true;} // true if equal

        else {return false;} // false if different
        
    }
};
