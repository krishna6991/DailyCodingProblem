//find the smallest missing number from an unsorted array, can have duplicate elements in array
//time complexity o(n) and space complexity o(1)

#include<bits/stdc++.h>
using namespace std;

void swap(int *a, int *b){
  int temp;
  temp = *a;
  *a = *b;
  *b =temp;
}

int removeNegativeNumber(int arr[], int size){
  int j=0;
  for(int i=0; i<size; i++){
      if(arr[i]<=0){
        swap(&arr[i], &arr[j]);
        j++;
      }
  }
  return j;
}

int missingSmallestPositiveUtil(int arr[], int size){
  for(int i =0; i<size;i++){
    if(abs(arr[i])-1 < size && arr[abs(arr[i])- 1] > 0)
      arr[abs(arr[i])-1] = -arr[abs(arr[i]) - 1];
  }
  for(int i=0;i<size;i++)
    if(arr[i]>0)
      return i+1;
    return size+1;
}

int missingSmallestPositive(int arr[], int size){
  int border = removeNegativeNumber(arr,size);
  return missingSmallestPositiveUtil(arr+border, size-border);
}
int main(){
  int arr[] = {0, 10, 2, -10, -20, 1,5,20, -6};
  int size = sizeof(arr)/sizeof(arr[0]);
  int missing = missingSmallestPositive(arr, size);
  cout<<"The smallest positive missing number is: "<<missing<<endl;
  return 0;

}
