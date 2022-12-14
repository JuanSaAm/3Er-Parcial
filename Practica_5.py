currentPoint = initialPoint    // the zero-magnitude vector is common
   stepSize = initialStepSizes    // a vector of all 1's is common
   acceleration = someAcceleration // a value such as 1.2 is common
   candidate[0] = -acceleration
   candidate[1] = -1 / acceleration
   candidate[2] = 0
   candidate[3] = 1 / acceleration
   candidate[4] = acceleration
   loop do
      before = EVAL(currentPoint)
      for each element i in currentPoint do
         best = -1
         bestScore = -INF

         for j from 0 to 4         // try each of 5 candidate locations
            currentPoint[i] = currentPoint[i] + stepSize[i] * candidate[j]
            temp = EVAL(currentPoint)
            currentPoint[i] = currentPoint[i] - stepSize[i] * candidate[j]
            if(temp > bestScore)
                 bestScore = temp
                 best = j
         if candidate[best] is not 0
            currentPoint[i] = currentPoint[i] + stepSize[i] * candidate[best]
            stepSize[i] = stepSize[i] * candidate[best] // accelerate
      if (EVAL(currentPoint) - before) < epsilon 
         return currentPoint
