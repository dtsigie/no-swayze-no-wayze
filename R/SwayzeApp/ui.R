library(shiny)

shinyUI(fluidPage(
  titlePanel("Swayze Fever"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Search Swayze by keyword"),
      
      #creates a text input in ui
      textInput("key", "Keywayze", "roadhouse"),
      
      selectInput("breakNum", "Number of Columns (for Histogram)", c(3:25)),
      
      sliderInput("angle", "Angle (for 3d Scatter Plot)",
                  min = 0, max = 360, value = 24),
      
      selectInput("type", "What do you want to display?", c("Histogram", "Average Color", "3d Scatter Plot"))
      
      # submitButton("search")
                  
      #numericInput("breakNum", "Number of Columns", "5", min = 5, max = 25)
      
      ),
      mainPanel(plotOutput("hist"))
  )
))