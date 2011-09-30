object project4 extends util.Project{
    def description = "Find the largest palindrome made from the product of two 3-digit numbers."
    def isPal[T](s: T)  = {
        val str = s.toString 
        str == str.reverse
    }
    def solve(args: Array[String]) = {
        val pals = 
            for{
                i <- 100 until 1000
                j <- i until 1000
                val k = i*j if(isPal(k))
            }
            yield k
        println("Answer is " + pals.toList.sort(_ > _).head) 

    }
    
    override def test = {
        verify(isPal("1001"))
        verify(!isPal("1101"))
    }
}
