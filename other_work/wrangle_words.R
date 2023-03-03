

library(tidyverse)
word_list <- read_csv("https://raw.githubusercontent.com/emmaholt833/SeniorProject/main/datasets/wordfreq.csv")
View(word_list)


bob <- word_list %>%
  filter(nchar(word) >= 4 & nchar(word) <= 10)

View(bob)

write_csv(bob, "updated.csv")



