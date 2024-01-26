import random
import string
from locust import HttpUser, task, between


def genera_stringa_casuale(lunghezza, caratteri=string.ascii_letters + string.digits):
    """Genera una stringa casuale."""
    return ''.join(random.choice(caratteri) for _ in range(lunghezza))

class ApiUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def get(self):
        query = '''
        query MyQuery {
            getAllTodo {
                dateCreated
                dateExpire
                description
                emailUser
                favorite
                id
                priority
                statusDone
                title
            }
        }'''
        self.client.post("/graphql", json={"query": query})

    @task(2)
    def create(self):
        mutation = '''
        mutation MyMutation {{
            createTodo(
                todoData: {{title: "{titolo}", description: "{desc}", dateCreated: "24-12-2", dateExpire: "24-02-2", statusDone: false, emailUser: "{email}", priority: 10, favorite: false}}
            ) {{
                dateCreated
                dateExpire
                description
                emailUser
                favorite
                id
                priority
                statusDone
                title
            }}
            }}
        '''.format(titolo=genera_stringa_casuale(10), desc=genera_stringa_casuale(10), email=genera_stringa_casuale(10))

        self.client.post("/graphql", json={"query": mutation})

    @task(3)
    def update(self):
        mutation = '''
        mutation MyMutation {{
            updateTodo(
                id: 9
                todoData: {{title: "{titolo}", description: "{desc}", dateCreated: "24-12-2", dateExpire: "24-02-2", statusDone: false, emailUser: "{email}", priority: 10, favorite: false}}
            )
            }}
        '''.format(titolo=genera_stringa_casuale(10), desc=genera_stringa_casuale(10), email=genera_stringa_casuale(10))

        self.client.post("/graphql", json={"query": mutation})

    @task(4)
    def delete(self):
        mutation = f'''
        mutation MyMutation {{
                deleteTodo(id: {random.randint(1,200)})
                }}
        '''
        self.client.post("/graphql", json={"query": mutation})
        
    @task(5)
    def read(self):
        mutation = '''
        query MyQuery {
                getAllTodo {
                    dateCreated
                    dateExpire
                    description
                    favorite
                    emailUser
                    id
                    priority
                    statusDone
                    title
                }
            }
        '''
        self.client.post("/graphql", json={"query": mutation})

    # @task(2)
    # def update(self):
    #     payload = {
    #         "name": "example_item",
    #         "description": "Just a test item"
    #     }
    #     headers = {'Content-Type': 'application/json'}
    #     self.client.post("/api/v1/create", json=payload, headers=headers)
