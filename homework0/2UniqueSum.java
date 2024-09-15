
/**
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

import java.util.HashMap;

public class UniqueSum {

    public static int[] test1 = { 1, 10, 8, 3, 2, 5, 7, 2, -2, -1 };
    public static int[] test2 = { 4, 3, 3, 5, 7, 0, 2, 3, 8, 6 };

    public static void main(String[] args) {
        System.out.println("Result for test 1: " + unique_sum(test1));
        System.out.println("Result for test 2: " + unique_sum(test2));
    }

    /**
     * Adds until element's count is higher than 1
     * 
     * @param arr Test array
     * @return Sum of unique elements in the array
     */
    public static int unique_sum(int[] arr) {
        HashMap<Integer, Integer> counts = new HashMap<>();
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            int current = arr[i];
            if (counts.getOrDefault(current, 0) < 1) sum += current;
            counts.put(current, counts.getOrDefault(current, 0) + 1);
        }
        return sum;
    }
}

/**
 * Question: 10 minutes
 */
