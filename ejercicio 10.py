
rounds = [
{
'theme': 'Entrada',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Santiago': {'judge_1': 6, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 8},
}
},
{
'theme': 'Plato principal',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Mateo': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Camila': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Lucía': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
}
},
{
'theme': 'Postre',
'scores': {
'Valentina': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Mateo': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Santiago': {'judge_1': 7, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
}
},
{
'theme': 'Cocina internacional',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 9,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Santiago': {'judge_1': 8, 'judge_2': 9,
'judge_3': 7},
'Lucía': {'judge_1': 7, 'judge_2': 7,
'judge_3': 8},
}
},
{
'theme': 'Final libre',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 8,
'judge_3': 9},
'Mateo': {'judge_1': 8, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 7, 'judge_2': 7,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 7},
}
}
]


puntajes_acumulados ={'Valentina':0, 'Mateo':0, 'Camila':0,'Santiago':0,'Lucía':0}
puntaje_ronda ={'Valentina':0, 'Mateo':0, 'Camila':0,'Santiago':0,'Lucía':0}
rondas_ganadas ={'Valentina':0, 'Mateo':0, 'Camila':0,'Santiago':0,'Lucía':0}
tabla_final ={'Valentina':{'puntos' :0,'rondas_ganadas':0,'mejor ronda':-1,'promedio':0}, 
              'Mateo':{'puntos' :0,'rondas_ganadas':0,'mejor ronda':-1,'promedio':0},
              'Camila':{'puntos' :0,'rondas_ganadas':0,'mejor ronda':-1,'promedio':0},
              'Santiago':{'puntos' :0,'rondas_ganadas':0,'mejor ronda':-1,'promedio':0},
              'Lucía':{'puntos' :0,'rondas_ganadas':0,'mejor ronda':-1,'promedio':0}}

ronda =1
for rondas in rounds :
    print('ronda numero',ronda)
    ronda +=1
    for nombre, puntaje in rondas['scores'].items():
        sumatoria = sum(puntaje.values())
        puntajes_acumulados[nombre]+=sumatoria

        tabla_final[nombre]["puntos"]+=sumatoria

        puntaje_ronda[nombre] = sumatoria

        if sumatoria > tabla_final[nombre]["mejor ronda"]:
            tabla_final[nombre]["mejor ronda"] =sumatoria
        
    max_puntaje = max(puntaje_ronda.values())
    
    ranking = sorted(puntajes_acumulados.items(), key = lambda x: x[1], reverse =True)
    posicion =1
    
    

    for nombre, puntaje in puntaje_ronda.items() :
        if puntaje ==max_puntaje :
            rondas_ganadas[nombre]+=1
            tabla_final[nombre]["rondas_ganadas"]+=1

        print(f"{posicion} - {nombre} - {puntaje}")
        posicion +=1

for nombre in tabla_final :
     tabla_final[nombre]["promedio"] = tabla_final[nombre]["puntos"]/len(rounds)
print('\nTABLA FINAL')
for nombre in tabla_final:
    print(f"{nombre}")
    print(f"-- Puntos totales : {tabla_final[nombre]['puntos']}")
    print(f"-- Rondas ganadas: {tabla_final[nombre]['rondas_ganadas']}")
    print(f"-- Mejor ronda   : {tabla_final[nombre]['mejor ronda']}")
    print(f"-- Promedio      : {tabla_final[nombre]['promedio']:.2f}")
    print("--" * 35)


    