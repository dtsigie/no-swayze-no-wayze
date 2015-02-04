# server.R


library(stringr)
library(shiny)
source("helpers.R")
#load("joined.rdata")
load('swayzeMovie.rdata')


shinyServer(
  function(input, output) {
      #outputs histogram 
      output$stream <- renderPlot({
        colors = input$colors

        moviesWithColors = swayzeMovie[,(names(swayzeMovie) %in% colors)]
        x = seq(28)
        y = as.matrix(moviesWithColors)
        plot.stream(x,y, col=names(moviesWithColors))
      })

})
