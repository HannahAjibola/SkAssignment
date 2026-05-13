public class perfectSquare{

    public static boolean ps(int[][]nums){
        
        for(int i = 0; i < nums.length; i++){
        int row = 0;
        int column = 0;


            for(int j = 0; i < nums.length; i++){
                row += nums[i][j];
                column += nums[j][i];
            
            }
                if(row != column){
                    return false;    
                }
            }
            return true;
 }  
    
    public static void main(String[] args){
        int[][] nums = {{2,4,5},
                        {3,3,5},
                        {6,4,1}};

        boolean result = ps(nums);

        System.out.print(result);
    }
}
