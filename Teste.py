from calendarAPI import CalendarAPI

calendarEvent = CalendarAPI()
calendarEvent.authenticate()
calendarEvent.createEvent("Teste De Criação de Eventos",
                        "",
                        "Teste",
                        "2021-01-21T12:00:00-03:00:00",
                        "2021-01-21T17:00:00-03:00:00",
                        "",
                        [{'email': 'thais.angelo097@gmail.com'},{'email': 'gabriel.ssouza@totvs.com.br'},{'email': 'thais.angelo@totvs.com.br'}],
                        'gabrieldss808@gmail.com'
                        )