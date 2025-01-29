### Plot based vector searching with pgvector in fastapi
---
This module use pgvector of postgresql. Here movies plot convert to embedding format using Hugging Face all-MiniLM-L6-v2 models. 
One api is deployed in fastapi to show this.   

---
#### Pre-requistics
1. Need to install and enable vector extension 
You can download models and embdedding plot as follow github links:   
[https://github.com/pgvector/pgvector](https://github.com/pgvector/pgvector)
2. You can use interface api (I used it so my respopnse  have more delay) to hugging face with api token.   [https://huggingface.co/docs/huggingface_hub/v0.13.2/en/guides/inference](https://huggingface.co/docs/huggingface_hub/v0.13.2/en/guides/inference)  
Or you can down whole models and used it as follow: 
[https://huggingface.co/sentence-transformers](https://huggingface.co/sentence-transformers)
---
### How to run this.
---   
1. Set up .env file with following keys.Set value as per your requirements
````
HF_TOKEN=xxxx # hugging face token
EMBEDDING_URL=https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2
DATABASE_URL=postgresql://postgres:postgres@localhost/sample_movie
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_NAME=sample_movie
DATABASE_PORT=5432
````
2. Install dependenceny   
````
pip install -r requirements.txt
````
3. Run the below command to start fastapi
````
uvicorn main:app --reload
````
4. You can see api swagger here [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

![Api list](api_swagger.jpg)

Other References:
----

1. [https://www.datacamp.com/tutorial/pgvector-tutorial](https://www.datacamp.com/tutorial/pgvector-tutorial)   
2. [https://github.com/pgvector/pgvector-python](https://github.com/pgvector/pgvector-python)
3. [https://github.com/pgvector/pgvector/blob/master/Dockerfile](https://github.com/pgvector/pgvector/blob/master/Dockerfile)