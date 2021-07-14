# Queues
- All queues must import the broker object from the app.py file.
- Queues are defined using the notion shown below:
  ```
  @broker.queue('queue name')
  def queue(ch, method, properties, body):
    print(body)
  ```
