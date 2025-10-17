# 📊 Some Statistics for the Dataset

## 🔍 Data Splits Statistics

The table below shows the number of records for each data split and record type:

| Split  | Record Type | Language | Record Count |
|--------|-------------|----------|--------------|
| Train  | Article     | en       | 250          |
|        |             | de       | 3            |
|        | Book        | en       | 13,080       |
|        |             | de       | 8,998        |
|        | Conference  | en       | 2,097        |
|        |             | de       | 626          |
|        | Report      | en       | 718          |
|        |             | de       | 530          |
|        | Thesis      | de       | 3,499        |
|        |             | en       | 2,242        |
| Dev    | Article     | en       | 40           |
|        |             | de       | 1            |
|        | Book        | en       | 2,198        |
|        |             | de       | 1,497        |
|        | Conference  | en       | 358          |
|        |             | de       | 99           |
|        | Report      | en       | 120          |
|        |             | de       | 82           |
|        | Thesis      | de       | 585          |
|        |             | en       | 374          |
| Test   | Article     | en       | 34           |
|        | Book        | en       | 1,971        |
|        |             | de       | 1,426        |
|        | Conference  | en       | 327          |
|        |             | de       | 97           |
|        | Report      | en       | 107          |
|        |             | de       | 78           |
|        | Thesis      | de       | 525          |
|        |             | en       | 345          |


## 📝 Abstract Statistics

The table below shows the minimum, maximum, and mean length of abstracts in different data splits:

| Split  | Record Type | Language | Min | Max   | Mean   |
|--------|-------------|----------|-----|-------|--------|
| Train  | Article     | de       | 22  | 139   | 65.0   |
|        |             | en       | 9   | 396   | 142.6  |
|        | Book        | de       | 11  | 1574  | 155.9  |
|        |             | en       | 8   | 3000  | 174.9  |
|        | Conference  | de       | 11  | 791   | 140.7  |
|        |             | en       | 15  | 1381  | 168.5  |
|        | Report      | de       | 8   | 684   | 122.6  |
|        |             | en       | 7   | 667   | 87.5   |
|        | Thesis      | de       | 6   | 3325  | 188.4  |
|        |             | en       | 6   | 1752  | 180.9  |
| Dev    | Article     | de       | 23  | 23    | 23.0   |
|        |             | en       | 11  | 453   | 148.9  |
|        | Book        | de       | 10  | 709   | 152.4  |
|        |             | en       | 11  | 1878  | 175.7  |
|        | Conference  | de       | 12  | 560   | 145.1  |
|        |             | en       | 14  | 1152  | 162.5  |
|        | Report      | de       | 10  | 758   | 146.4  |
|        |             | en       | 10  | 428   | 84.2   |
|        | Thesis      | de       | 9   | 1130  | 178.5  |
|        |             | en       | 7   | 1025  | 176.2  |
| Test   | Article     | en       | 27  | 283   | 131.2  |
|        | Book        | de       | 10  | 997   | 152.0  |
|        |             | en       | 12  | 1548  | 176.5  |
|        | Conference  | de       | 15  | 396   | 135.6  |
|        |             | en       | 17  | 867   | 170.2  |
|        | Report      | de       | 11  | 262   | 120.7  |
|        |             | en       | 11  | 408   | 70.0   |
|        | Thesis      | de       | 6   | 1238  | 184.2  |
|        |             | en       | 9   | 1149  | 171.2  |


For more insights into dataset statistics, visit the `data-statistics` subfolder. The dataset can be downloaded from the `data` subfolder.