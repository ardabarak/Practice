class Solution {
public:
    int strStr(string haystack, string needle) {

        for (int i=0; i< haystack.length(); i++) {
            std::string sub = haystack.substr(i, needle.length()); //saving the current substring 
            if (sub == needle) {return i;} //return index if the we find the first matching substring
        }
        return -1; // return -1 if there's no matches
    }
};
