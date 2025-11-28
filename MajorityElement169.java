import java.util.HashMap;
import java.util.Map;

class Solution {
    public int majorityElement(int[] nums) {

        Map<Integer, Integer> counts = new HashMap<>(); //creating a hashmap to store each occurrence as key & value
        for (int elem : nums) { // mapping each element by repeats
            counts.put(elem, counts.getOrDefault(elem, 0) + 1);
        }
        
        int majorMin = (nums.length)/2; // the min repeats needed to be major number

        for(Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if ((entry.getValue()) > majorMin) { // if cureent entry's number repeats more than the majorMin
                return (entry.getKey());
            }
        }

        return 0; 
    }
}
