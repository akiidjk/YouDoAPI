import random
import string
from locust import HttpUser, task, between


def genera_stringa_casuale(lunghezza, caratteri=string.ascii_letters + string.digits):
    return ''.join(random.choice(caratteri) for _ in range(lunghezza))

class ApiUser(HttpUser):
    """Class that inherits from the HttpUser class from Locust."""
    wait_time = between(1, 5)

    @task(1)
    def get(self):
        """This function sends a GET request to the specified GraphQL endpoint to retrieve all todo items."""
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
        """Method to create a new todo item using a GraphQL mutation. It generates random values for the title, description, and email, and sends a POST request to the GraphQL endpoint."""
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
        """Function to update a todo item using a GraphQL mutation."""
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
        """A function to delete a todo using a GraphQL mutation."""
        mutation = f'''
        mutation MyMutation {{
                deleteTodo(id: {random.randint(1,200)})
                }}
        '''
        self.client.post("/graphql", json={"query": mutation})

    @task(5)
    def read(self):
        """This function reads data from the GraphQL API using a specified query."""
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
