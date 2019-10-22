package codingBats;

public class Bats {

	public static void main(String[] args) {
		System.out.println(makeBricks(3, 2, 9));
	}

	
//	We want to make a row of bricks that is goal inches long. 
//	We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
//	Return true if it is possible to make the goal by choosing from the given bricks. 
//	This is a little harder than it looks and can be done without any loops	
	public static boolean makeBricks(int small, int big, int goal) {
		  boolean can = false;
		  
		  int totSmall = small * 1;
		  int totBig = big * 5;
		  
		  if (totBig == goal) can = true;
		  else if (totBig < goal) {
		    if (totBig + totSmall >= goal) can = true;
		  }
		  else if (totBig > goal) {
		    if (goal % 5 == 0) can = true;
		    else if (goal % 5 != 0) {
		      int rest = goal % 5;
		      if (totSmall >= rest) can = true;
		    }
		  }
		  return can;
		}
}
