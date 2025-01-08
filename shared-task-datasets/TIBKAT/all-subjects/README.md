# 📊 Some Statistics for the Dataset

## 🔍 Data Splits Statistics

The table below shows the number of records for each data split and record type:

| Split  | Record Type | Language | Record Count |
|--------|-------------|----------|--------------|
| Train  | Article     | en       | 1,042        |
|        |             | de       | 6            |
|        | Book        | de       | 33,401       |
|        |             | en       | 26,966       |
|        | Conference  | en       | 3,619        |
|        |             | de       | 2,210        |
|        | Report      | de       | 1,507        |
|        |             | en       | 1,275        |
|        | Thesis      | de       | 8,459        |
|        |             | en       | 3,452        |
| Dev    | Article     | en       | 173          |
|        |             | de       | 1            |
|        | Book        | de       | 5,589        |
|        |             | en       | 4,482        |
|        | Conference  | en       | 601          |
|        |             | de       | 371          |
|        | Report      | de       | 256          |
|        |             | en       | 215          |
|        | Thesis      | de       | 1,404        |
|        |             | en       | 574          |
| Test   | Article     | en       | 523          |
|        |             | de       | 3            |
|        | Book        | de       | 17,923       |
|        |             | en       | 13,840       |
|        | Conference  | en       | 1,837        |
|        |             | de       | 1,150        |
|        | Report      | de       | 786          |
|        |             | en       | 653          |
|        | Thesis      | de       | 4,303        |
|        |             | en       | 1,739        |


## 📝 Abstract Statistics

The table below shows the minimum, maximum, and mean length of abstracts in different data splits:

| Split  | Record Type | Language | Min | Max  | Mean  |
|--------|-------------|----------|-----|------|-------|
| Train  | Article     | de       | 22  | 237  | 91.7  |
|        |             | en       | 11  | 626  | 155.8 |
|        | Book        | de       | 8   | 1,776| 143.5 |
|        |             | en       | 1   | 5,101| 174.7 |
|        | Conference  | de       | 7   | 1,217| 144.1 |
|        |             | en       | 13  | 1,617| 168.6 |
|        | Report      | de       | 8   | 884  | 122   |
|        |             | en       | 9   | 901  | 94.3  |
|        | Thesis      | de       | 6   | 2,311| 167.4 |
|        |             | en       | 7   | 1,859| 183.8 |
| Dev    | Article     | de       | 107 | 107  | 107   |
|        |             | en       | 9   | 378  | 155.7 |
|        | Book        | de       | 11  | 1,221| 143.5 |
|        |             | en       | 10  | 1,679| 170.3 |
|        | Conference  | de       | 15  | 778  | 145.3 |
|        |             | en       | 18  | 1,298| 165.4 |
|        | Report      | de       | 10  | 394  | 114.3 |
|        |             | en       | 8   | 534  | 93.7  |
|        | Thesis      | de       | 8   | 3,325| 170.5 |
|        |             | en       | 8   | 1,133| 185.9 |
| Test   | Article     | de       | 34  | 186  | 119.7 |
|        |             | en       | 12  | 513  | 155.5 |
|        | Book        | de       | 8   | 1,731| 141.1 |
|        |             | en       | 8   | 3,000| 173.3 |
|        | Conference  | de       | 10  | 808  | 144.3 |
|        |             | en       | 15  | 1,773| 172.3 |
|        | Report      | de       | 8   | 551  | 117.4 |
|        |             | en       | 7   | 829  | 94.4  |
|        | Thesis      | de       | 6   | 1,705| 165.8 |
|        |             | en       | 6   | 1,752| 184.6 |

For more insights into dataset statistics, visit the `data-statistics` subfolder. The dataset can be downloaded from the `data` subfolder.
