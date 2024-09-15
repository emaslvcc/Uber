
/**
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

import java.util.HashMap;

public class FirstOccurrence {

    public static String test1 = "abracadabra";
    public static String test2 = "Uber Career Prep";
    public static String test3 = "zzyzx";

    public static void main(String[] args) {
        System.out.println("Result for test 1: " + first_occurrence(test1));
        System.out.println("Result for test 2: " + first_occurrence(test2));
        System.out.println("Result for test 3: " + first_occurrence(test3));
    }

    /**
     * Adds until element's count is higher than 1
     * 
     * @param arr Test array
     * @return Sum of unique elements in the array
     */
    public static String first_occurrence(String str) {
        HashMap<Character, Integer> counts = new HashMap<>();
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < str.length(); i++) {
            char current = str.charAt(i);

            if (counts.getOrDefault(current, 0) == 0) {
                result.append(current);
            }
            counts.put(current, counts.getOrDefault(current, 0) + 1);
        }
        return result.toString();
    }
}

/**
 * Question: 10 minutes
 */
