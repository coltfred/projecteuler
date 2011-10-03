import util.funcs
object project2 extends util.Project{
    def description = "By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."
    def solve(args: Array[String]) = println("Answer is " + funcs.fib.filter(_ % 2 == 0).takeWhile(_ < 4000000).foldLeft(BigInt(0))(_+_))

}
