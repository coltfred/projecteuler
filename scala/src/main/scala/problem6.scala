import util.funcs
object project6 extends util.Project{
    def description = "Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."
    def solve(args: Array[String]) = {
        val nums = 1.to(100)
        val squareOfSums = math.pow(nums.foldLeft(0)(_+_), 2)
        println("Square of sums is " + squareOfSums)
        val sumOfSquares = nums.map(math.pow(_,2)).sum
        println("Sum of squares is " + sumOfSquares)

        println("Answer is " + (squareOfSums - sumOfSquares))
    }
}
