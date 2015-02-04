#This all stolen from https://gist.github.com/menugget/7864454

#plot.stream makes a "stream plot" where each y series is plotted 
#as stacked filled polygons on alternating sides of a baseline.
#
#Arguments include:
#'x' - a vector of values
#'y' - a matrix of data series (columns) corresponding to x
#'order.method' = c("as.is", "max", "first") 
#  "as.is" - plot in order of y column
#  "max" - plot in order of when each y series reaches maximum value
#  "first" - plot in order of when each y series first value > 0
#'center' - if TRUE, the stacked polygons will be centered so that the middle,
#i.e. baseline ("g0"), of the stream is approximately equal to zero. 
#Centering is done before the addition of random wiggle to the baseline. 
#'frac.rand' - fraction of the overall data "stream" range used to define the range of
#random wiggle (uniform distrubution) to be added to the baseline 'g0'
#'spar' - setting for smooth.spline function to make a smoothed version of baseline "g0"
#'col' - fill colors for polygons corresponding to y columns (will recycle)
#'border' - border colors for polygons corresponding to y columns (will recycle) (see ?polygon for details)
#'lwd' - border line width for polygons corresponding to y columns (will recycle)
#'...' - other plot arguments
load ('moviesDF.rda')
plot.stream <- function(
  x, y, 
  order.method = "max", frac.rand=0.001, spar=0.4,
  center=TRUE,
  ylab="Relative Frequency of Colors", xlab="Year of Movie Release",  
  border = NULL, lwd=1, 
  col = rainbow(length(y[1,])),
  ylim=NULL, 
  ...
){
  
  if(sum(y < 0) > 0) error("y cannot contain negative numbers")
  
  if(is.null(border)) border <- par("fg")
  border <- as.vector(matrix(border, nrow=ncol(y), ncol=1))
  col <- as.vector(matrix(col, nrow=ncol(y), ncol=1))
  lwd <- as.vector(matrix(lwd, nrow=ncol(y), ncol=1))
  
  if(order.method == "max") {
    ord <- order(apply(y, 2, which.max))
    y <- y[, ord]
    col <- col[ord]
    border <- border[ord]
  }
  
  if(order.method == "first") {
    ord <- order(apply(y, 2, function(x) min(which(r>0))))
    y <- y[, ord]
    col <- col[ord]
    border <- border[ord]
  }
  
  bottom.old <- x*0
  top.old <- x*0
  polys <- vector(mode="list", ncol(y))
  for(i in seq(polys)){
    if(i %% 2 == 1){ #if odd
      top.new <- top.old + y[,i]
      polys[[i]] <- list(x=c(x, rev(x)), y=c(top.old, rev(top.new)))
      top.old <- top.new
    }
    if(i %% 2 == 0){ #if even
      bottom.new <- bottom.old - y[,i]
      polys[[i]] <- list(x=c(x, rev(x)), y=c(bottom.old, rev(bottom.new)))
      bottom.old <- bottom.new
    }
  }
  
  ylim.tmp <- range(sapply(polys, function(x) range(x$y, na.rm=TRUE)), na.rm=TRUE)
  outer.lims <- sapply(polys, function(r) rev(r$y[(length(r$y)/2+1):length(r$y)]))
  mid <- apply(outer.lims, 1, function(r) mean(c(max(r, na.rm=TRUE), min(r, na.rm=TRUE)), na.rm=TRUE))
  
  #center and wiggle
  if(center) {
    g0 <- -mid + runif(length(x), min=frac.rand*ylim.tmp[1], max=frac.rand*ylim.tmp[2])
  } else {
    g0 <- runif(length(x), min=frac.rand*ylim.tmp[1], max=frac.rand*ylim.tmp[2])
  }
  
  fit <- smooth.spline(g0 ~ x, spar=spar)
 #print(g0)
 out1 = list() 
 
 for(i in seq(polys)){
    
    polys[[i]]$y <- polys[[i]]$y + c(fit$y, rev(fit$y))
   # out1[[i]] <- spline(polys[[i]],method="periodic")
   
  }


# print(polys)
# print(out1)  

  
  if(is.null(ylim)) ylim <- range(sapply(polys, function(x) range(x$y, na.rm=TRUE)), na.rm=TRUE)
par(mar = c(6.5, 6.5, 4, 2))
plot(x,y[,1], ylab=ylab, xlab=xlab,cex.lab=1.5, ylim=ylim, t="n", ...,axes=FALSE,mgp = c(5, 2.5, 1), main = "Streamgraph of Relative Color Frequencies of Patrick Swayze Movies Chronologically",cex.main=2.0)
for(i in seq(polys)){
  polygon(polys[[i]], border=border[i], col=col[i], lwd=lwd[i])
}
axis(1, at=1:30,labels=moviesDF$year[1:30], col.axis="black", las=2,cex.axis=1.2)
axis(2,cex.axis=1.2)
grid(30, NULL, col="lightgrey", lty="solid", lwd=0.9)

}
