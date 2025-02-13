// Time - O(nlogn), Memory - O(n)
var carFleet = function(target, position, speed) {
  let i = 0;
  const positionSpeedList = [];
  while(i < position.length) {
      positionSpeedList.push([position[i], speed[i]]);
      i++;
  }

  const sortedPositionSpeedList = positionSpeedList.sort((a,b) => b[0] - a[0]);
  const stack = [];

  for(const pair of sortedPositionSpeedList) {
      const timeTakenToReachDestination = (target - pair[0])/pair[1];
      // stack.push(timeTakenToReachDestination);
      // if(stack.length >= 2 && stack[stack.length - 1] <= stack[stack.length - 2]) {
      //     stack.pop();
      // }
    if(stack.length === 0) {
      stack.push(timeTakenToReachDestination);
    } else if(stack.length >= 1 && timeTakenToReachDestination > stack[stack.length - 1]) {
      stack.push(timeTakenToReachDestination);
    }
  }

  return stack.length;
};

console.log(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]));

// Python
/**
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = []
        for i in range(len(speed)):
            temp.append([position[i], speed[i]])
        temp = sorted(temp, key=lambda x: x[0], reverse=True)
        stack = []
        for array in temp:
            [position, speed] = array
            time = (target - position) / speed
            if not stack :
                stack.append(time)
            elif len(stack) >= 1 and time > stack[-1]:
                stack.append(time)
        return len(stack)
 */