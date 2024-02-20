Solution sol = new Solution();
int[] nums = { 1, 2 };
int result = sol.RemoveDuplicates(nums);
Console.WriteLine(result);

public class Solution
{
    public int RemoveDuplicates(int[] nums)
    {
        var stack = new Stack<int>();
        int prev = nums[0];
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] != prev)
            {
                stack.Push(nums[i]);
            }
            Console.WriteLine(string.Format("{0}  {1}", prev, nums[i]));
            // Console.WriteLine(stack[i]);
            prev = nums[i];
        }
        return prev;
    }
    public string s = "hi";
}