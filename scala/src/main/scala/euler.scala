object euler {
  val projects = Set[util.Project](project1, project2, project4, project6, project11)

  def main(args: Array[String]) {
    if (args.length == 0) {
      println("\nUsage: euler <projectN> [more args]\n")
      scala.sys.exit(0);
    }
    val projectName = args(0)
    projects.find { _.name == projectName } match {
      case Some(project) =>
        printf("Running %s:\n  %s\n\n", project.name, project.description)
        val startTime = System.currentTimeMillis
        project.run(args.tail)
        printf("\nRun Time: %d ms\n\n", System.currentTimeMillis - startTime)
      case None if "list" == projectName => 
        projects.map{_.name}.foreach{println(_)}
      case None if "all" == projectName => 
        projects.map{_.name}.foreach{(p) => main(p +: args.tail)}
      case None => 
        printf("\nSorry, I couldn't find a project named %s.\n", projectName)
        scala.sys.exit(1)
    }
  }
}
