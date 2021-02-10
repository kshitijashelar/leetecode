package autodesk;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/*
 *Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
 *Find all the elements of [1, n] inclusive that do not appear in this array.
 *Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
 *Example:
 *
 *Input:
 *[4,3,2,7,8,2,3,1]
 *Output:
 *[5,6]
*/
class DisappearingNum {
	public List<Integer> findDisappearedNumbers(int[] nums) {
		ArrayList<Integer> finalArr = new ArrayList<>();
		HashMap<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < nums.length; i++) {

			map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);

		}

		for (int i = 1; i <= nums.length; i++) {
			if (!map.containsKey(i)) {
				finalArr.add(i);
			}
		}
		return finalArr;
	}

	public static void main(String[] args) {
		DisappearingNum num = new DisappearingNum();
		int[] arr = { 4, 3, 2, 7, 8, 2, 3, 1 };
		System.out.println(num.findDisappearedNumbers(arr));
	}
}