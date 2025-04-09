# The **LLMs4Subjects** Shared Task Baseline

## 📚 About

The baseline results for the **LLMs4Subjects shared task** were obtained using OpenAI's **GPT-4o** model. Two distinct OpenAI Assistants, named **all-subjects** and **tib-core-subjects**, were employed to perform inferences with predefined prompts and GND (Gemeinsame Normdatei) subject specifications. These Assistants generated **50 suggested GND subject tags** for each TIBKAT record. The outputs were subsequently evaluated to establish the baseline results for the LLMs4Subjects shared task.

## 🛠️ OPENAI Assistant API

The OpenAI Assistant API enables the development of AI assistants equipped with essential tools and integrations. Each Assistant is configured with specific instructions and can utilize models, tools, and files to respond to user queries. For this shared task, two Assistants were created: one for the **all-subjects** category and another for the **tib-core-subjects** category. The GND subject specifications were provided to these Assistants through two files: [GND-Subjects-all.json](../shared-task-datasets/GND/dataset/GND-Subjects-all.json) and [GND-Subjects-tib-core.json](../shared-task-datasets/GND/dataset/GND-Subjects-tib-core.json) by storing them into **vector stores** on OpenAI servers. This vector store was then incorporated into a file-search tool, which operates by querying vector stores containing pre-computed vector embeddings of the GND subject tags. When a TIBKAT record is processed, its title and abstract are transformed into a vector embedding using the GPT-4o model. This query embedding is then compared against the embeddings of the GND subject tags stored in the vector store to identify the most semantically similar tags. The prompts used for these Assistants are available at [all-subject-assistant](prompts/all-subject-assistant.txt) and [tib-core-assistant](prompts/tib-core-assistant.txt). The API endpoints for these Assistants were utilized to obtain the suggested GND subject codes based on the title and abstract of each TIBKAT record.

## 🔬 Experiments

The OpenAI Assistants were executed on the test dataset for both categories: **all-subjects** and **tib-core-subjects**. The all-subjects test split comprised 27,986 records, while the tib-core-subjects test split contained 6,174 records. Each request's output was formatted as a JSON object containing the GND code and name, adhering to the schema defined in [response_format.json](response_format.json). In total, 34,160 records were annotated with GND subjects during these experiments. The total cost incurred for these experiments was approximately $3,000.

## 📊 Evaluation Metrics

To assess the performance of the baseline and compare it with participant submissions, we evaluated the results using average Precision, Recall, and F1-score at varying values of K (i.e., top-K predicted subjects). These metrics were computed across different levels of granularity, in alignment with the LLMs4Subjects shared task evaluation protocol.

The overall ranking of all participant systems, along with the baseline results, can be found [here](https://sites.google.com/view/llms4subjects/team-results-leaderboard)

## 📌 References

1. [OpenAI Assistant API Documentation](https://platform.openai.com/docs/api-reference/assistants)
2. [OpenAI Vector Stores](https://platform.openai.com/docs/api-reference/vector-stores)