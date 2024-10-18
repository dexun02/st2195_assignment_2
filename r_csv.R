library(rvest)
library(readr)
url <- "https://en.wikipedia.org/wiki/Comma-separated_values"
page <- read_html(url)
csv_example <- page %>%
  html_nodes("pre") %>%
  html_text()
write_file(csv_example, "cars_data.csv")
cat("CSV data saved to 'cars_data.csv'")
csv_example
