# 📊 Some Statistics for the Dataset

## 🔍 Data Splits Statistics

The table below shows the number of records for each data split and record type:

| Split  | Record Type | Language | Record Count |
|--------|-------------|----------|--------------|
| Train  | Article     | en       | 937          |
|        |             | de       | 5            |
|        | Book        | de       | 25,768       |
|        |             | en       | 23,698       |
|        | Conference  | en       | 3,306        |
|        |             | de       | 1,971        |
|        | Report      | en       | 1,222        |
|        |             | de       | 1,195        |
|        | Thesis      | de       | 8,767        |
|        |             | en       | 3,764        |
| Dev    | Article     | en       | 159          |
|        |             | de       | 1            |
|        | Book        | de       | 4,375        |
|        |             | en       | 3,959        |
|        | Conference  | en       | 564          |
|        |             | de       | 322          |
|        | Report      | en       | 202          |
|        |             | de       | 178          |
|        | Thesis      | de       | 1,451        |
|        |             | en       | 630          |
| Test   | Article     | en       | 329          |
|        |             | de       | 1            |
|        | Book        | de       | 9,802        |
|        |             | en       | 5,809        |
|        | Conference  | de       | 804          |
|        |             | en       | 626          |
|        | Report      | de       | 376          |
|        |             | en       | 271          |
|        | Thesis      | de       | 2,831        |
|        |             | en       | 740          |


## 📝 Abstract Statistics

The table below shows the minimum, maximum, and mean length of abstracts in different data splits:

| Split  | Record Type | Language | Min | Max  | Mean  |
|--------|-------------|----------|-----|------|-------|
| Train  | Article     | de       | 22  | 139  | 66.0  |
|        |             | en       | 9   | 626  | 156.8 |
|        | Book        | de       | 8   | 1776 | 148.0 |
|        |             | en       | 8   | 3000 | 174.5 |
|        | Conference  | de       | 7   | 1045 | 145.5 |
|        |             | en       | 13  | 1617 | 169.2 |
|        | Report      | de       | 8   | 884  | 121.2 |
|        |             | en       | 7   | 667  | 92.0  |
|        | Thesis      | de       | 6   | 3325 | 171.0 |
|        |             | en       | 6   | 1859 | 179.2 |
| Dev    | Article     | de       | 23  | 23   | 23.0  |
|        |             | en       | 11  | 453  | 159.2 |
|        | Book        | de       | 10  | 1117 | 146.6 |
|        |             | en       | 10  | 1878 | 173.8 |
|        | Conference  | de       | 12  | 667  | 146.5 |
|        |             | en       | 14  | 1152 | 163.6 |
|        | Report      | de       | 10  | 758  | 125.2 |
|        |             | en       | 8   | 428  | 85.7  |
|        | Thesis      | de       | 9   | 1130 | 170.9 |
|        |             | en       | 7   | 1133 | 181.0 |
| Test   | Article     | de       | 186 | 186  | 186.0 |
|        |             | en       | 16  | 513  | 160.7 |
|        | Book        | de       | 8   | 1731 | 139.5 |
|        |             | en       | 12  | 2115 | 172.3 |
|        | Conference  | de       | 10  | 808  | 141.8 |
|        |             | en       | 17  | 867  | 173.6 |
|        | Report      | de       | 10  | 551  | 119.3 |
|        |             | en       | 11  | 829  | 96.9  |
|        | Thesis      | de       | 6   | 1705 | 156.0 |
|        |             | en       | 9   | 1149 | 181.3 |

For more insights into dataset statistics, visit the `data-statistics` subfolder. The dataset can be downloaded from the `data` subfolder.
