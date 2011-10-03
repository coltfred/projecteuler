object project1 extends util.Project{
    def description = "Compute the sum of all numbers that are divisible by 3 or 5 under 1000"
    def solve(args: Array[String]) = println("Answer is " + threeOrFive(0,1000))
    def threeOrFive (from: Int, to: Int): List[Int]= 
        for(i <- List.range(from, to) if(i % 3 == 0 || i % 5 == 0)) yield i

}
