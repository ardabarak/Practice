import static java.lang.Math.sqrt;

public class Solution {

    public int mySqrt(int x) {
        double root = sqrt(x);
        int floored = (int) Math.floor(root);
        return floored;
    }
}
