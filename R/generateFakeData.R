source("dbtest.R")
library("RMySQL")


random_hex <- function() {
  r <- runif(1, min=0, max=255)
  r <- round(r)
  r <- as.hexmode(r)
  return(r)
}

random_color <- function() {
  r <- as.character(random_hex())
  g <- as.character(random_hex())
  b <- as.character(random_hex())
  return(paste("#",r,g,b, sep=""))
}

#Number of random Swayzes to generate.
n <- 100
for (i in 1:n) {
  swaykeys <- c("patrick", "swayze", "roadhouse", "ghost", "point break")
  
  n_keywords <- 2 + round(runif(1,min=0,max=2))
  sample_swayze <- sample(swaykeys, n_keywords)
  
  url <- paste(sample(swaykeys, 1),".com", sep="")
  title <- paste(sample_swayze, collapse= " ")
  fake = 1
  
  query <- sprintf("INSERT INTO swayze (url, title, fake) VALUES ('%s', '%s', %d)",
                   url, title, fake)
  insert <- dbSendQuery(con, query)
  lastId = dbGetQuery(con, "SELECT LAST_INSERT_ID() as id;")
  lastId <- lastId$id

  n_colors <- 2 + round(runif(1,min=0,max=2))
  for (i in 1:n_colors) {
    query = sprintf("INSERT INTO colors (swayze_id, color, frequency, fake) VALUES (%d, '%s', %d, %d)",
                  lastId, random_color(), 0.0, fake);
    insert <- dbSendQuery(con, query)    
  }

}
