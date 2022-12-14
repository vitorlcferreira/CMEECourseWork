#!usr/bin/env Rscript

##------------------------------------------
## Name: Girko.R
## Description: This script builds Girko's circular law function and 
##              creates a plot of it
## Author: Vitor Ferreira, f.ferreira22@imperial.ac.uk
## Date: October 2022
## Inputs: none
## Outputs: Girko.pdf
##------------------------------------------


# Clean enviroment
rm(list = ls())

# Clear graphics
graphics.off()

# Load Libraries
suppressMessages(require(tidyverse, quietly = T))

# Define Girko's circular law function
build_ellipse <- function(hradius, vradius){ # function that returns an ellipse
  npoints = 250
  a <- seq(0, 2 * pi, length = npoints + 1)
  x <- hradius * cos(a)
  y <- vradius * sin(a)  
  return(data.frame(x = x, y = y))
}


# Defining parameters

N <- 250

M <- matrix(rnorm(N * N), N, N) # Building the matrix

eigvals <- eigen(M)$values # Find the eigenvalues

eigDF <- data.frame("Real" = Re(eigvals), "Imaginary" = Im(eigvals)) # Build a dataframe

my_radius <- sqrt(N) # The radius of the circle is sqrt(N)

ellDF <- build_ellipse(my_radius, my_radius) # Dataframe to plot the ellipse

names(ellDF) <- c("Real", "Imaginary") # renaming columns


# plot the eigenvalues
p <- ggplot(eigDF, aes(x = Real, y = Imaginary))
p <- p +
  geom_point(shape = I(3)) +
  theme(legend.position = "none")


# now add the vertical and horizontal line
p <- p + geom_hline(aes(yintercept = 0))
p <- p + geom_vline(aes(xintercept = 0))


# finally, add the ellipse
p <- p + geom_polygon(data = ellDF, aes(x = Real, y = Imaginary, alpha = 1/20, fill = "red"))

pdf("../results/Girko.pdf")
print(p)
graphics.off()
