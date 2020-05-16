import math

def bisection(low, high, iteration):
     root = 1e-4
     for i in range(iteration):

          tolerance = high - low

          res_midpoint = (low + high) / 2

          result = math.pow(res_midpoint, 3) + (4 * math.pow(res_midpoint, 2)) - 10

          if tolerance < root: 
               break
          if result > 0:
               high = res_midpoint
          else:
               low = res_midpoint

          print('Iteration {} \t a: {:.5f} \t b: {:.5f} \t midpoint : {:.5f} \t f(p): {:.6f} \t Tolerance: :{:.5f}'.format(i+1,low,high,res_midpoint,result, tolerance))

     return "Bisected!"

if __name__ == '__main__':
     bisection(1,2,50)