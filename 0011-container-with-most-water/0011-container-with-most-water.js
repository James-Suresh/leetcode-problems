

/**
 * @param {number[]} height
 * @return {number}
 */
 function maxArea (height) {
  start = 0
  end = height.length - 1;
  //const maxareareached = false
  let width = height.length-1;
  let maxarea = (Math.min(height[start], height[end])) * width;
  let area = 0;
  let counter = 0;

function checkHeight(start, end)
{
   let area = (Math.min(height[start], height[end])) * width;
   if (area > maxarea)
   maxarea=area
}

  while(start<end){
      if(height[start]<=height[end])
      {
          start++
          width--
      }
      else
      {
        end--
        width--
      }
      checkHeight(start, end)
  }

  return(maxarea)
};