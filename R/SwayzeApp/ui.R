library(shiny)

shinyUI(fluidPage(
  titlePanel("Swayze Fever"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Search Swayze by keyword"),
      
      #creates a text input in ui
      textInput("key", "Keywayze", "roadhouse"),
      
      selectInput("breakNum", "Number of Columns", c(3:25)),
      
      sliderInput("angle", "Angle:",
                  min = 0, max = 360, value = 24),
      
      selectInput("type", "Histogram or Average Color", c("Histogram", "Average Color", "3d Scatter Plot")),
      
      submitButton("search")
                  
      #numericInput("breakNum", "Number of Columns", "5", min = 5, max = 25)
      
      ),
      mainPanel(plotOutput("hist"))
  )
))