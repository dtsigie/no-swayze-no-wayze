library(shiny)

shinyUI(fluidPage(
  titlePanel("Swayze Fever"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Select Colors of interest"),
      
      checkboxGroupInput("colors", "color:",
                         c("Red" = "Red",
                           "Yellow" = "Yellow",
                           "Green" = "Green",
                           "Cyan" = "Cyan",
                           "Blue" = "Blue",
                           "Purple" = "Purple"),
                         selected = c("Red", "Yellow", "Green", "Cyan", "Blue", "Purple"))
                  
      #numericInput("breakNum", "Number of Columns", "5", min = 5, max = 25)
      
      ),
      mainPanel(plotOutput("stream"))
  )
))