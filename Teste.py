from calendarAPI import CalendarAPI

calendarEvent = CalendarAPI()
calendarEvent.authenticate()
calendarEvent.createEvent("Festa comigo, teste de envio de invite","Rua Armando Sarnes, Campinas-SP","Teste","2021-01-21T12:00:00-03:06:35","2021-01-21T17:00:00-03:06:35","",[{'email': 'thais.angelo097@gmail.com'},{'email': 'gabriel.ssouza@totvs.com.br'}],'gabrieldss808@gmail.com')