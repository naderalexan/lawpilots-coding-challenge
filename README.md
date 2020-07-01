# Consumer-Producer pattern implementation in python 

### Prerequisites
Install `docker-compose` and `docker`

### Run
`docker-compose up --build` 

### Test
- Run
- `docker-compose run worker sh -c "python -m lawpilots.tests"`

### Monitor
- Run
- Go to `localhost:8888`

### Tech Choices
Generally the tech choices were based upon the criteria: scalability, easy of integrations, and robustness

For the implementation of a producer-consumer pattern, there is a need for a message broker and a task queue.
For quick scripting, a simple thread safe queue would suffice, however for scaling, it is advisable to use an Advanced
Messaging Queue Protocol (AMQP). 
This project uses Rabbitmq and Celery due to the fact that they are lightweight, powerful, and extremely easy to integrate.

Alternatives: Redis, Kafka, SQS, Zookeeper, Pika, RQ, and Dramatiq

Pros:
- Subtasks support 
- Multi-language support
- Simple monitoring support
- Scalability

Cons:
- Priority queues require multiple worker to consume from different queues
- Documentation for Celery does not have the best structure / simplicity to follow  