# server.R

load("joined.rdata")
library(stringr)
library(shiny)
library(scatterplot3d)

shinyServer(

  function(input, output) {
    cubedraw <- function(res3d, min = 0, max = 255, cex = 2)
    {
      cube01 <- rbind(0,c(1,0,0),c(1,1,0),1,c(0,1,1),c(0,0,1),c(1,0,1),
                      c(1,0,0),c(1,0,1),1,c(1,1,0),
                      c(0,1,0),c(0,1,1), c(0,1,0),0)
      cub <- min + (max-min)* cube01
      res3d$points3d(cub[ 1:11,], cex = cex, type = 'b', lty = 1)
      res3d$points3d(cub[11:15,], cex = cex, type = 'b', lty = 3)
    }
    
      #outputs histogram 
      output$hist <- renderPlot({
        #reactive elements (keyword input)
        
        #put search in lowercase
        keyL <- tolower(input$key)
        
        #split search into multiple strings
        keySplit <- str_extract_all(keyL, "[a-z]+")
        
        #puts the search strings into a vector
        keySplit <- unlist(keySplit)
        
        #matches keywords to rows
        #stringToMatch <- paste(keySplit, collapse="|")
        stringToMatch <- paste( keySplit, collapse=")(?=.*")
        stringToMatch <- paste("^(?=.*", stringToMatch, ").*$", sep="")
        
        matched <- joined[grep(stringToMatch,joined$title, perl=TRUE),]
        #matched <- joined[grep(stringToMatch,joined$title),]
        
        #if(length(matched$color) < (as.numeric(input$breakNum)/2)){
        #  hist(0, border = 'white', xlab = "Hue Value", ylab = "Precentage", main = "The various colors of Swayze", xlim = c(0, 1), ylim = c(0,1))
        #} else {
        
          relevantCol <- matched$color
          sevens <- relevantCol[which(nchar(relevantCol)==7)]
          rgbCol <- col2rgb(sevens)
          hsvCol <- rgb2hsv(rgbCol[1,], g=rgbCol[2,], b=rgbCol[3,])
          
          #sort hsv data
          colSort <- data.frame(x=1:length(hsvCol[1,]))
          
          colSort$h <- hsvCol[1,]
          colSort$s <- hsvCol[2,]
          colSort$v <- hsvCol[3,]
          colSort <- colSort[,-1]
          
          colSort <- colSort[with(colSort, order(h)), ]
    
          means <- vector(mode = "numeric", length = as.numeric(input$breakNum))
          
          breaking <- seq(from = 0, to = 1, by = 1/as.numeric(input$breakNum))
          segys <- vector(mode = "numeric", length = length(colSort$h))
          
          
          #add a new variable to colSort that catagoriezes the colors
          for(l in 1:length(colSort$h)){
            if (colSort$h[l] < breaking[1]) {
              segys[l] <- breaking[1]
            
            } else{
                for (j in 1:length(breaking)){
                  if((colSort$h[l] < breaking[j]) && (colSort$h[l] > breaking[j-1])){
                    segys[l] <- breaking[j]
                  }
                }
              }
          }
          colSort$segys <- segys
          
          seg <- 1
          #take multiple means and place them in vector
          for(j in 1:(as.numeric(input$breakNum))){
            if (length(colSort$h[which(breaking[j+1] == colSort$segys)]) == 0) {
              means[j] <- 0
            } else {
              means[j] <- mean(colSort$h[which(breaking[j+1] == colSort$segys)])
            }
          }
          
          columnCol <- hsv(h = means, s = 0.9, v = 0.9)
          
          if (input$type == "Histogram") {
            h <- hist(colSort$h, breaks = seq(from = 0, to = 1, by = 1/as.numeric(input$breakNum)), freq = FALSE, col = columnCol, 
                 border = 'white', xlab = "Hue Value", ylab = "Frequency", main = "The Various Colors of Swayze")
            h$counts = h$counts/sum(h$counts)
            max <- max(h$counts)+0.02
            plot(h, col = columnCol, border = 'white', xlab = "Hue Value", ylab = "Relative Frequency", 
                 main = "The various colors of Swayze",cex.main=2.0, ylim = c(0, max),cex.lab=1.5,cex.axis =1.3)
          } else if (input$type == "Average Color"){
            hist(1, border = "white", col = hsv(h = mean(colSort$h), s = mean(colSort$s), v = mean(colSort$v)), 
                 main = "Average Color", xlab = "", ylab = "" )
          }
          else if (input$type == "3d Scatter Plot") {
            #relevantCol <- matched$color
            #sevens <- relevantCol[which(nchar(relevantCol)==7)]
            #rgbCol <- col2rgb(sevens)
            
            crgb <- t(rgbCol)
            rr <- scatterplot3d(crgb, color = sevens, box = FALSE, angle = input$angle)
            cubedraw(rr)
          }
        #}
        
      })

})
