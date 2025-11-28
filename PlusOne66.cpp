class Solution {

public:
    vector<int> plusOne(vector<int>& digits) {
        int i = digits.size() -1; // size of vector as the starting index
        bool flag = true;

        while (flag){               //while flag is true
            if (digits[i] == 9){    //check if current digit is 9 (and +1 will be 10)
                digits[i] = 0;      //update current index to 0
                i -= 1;             //move to previous index
                if (i == -1){       //if we reached the first number 
                    digits.insert(digits.begin(), 1);//insert 1 to front
                    flag = false;   //exit loop
                }
            }
            else {                  // else, inrease the last digit
                digits[i] = digits[i]+1;
                flag = false;       //exit loop
            }
        }
    return digits;
    }
};
