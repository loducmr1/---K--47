input<-mtcars[,c("mpg","wt","disp","hp")]
input
Model<-lm(mpg~wt+disp+hp,data=input)
print(Model)
