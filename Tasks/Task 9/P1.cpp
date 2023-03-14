class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        //size of vector
        long n;
        n = arr.size();

        //getting the maximum number relative to the second to last element
        //i.e the last element
        // and setting the last element to -1
        long maxNum = arr[n - 1];
        arr [n - 1] = -1;

        //iterating from second to last to first element
        //if the number is bigger than the maximum number 
        //keep the number in a temp variable and
        //set the number to max number and set max number to temp
        //else set the number to max number and continue
        for (int i = n - 2; i>=0 ; i--){
            if (arr[i] > maxNum){
                long temp;
                temp = arr[i];
                arr[i] = maxNum;
                maxNum = temp;
            }
            else{
                arr[i] = maxNum;
            }
        }

        
       return arr; 
    }
    
        
    
};