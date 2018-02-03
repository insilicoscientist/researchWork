#### NIH data analysis
## 2017-03-14
library("dplyr")
library("ggplot2")
library("reshape2")
library("gridExtra")
library("scales")
##********************************************************************************###
## Faceted boxplot and lineplot 
##********************************************************************************###
##-----------------------------------------------------------------------------------
## Data processing
#To remove all objection from session
rm(list = ls())

# Read data
df.01 <- read.csv2("final_extractWords_count_data.csv", header=T, sep="," )
df.01 <- df.01[,-c(2)]
summary(df.01)
str(df.01)

# Transpose
t.df.01 = setNames(data.frame(t(df.01[,-1])), df.01[,1])

##Transpose dataframe with setting first column to column header names
t.df.01b <- as.data.frame(t(df.01))

#Save data
write.table(t.df.01, "final_extractWords_count_data_transposed.csv", sep=",", quote=T, row.names=T)
##-----------------------------------------------------------------------------------
## lineplot-1

##----
##ggplot

# Read data
df.02 <- read.csv2("NIH_Grant_Analysis_extractWords_count_data.csv", header=T, sep=",", check.names=F, strip.white=T, stringsAsFactors=FALSE)
str(df.02)

# reshape dat for ggplot
df.02.mlt <- melt(df.02, id.vars="YEAR")

ggplot(df.02.mlt, aes(x=YEAR, y=value, group=variable)) +  
  geom_line() + # request box plot 
  facet_wrap(~ variable
             , scales="free_y"
             , ncol=5) + # use facet to plot all figures in one page; ncol will assign number of columns
  scale_x_continuous(breaks=pretty_breaks()) + # specify number of tick marks, e.g n=3 or leave blank
  scale_y_continuous(breaks=pretty_breaks()) + # specify number of tick marks
  theme( axis.text.x=element_text(size=8, angle=90, hjust=1, vjust=0.5, family="sans")
         #axis.text.x=element_blank()
         ,axis.text.y=element_text(size=8, angle=0, hjust=1, vjust=0.5, family="sans")
         #,axis.text.y=element_blank()
         #
         #,axis.title.x=element_text(color="black", size=10, face="bold")
         #,axis.title.x=element_blank()
         #,axis.title.y=element_text(color="black", size=14, face="bold")
         #,axis.title.y=element_blank() 
         #,plot.title=element_text(color="black", size=12, face="bold")
         #
         #,axis.line=element_blank()
         #,axis.ticks=element_blank()
         #,legend.position="none"
         #,panel.background=element_blank()
         ,panel.background = element_rect(fill='whitesmoke', colour='black')
         #,panel.border=element_blank()
         #,panel.grid.major=element_blank()
         #,panel.grid.major=element_line(colour="red", linetype="dotted")
         #,panel.grid.minor=element_blank()
         #,panel.grid.minor=element_line(colour="red", linetype="dotted")
         #
         #,plot.background=element_blank() 
         #,plot.background = element_rect(fill = "gray90")
         ,strip.text = element_text(size=6, face="italic") # facet labels in italics
         #,strip.background = element_blank(), strip.placement = "outside"
         ,strip.background = element_rect(fill='gray90', colour='black'), strip.placement = "outside"
  ) +
  #labs(x="YEAR",y="COUNT") + # add x,y axis labels
  xlab("YEAR") +
  ylab("COUNT") +
  ggtitle("Trends in the research of bacterial species") # add a title


# Save as figure
ggsave("NIH_linePolt-facet-1.png", width=8, height=20, dpi=300)
##-----------------------------------------------------------------------------------
