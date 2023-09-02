## class CLIENT 
The client class is a software component that provides interaction with the API. Typically, the client class includes methods for sending requests to the API server, processing responses, and interacting with other application components.

In the client class, we can combine all API methods for a specific service or set of services. This allows you to simplify the code and simplify the interaction with the API for other components of the application. The client class can contain methods for authentication, sending requests to the server, processing responses, parsing data, and other operations necessary to work with the API.
Creating a client class is a good programming practice when working with the API, as it simplifies the code and allows you to reuse API methods in various parts of the application.

____
Класс клиент - это программный компонент, который обеспечивает взаимодействие с API. Обычно класс клиент включает в себя методы для отправки запросов на сервер API, обработки ответов и взаимодействия с другими компонентами приложения.

В классе клиент мы можем объединить все методы API для определенного сервиса или набора сервисов. Это позволяет упростить код и упростить взаимодействие с API для других компонентов приложения. Класс клиент может содержать методы для аутентификации, отправки запросов на сервер, обработки ответов, парсинга данных и других операций, необходимых для работы с API.
Создание класса клиента - это хорошая практика программирования при работе с API, так как он упрощает код и позволяет повторно использовать методы API в различных частях приложения.


### The end code after full refactoring (the part of code, for example):

```
import requests
from requests import Response
from ..models.registaration_model import Registration_model
from ..models.change_password import Change_password
from ..models.change_email import Change_email
from ..models.reset_password import Reset_password
from requests import session
class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        self.session.headers = headers

    def post_v1_account(self, json: Registration_model, **kwargs) -> Response:

        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=json,
            **kwargs
        )
        return response

    def post_account_password_change(self, json: Change_password, **kwargs) -> Response:

        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_token(self):

        token = '221312'
        response = requests.put(
            url=f"{self.host}/v1/account/{token}"
        )
        return response
```

## class FACADE

Facade class and the first test

The facade class is a design pattern that provides a simple interface for interacting with a set of components or subsystems. In the context of working with the API, the facade class can be used to combine several client classes into one simplified interface.

The facade class includes methods that link methods from various classes of clients. This allows you to hide the complexity of interacting with several services and provide a simple interface for working with them. You can add new methods to the facade class that correspond to more complex operations performed using multiple services.

In our case, this will be the Dm Api Account class, which combines AccountApi and LoginApi
____________________________

Класс фасад и первый тест

Класс фасад - это паттерн проектирования, который обеспечивает простой интерфейс для взаимодействия с набором компонентов или подсистем. В контексте работы с API, класс фасад может использоваться для объединения нескольких классов клиентов в один упрощенный интерфейс.

Класс фасад включает в себя методы, которые связывают в себе методы из различных классов клиентов. Это позволяет скрыть сложность взаимодействия с несколькими сервисами и предоставить простой интерфейс для работы с ними. В класс фасад можно добавлять новые методы, которые соответствуют более сложным операциям, выполняемым с помощью нескольких сервисов.
В нашем случае это будет класс DmApiAccount, который связывает в себе AccountApi и LoginApi
