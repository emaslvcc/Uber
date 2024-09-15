
/**
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

import java.util.HashMap;

public class ZeroSum {

    public static int[] test1 = { 1, 10, 8, 3, 2, 5, 7, 2, -2, -1 };
    public static int[] test2 = { 1, 10, 8, -2, 2, 5, 7, 2, -2, -1 };
    public static int[] test3 = { 4, 3, 3, 5, 7, 0, 2, 3, 8, 6 };
    public static int[] test4 = { 4, 3, 3, 5, 7, 0, 2, 3, 8, 0 };

    public static int[] test5 = { 1, 10, 8, 3, 2, 5, 7, 2, -2, -1 };
    public static int[] test6 = { 1, 10, 8, -2, 2, 5, 7, 2, -2, -1 };
    public static int[] test7 = { 4, 3, 3, 5, 7, 0, 2, 3, 8, 6 };
    public static int[] test8 = { 4, 3, 3, 5, 7, 0, 2, 3, 8, 0 };

    public static void main(String[] args) {
        System.out.println("Result for test 1: " + zero_sum(test1));
        System.out.println("Result for test 2: " + zero_sum(test2));
        System.out.println("Result for test 3: " + zero_sum(test3));
        System.out.println("Result for test 4: " + zero_sum(test4));

        System.out.println("Result for test 5: " + zero_sum_follow(test5));
        System.out.println("Result for test 6: " + zero_sum_follow(test6));
        System.out.println("Result for test 7: " + zero_sum_follow(test7));
        System.out.println("Result for test 8: " + zero_sum_follow(test8));
    }

    /**
     * Searches for the negative of the element, and adds a sum if it exists
     * 
     * @param arr Test array
     * @return Number of pairs of integers that sum to 0
     */
    public static int zero_sum(int[] arr) {
        HashMap<Integer, Integer> counts = new HashMap<>();
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            int current = arr[i];

            if (current >= 0 && counts.getOrDefault(-current, 0) > 0) {
                sum++;
                counts.put(-current, counts.get(-current) - 1);
            } else if (current < 0 && counts.getOrDefault(-current, 0) > 0) {
                sum++;
                counts.put(-current, counts.get(-current) - 1);
            } else {
                counts.put(current, counts.getOrDefault(current, 0) + 1);
            }
        }
        return sum;
    }

    /**
     * Searches for the negative of the element, and adds a sum if it exists
     * 
     * @param arr Test array
     * @return Number of pairs of integers that sum to 0
     */
    public static int zero_sum_follow(int[] arr) {
        HashMap<Integer, Integer> counts = new HashMap<>();
        int sum = 0;

        for (int i = 0; i < arr.length; i++) {
            int current = arr[i];

            if (counts.getOrDefault(-current, 0) > 0) {
                sum += counts.get(-current);
            }
            counts.put(current, counts.getOrDefault(current, 0) + 1);
        }
        return sum;
    }
}

/**
 * Initial Question: 20 minutes
 * Follow-up Question: 15 minutes
 */
