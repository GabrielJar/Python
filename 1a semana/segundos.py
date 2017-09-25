segundos = input("Por favor, entre com o número de segundos que deseja converter: ")

segundosInt = int(segundos)

dias = segundosInt // 86400
segundosRestantesDias = segundosInt % 86400
horas = segundosRestantesDias // 3600
segundosRestantesHoras = segundosRestantesDias % 3600
minutos = segundosRestantesHoras // 60
segundosRestantesMinutos = segundosRestantesHoras % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundosRestantesMinutos, "segundos.")